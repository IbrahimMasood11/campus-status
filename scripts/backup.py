#!/usr/bin/env python3
"""Create a simple timestamped backup of selected Campus Status files."""

from __future__ import annotations

import datetime as dt
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def copy_item(source: Path, destination: Path) -> None:
    if source.is_dir():
        shutil.copytree(source, destination / source.name, dirs_exist_ok=True)
    elif source.is_file():
        destination.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination / source.name)
    else:
        print(f"Skipping missing item: {source}")


def main() -> int:
    config = load_json(ROOT / "config" / "backup.json")
    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_root = ROOT / config["backup_dir"] / timestamp
    backup_root.mkdir(parents=True, exist_ok=True)

    for item in config["include"]:
        copy_item(ROOT / item, backup_root)

    print(f"Backup written to {backup_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
