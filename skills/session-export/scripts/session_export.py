# /// script
# dependencies = []
# ///
import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="session-export calculation and validation helper."
    )
    parser.add_argument("--file", type=str, help="Target JSON file path")
    parser.add_argument("--data", type=str, help="JSON payload to export")
    parser.add_argument("--input", type=str, help="Input prompt or JSON payload")
    parser.add_argument("--json", action="store_true", help="Output result as formatted JSON")
    args = parser.parse_args()

    if args.file and args.data:
        try:
            parsed_data = json.loads(args.data)
            with Path(args.file).open("w", encoding="utf-8") as f:
                json.dump(parsed_data, f)
        except Exception as e:  # noqa: BLE001
            sys.stderr.write(str(e) + "\n")
            return 1
        else:
            sys.stdout.write(json.dumps({"status": "exported"}) + "\n")
            return 0

    result = {
        "skill": "session-export",
        "status": "success",
        "input": args.input or args.data,
    }

    if args.json:
        sys.stdout.write(json.dumps(result, indent=2) + "\n")
    else:
        sys.stdout.write(json.dumps(result) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
