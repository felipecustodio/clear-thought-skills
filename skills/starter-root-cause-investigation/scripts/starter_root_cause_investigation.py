# /// script
# dependencies = []
# ///
import argparse
import json
import sys


def main() -> int:
    parser = argparse.ArgumentParser(
        description="starter-root-cause-investigation starter orchestration helper."
    )
    parser.add_argument("--input", type=str, help="Input problem prompt or JSON payload")
    parser.add_argument("--json", action="store_true", help="Output result as formatted JSON")
    args = parser.parse_args()

    result = {
        "starter_skill": "starter-root-cause-investigation",
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
