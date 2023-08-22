#!/usr/bin/env python3
"""
Author : Jon Walters <ringbolt60@gmail.com>
Date   : 2023-08-22
Purpose: Morbid poetry
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Morbid poetry",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "letter",
        metavar="LETTER",
        help="Letter(s)",
        nargs="+",
    )

    parser.add_argument(
        "-f",
        "--file",
        help="Input file",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default="gashlycrumb.txt",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Start doing stuff here."""

    args = get_args()
    lookup = {line[0].lower(): line.rstrip() for line in args.file}
    for letter in args.letter:
        print(lookup.get(letter.lower(), f'I do not know "{letter}".'))


# --------------------------------------------------
if __name__ == "__main__":
    main()
