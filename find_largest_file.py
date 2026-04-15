#!/usr/bin/env python3

import argparse
import os
import sys


def find_largest_file(directory: str):
    largest_file_path = None
    largest_size = -1

    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            try:
                size = os.path.getsize(filepath)
            except OSError as exc:
                print(f"Warning: could not access {filepath}: {exc}", file=sys.stderr)
                continue

            if size > largest_size:
                largest_size = size
                largest_file_path = filepath

    return largest_file_path, largest_size


def format_size(size: int) -> str:
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    value = float(size)

    for unit in units:
        if value < 1024 or unit == units[-1]:
            return f"{value:.2f} {unit}"
        value /= 1024

    return f"{size} B"


def main():
    parser = argparse.ArgumentParser(
        description="Find the largest file in a directory and its subdirectories."
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Directory to search (defaults to current directory).",
    )

    args = parser.parse_args()
    directory = args.directory

    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory.", file=sys.stderr)
        sys.exit(1)

    largest_file_path, largest_size = find_largest_file(directory)

    if largest_file_path is None:
        print("No files found.")
        sys.exit(0)

    print(f"Filename: {os.path.basename(largest_file_path)}")
    print(f"Path: {os.path.abspath(largest_file_path)}")
    print(f"Size: {largest_size} bytes ({format_size(largest_size)})")


if __name__ == "__main__":
    main()