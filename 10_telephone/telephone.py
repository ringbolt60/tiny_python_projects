#!/usr/bin/env python3
"""
Author : Jon Walters <ringbolt60@gmail.com>
Date   : 2023-08-25
Purpose: Chinese Whispers
"""

import argparse
import os
import random
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Chinese Whispers",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="TEXT", help="Input text or file")

    parser.add_argument(
        "-s", "--seed", help="Random seed", metavar="seed", type=int, default=None
    )

    parser.add_argument(
        "-m",
        "--mutations",
        help="Percent mutations",
        metavar="mutations",
        type=float,
        default=0.1,
    )

    args = parser.parse_args()
    if not 0 <= args.mutations <= 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    if os.path.isfile(args.text):
        with open(args.text) as fh:
            args.text = fh.read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Start doing stuff here."""

    args = get_args()
    text, mutations, seed = args.text, args.mutations, args.seed
    random.seed(seed)
    num_mutations = round(len(text) * mutations)
    alpha = "".join(sorted(string.ascii_letters + string.punctuation))
    index = random.sample(range(len(text)), num_mutations)
    new_text = list(text)
    for i in index:
        new_text[i] = random.choice(alpha.replace(new_text[i], ""))
    print(f'You said: "{text}"')
    print(f'I heard : "{"".join(new_text)}"')


# --------------------------------------------------
if __name__ == "__main__":
    main()
