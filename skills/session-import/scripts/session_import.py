# /// script
# dependencies = []
# ///
import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="session-import script")
    parser.add_argument("--file", type=str, required=True)
    args = parser.parse_args()

    if not Path(args.file).exists():
        sys.stderr.write("File not found\n")
        return 1

    try:
        with Path(args.file).open("r", encoding="utf-8") as f:
            data = json.load(f)
        sys.stdout.write(json.dumps({"status": "imported", "data": data}) + "\n")
    except Exception as e:  # noqa: BLE001
        sys.stderr.write(str(e) + "\n")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
