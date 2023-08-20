#!/usr/bin/env python3
"""
Author : Jon Walters <ringbolt60@gmail.com>
Date   : 2023-08-20
Purpose: Crow's Nest -- choose the correct article
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("word", metavar="word", help="A word")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Start doing stuff here."""

    args = get_args()
    word = args.word
    article = "an" if word[0].lower() in "aeiou" else "a"
    print(f"Ahoy, Captain, {article} {word} " f"off the larboard bow!")


# --------------------------------------------------
if __name__ == "__main__":
    main()
