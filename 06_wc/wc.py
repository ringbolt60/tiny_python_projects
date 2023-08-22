#!/usr/bin/env python3
"""
Author : Jon Walters <ringbolt60@gmail.com>
Date   : 2023-08-22
Purpose: Emulate wc (word count)
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Emulate wc (word count)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
        metavar="FILE",
        help="Input file(s)",
        type=argparse.FileType("rt"),
        default=[sys.stdin],
        nargs="*",
    )

    parser.add_argument(
        "-l",
        "--lines",
        help="Print line count",
        action="store_true",
    )

    parser.add_argument(
        "-w",
        "--words",
        help="Print word count",
        action="store_true",
    )

    parser.add_argument(
        "-c",
        "--characters",
        help="Print character count",
        action="store_true",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Start doing stuff here."""

    args = get_args()
    if args.lines is False and args.words is False and args.characters is False:
        args.lines, args.words, args.characters = True, True, True
    total_lines, total_words, total_bytes = 0, 0, 0
    for fh in args.file:
        num_lines, num_words, num_bytes = 0, 0, 0
        for line in fh:
            num_lines += 1
            num_words += len(line.split())
            num_bytes += len(line)
        total_lines += num_lines
        total_words += num_words
        total_bytes += num_bytes
        lines = f"{num_lines:8}" if args.lines else ''
        words = f"{num_words:8}" if args.words else ''
        characters = f"{num_bytes:8}" if args.characters else ""
        print(f"{lines}{words}{characters} {fh.name}")
    if len(args.file) > 1:
        lines = f"{total_lines:8}" if args.lines else ""
        words = f"{total_words:8}" if args.words else ""
        characters = f"{total_bytes:8}" if args.characters else ""
        print(f"{lines}{words}{characters} total")


# --------------------------------------------------
if __name__ == "__main__":
    main()
