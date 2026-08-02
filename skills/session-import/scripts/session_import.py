# /// script
# dependencies = []
# ///
import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="session-import calculation and validation helper."
    )
    parser.add_argument("--file", type=str, help="Source JSON file path")
    parser.add_argument("--input", type=str, help="Input prompt or JSON payload")
    parser.add_argument("--json", action="store_true", help="Output result as formatted JSON")
    args = parser.parse_args()

    if args.file:
        if not Path(args.file).exists():
            sys.stderr.write("File not found\n")
            return 1
        try:
            with Path(args.file).open("r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:  # noqa: BLE001
            sys.stderr.write(str(e) + "\n")
            return 1
        else:
            sys.stdout.write(json.dumps({"status": "imported", "data": data}) + "\n")
            return 0

    result = {
        "skill": "session-import",
        "status": "success",
        "input": args.input,
    }

    if args.json:
        sys.stdout.write(json.dumps(result, indent=2) + "\n")
    else:
        sys.stdout.write(json.dumps(result) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
