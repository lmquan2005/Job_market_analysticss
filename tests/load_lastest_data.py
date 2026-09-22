import json
from pathlib import Path


RAW_DIR = Path("storage/raw_test")


def load_latest_raw():
    files = list(RAW_DIR.glob("*.json"))

    assert files, "Không tìm thấy file raw nào"

    latest_file = max(files, key=lambda f: f.stat().st_mtime)

    print(f"\nReading raw file: {latest_file}")

    with open(latest_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data