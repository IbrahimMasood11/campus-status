#!/usr/bin/env python3
"""Validate Campus Status configuration files using the Python standard library."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config"


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate_service() -> None:
    data = load_json(CONFIG / "service.json")
    require(isinstance(data.get("service_name"), str) and data["service_name"], "service_name must be set")
    require(data.get("host") in {"localhost", "127.0.0.1"}, "host should be localhost for the lab demo")
    require(isinstance(data.get("port"), int), "port must be an integer")
    require(1 <= data["port"] <= 65535, "port must be in the valid TCP port range")
    require(isinstance(data.get("health_path"), str) and data["health_path"].startswith("/"), "health_path must start with /")


def validate_monitoring() -> None:
    data = load_json(CONFIG / "monitoring.json")
    require(isinstance(data.get("interval_seconds"), int), "interval_seconds must be an integer")
    require(5 <= data["interval_seconds"] <= 3600, "interval_seconds must be between 5 and 3600")
    require(isinstance(data.get("timeout_seconds"), int), "timeout_seconds must be an integer")
    require(1 <= data["timeout_seconds"] <= 60, "timeout_seconds must be between 1 and 60")
    require(data.get("expected_status") == 200, "expected_status should be 200 for the demo")


def validate_backup() -> None:
    data = load_json(CONFIG / "backup.json")
    require(isinstance(data.get("backup_dir"), str) and data["backup_dir"], "backup_dir must be set")
    require(isinstance(data.get("retention_days"), int), "retention_days must be an integer")
    require(1 <= data["retention_days"] <= 365, "retention_days must be between 1 and 365")
    require(isinstance(data.get("include"), list) and data["include"], "include must be a non-empty list")


def main() -> int:
    try:
        validate_service()
        validate_monitoring()
        validate_backup()
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"CONFIG INVALID: {error}")
        return 1

    print("CONFIG OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
