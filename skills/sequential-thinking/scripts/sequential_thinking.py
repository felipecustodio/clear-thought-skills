# /// script
# dependencies = []
# ///
import argparse
import json
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description="sequential-thinking script")
    parser.add_argument("--thought", type=str, required=True)
    parser.add_argument("--number", type=int, required=True)
    args = parser.parse_args()

    output = {"status": "ok", "thought": args.thought, "number": args.number}
    sys.stdout.write(json.dumps(output) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
