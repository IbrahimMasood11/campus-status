#!/usr/bin/env python3
"""Check whether the local Campus Status demo service is responding."""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    service = load_json(ROOT / "config" / "service.json")
    monitoring = load_json(ROOT / "config" / "monitoring.json")

    url = f"http://{service['host']}:{service['port']}{service['health_path']}"
    timeout = monitoring["timeout_seconds"]
    expected = monitoring["expected_status"]

    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            status = response.status
    except urllib.error.URLError as error:
        print(f"SERVICE UNAVAILABLE: {error}")
        return 1

    if status != expected:
        print(f"UNEXPECTED STATUS: got {status}, expected {expected}")
        return 1

    print(f"SERVICE OK: {url} returned {status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
