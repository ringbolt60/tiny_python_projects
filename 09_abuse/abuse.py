#!/usr/bin/env python3
"""
Author : Jon Walters <ringbolt60@gmail.com>
Date   : 2023-08-25
Purpose: Roundly abuse your enemies
"""

import argparse
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Roundly abuse your enemies",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-a",
        "--adjectives",
        help="Number of adjectives",
        metavar="adjectives",
        type=int,
        default=2,
    )

    parser.add_argument(
        "-n",
        "--number",
        help="Number of insults",
        metavar="insults",
        type=int,
        default=3,
    )

    parser.add_argument(
        "-s", "--seed", help="Random seed", metavar="seed", type=int, default=None
    )

    parser.add_argument(
        "-A",
        "--adjective_file",
        help="File of adjectives",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default="./data/adjectives.txt",
    )

    parser.add_argument(
        "-N",
        "--noun_file",
        help="File of nouns",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default="./data/nouns.txt",
    )

    args = parser.parse_args()

    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')

    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Start doing stuff here."""

    args = get_args()
    random.seed(args.seed)
    adjectives = [line.rstrip() for line in args.adjective_file]
    nouns = [line.rstrip() for line in args.noun_file]
    for _ in range(args.number):
        adjs = ", ".join(random.sample(adjectives, args.adjectives))
        print(f"You {adjs} {random.choice(nouns)}!")


# --------------------------------------------------
if __name__ == "__main__":
    main()
