# /// script
# dependencies = []
# ///
import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="session-export script")
    parser.add_argument("--file", type=str, required=True)
    parser.add_argument("--data", type=str, required=True)
    args = parser.parse_args()

    try:
        parsed_data = json.loads(args.data)
        with Path(args.file).open("w", encoding="utf-8") as f:
            json.dump(parsed_data, f)
        sys.stdout.write(json.dumps({"status": "exported"}) + "\n")
    except Exception as e:  # noqa: BLE001
        sys.stderr.write(str(e) + "\n")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
