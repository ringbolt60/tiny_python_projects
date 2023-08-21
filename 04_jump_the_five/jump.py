#!/usr/bin/env python3
"""
Author : Jon Walters <ringbolt60@gmail.com>
Date   : 2023-08-21
Purpose: Encode telephone numbers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Encode telephone numbers",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "tel_number",
        type=str,
        metavar="STRING",
        help="Contains a telephone number to be encoded",
    )

    return parser.parse_args()



# --------------------------------------------------
def main():
    """Start doing stuff here."""

    args = get_args()
    coding = {
        "0": "5",
        "1": "9",
        "2": "8",
        "3": "7",
        "4": "6",
        "5": "0",
        "6": "4",
        "7": "3",
        "8": "2",
        "9": "1",
    }
    print("".join([coding.get(char, char) for char in args.tel_number]))


# --------------------------------------------------
if __name__ == "__main__":
    main()
