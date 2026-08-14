"""Storage manager for configuration and state persistence."""

import json
import os
import re
import shutil
from pathlib import Path
from typing import Any

from pydantic import ValidationError

from ..models import CategoryRule, Config, ProfileConfig


# Matches ${VAR_NAME} in string config values. Names follow env-var rules
# (ASCII letters, digits, underscore; must not start with a digit).
_ENV_VAR_PATTERN = re.compile(r"\$\{([A-Za-z_][A-Za-z0-9_]*)\}")


def _expand_env_vars(value: Any) -> Any:
    """Recursively expand ``${VAR}`` references inside any string leaves.

    Containers (dicts, lists, tuples) are walked; non-string leaves are
    returned unchanged. Strings with no ``${...}`` tokens are returned
    unchanged. References to unset variables are **left as-is**, so
    ``${MISSING}`` round-trips to ``${MISSING}`` and surfaces as a clear
    downstream error rather than a silent empty string.

    This is intentionally identical to the behaviour ``RSSScraper`` uses
    for RSS feed URLs, so a single ``${VAR}`` convention works everywhere
    in the config (AI ``base_url``, feed URLs, webhook URLs, ...).
    """
    if isinstance(value, str):
        return _ENV_VAR_PATTERN.sub(
            lambda m: os.environ.get(m.group(1), m.group(0)),
            value,
        )
    if isinstance(value, dict):
        return {k: _expand_env_vars(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_expand_env_vars(v) for v in value]
    if isinstance(value, tuple):
        return tuple(_expand_env_vars(v) for v in value)
    return value


class ConfigError(ValueError):
    """Raised when configuration is missing or invalid."""

    pass


class StorageManager:
    """Manages file-based storage for configuration and state."""

    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.config_path = self.data_dir / "config.json"
        self.base_config_path = self.data_dir / "config.base.json"
        self.categories_dir = self.data_dir / "categories"
        self.profiles_dir = self.data_dir / "profiles"
        self.summaries_dir = self.data_dir / "summaries"

        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.categories_dir.mkdir(parents=True, exist_ok=True)
        self.profiles_dir.mkdir(parents=True, exist_ok=True)
        self.summaries_dir.mkdir(parents=True, exist_ok=True)

    def load_categories(self) -> dict[str, CategoryRule]:
        """Load all category scoring rules from data/categories/ and data/categories.json."""
        categories: dict[str, CategoryRule] = {}

        # 1. Load single file data/categories.json if present
        single_file = self.data_dir / "categories.json"
        if single_file.exists():
            try:
                with open(single_file, "r", encoding="utf-8") as f:
                    raw = json.load(f)
                raw = _expand_env_vars(raw)
                if isinstance(raw, list):
                    for item in raw:
                        cat = CategoryRule.model_validate(item)
                        categories[cat.id] = cat
                elif isinstance(raw, dict):
                    for cat_id, item in raw.items():
                        if "id" not in item:
                            item["id"] = cat_id
                        cat = CategoryRule.model_validate(item)
                        categories[cat.id] = cat
            except Exception as e:
                logger = getattr(self, "logger", None)
                if logger:
                    logger.warning("Failed to load %s: %s", single_file, e)

        # 2. Load *.json from data/categories/ directory
        if self.categories_dir.exists():
            for filepath in sorted(self.categories_dir.glob("*.json")):
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        raw = json.load(f)
                    raw = _expand_env_vars(raw)
                    if isinstance(raw, dict):
                        if "id" not in raw:
                            raw["id"] = filepath.stem
                        cat = CategoryRule.model_validate(raw)
                        categories[cat.id] = cat
                except Exception as e:
                    pass

        return categories

    def load_profiles(self) -> dict[str, ProfileConfig]:
        """Load all user profiles from data/profiles/ directory."""
        profiles: dict[str, ProfileConfig] = {}
        if self.profiles_dir.exists():
            for filepath in sorted(self.profiles_dir.glob("*.json")):
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        raw = json.load(f)
                    raw = _expand_env_vars(raw)
                    if isinstance(raw, dict):
                        if "id" not in raw:
                            raw["id"] = filepath.stem
                        if "name" not in raw:
                            raw["name"] = filepath.stem
                        prof = ProfileConfig.model_validate(raw)
                        profiles[prof.id] = prof
                except Exception as e:
                    raise ConfigError(
                        f"Failed to load profile from {filepath}: {e}"
                    ) from e
        return profiles

    def load_config(self) -> Config:
        """Load configuration, supporting base config, category rules, and profiles."""
        target_path = None
        if self.base_config_path.exists():
            target_path = self.base_config_path
        elif self.config_path.exists():
            target_path = self.config_path
        else:
            raise FileNotFoundError(
                f"Configuration file not found: {self.base_config_path} or {self.config_path}\n"
                f"Please create it based on the template in README.md"
            )

        self.loaded_config_path = target_path

        try:
            with open(target_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            raise ConfigError(
                f"Invalid JSON in configuration file: {target_path}\nError: {e}"
            ) from e

        data = _expand_env_vars(data)

        try:
            config = Config.model_validate(data)
        except ValidationError as e:
            raise ConfigError(
                f"Configuration validation failed for {target_path}\nDetails: {e}"
            ) from e

        # Merge category rules
        loaded_categories = self.load_categories()
        if loaded_categories:
            for cat_id, cat_rule in loaded_categories.items():
                if cat_id not in config.categories:
                    config.categories[cat_id] = cat_rule

        # Merge profiles from data/profiles/
        loaded_profiles = self.load_profiles()
        if loaded_profiles:
            for prof_id, prof in loaded_profiles.items():
                if prof_id not in config.profiles:
                    config.profiles[prof_id] = prof

        return config

    def save_config(self, config: Config, backup: bool = True) -> Path:
        """Save configuration to config.json, optionally backing up the existing file.

        Args:
            config: The Config object to save.
            backup: If True and config.json exists, copy it to config.json.bak first.

        Returns:
            Path to the saved config file.
        """
        if backup and self.config_path.exists():
            shutil.copy2(self.config_path, self.config_path.with_suffix(".json.bak"))

        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(config.model_dump(mode="json"), f, indent=2, ensure_ascii=False)
            f.write("\n")

        return self.config_path

    def save_daily_summary(
        self,
        date: str,
        markdown: str,
        language: str = "en",
        profile_id: str | None = None,
    ) -> Path:
        filename = f"horizon-{date}-{language}.md"
        if profile_id:
            target_dir = self.summaries_dir / profile_id
            target_dir.mkdir(parents=True, exist_ok=True)
            filepath = target_dir / filename
        else:
            filepath = self.summaries_dir / filename

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(markdown)

        return filepath

    def load_subscribers(self) -> list:
        """Loads the list of email subscribers."""
        subscribers_path = self.data_dir / "subscribers.json"
        if not subscribers_path.exists():
            return []

        try:
            with open(subscribers_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def add_subscriber(self, email_addr: str):
        """Adds a new subscriber email."""
        subscribers = self.load_subscribers()
        if email_addr not in subscribers:
            subscribers.append(email_addr)
            self._save_subscribers(subscribers)

    def remove_subscriber(self, email_addr: str):
        """Removes a subscriber email."""
        subscribers = self.load_subscribers()
        if email_addr in subscribers:
            subscribers.remove(email_addr)
            self._save_subscribers(subscribers)

    def _save_subscribers(self, subscribers: list):
        """Helper to save subscribers list."""
        subscribers_path = self.data_dir / "subscribers.json"
        with open(subscribers_path, "w", encoding="utf-8") as f:
            json.dump(subscribers, f, indent=2)
