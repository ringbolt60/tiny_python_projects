#!/usr/bin/env python3
"""
Author : Jon Walters <ringbolt60@gmail.com>
Date   : 2023-08-24
Purpose: Play Apples and Bananas
"""

import argparse
import io
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Play Apples and Bananas",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="TEXT", help="Replace the vowels in this text")

    parser.add_argument(
        "-v",
        "--vowel",
        help="The vowel to be replaced (lowercase)",
        metavar="CHAR",
        type=str,
        default="a",
        choices=list('aeiou'),
    )

    args = parser.parse_args()
    args.text = (
        open(args.text)
        if os.path.isfile(args.text)
        else io.StringIO(initial_value=args.text + "\n")
    ).read()

    return args


# --------------------------------------------------
def main():
    """Start doing stuff here."""

    args = get_args()
    lookup = {}
    for vowel in "aeiou":
        lookup[vowel] = args.vowel
    for vowel in "AEIOU":
        lookup[vowel] = args.vowel.upper()
    output = args.text.translate(str.maketrans(lookup))
    final_out = output[0]
    for n, char in enumerate(output[1:]):
        if char == output[n] and char in 'aeiouAEIOU':
            pass
        else:
            final_out += char
    print("".join(final_out))


# --------------------------------------------------
if __name__ == "__main__":
    main()
