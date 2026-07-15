import argparse

from .composer import (
    new_extension,
    new_module
)
def main():
    parser = argparse.ArgumentParser(
        prog="nannokitc"
    )
    parser.add_argument(
        "--extension",
        "--ext",
        "-E"
    )
    parser.add_argument(
        "--module",
        "--mod",
        "-M",
    )
    args = parser.parse_args()
    if args.extension or args.ext or args.E:
        path = new_extension(
            args.extension
        )
        print(
            f"[OK] Created {path}"
        )
    elif args.module or args.mod or args.M:
        path = new_module(
            args.module
        )
        print(
            f"[OK] Created {path}"
        )
        
if __name__ == "__main__":
    main()