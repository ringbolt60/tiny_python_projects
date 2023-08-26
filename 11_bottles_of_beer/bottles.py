#!/usr/bin/env python3
"""
Author : Jon Walters <ringbolt60@gmail.com>
Date   : 2023-08-26
Purpose: Ten green bottles
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Ten green bottles",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-n", "--num", help="How many bottles", metavar="number", type=int, default=10
    )

    args = parser.parse_args()
    if not (0 <= args.num <= 12):
        parser.error(f'--num "{args.num}" must be between 1 and 12 inclusive')

    return args


# --------------------------------------------------
def verse(bottle):
    """Sing a verse."""

    numbers = "Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve".split()
    if bottle == 1:
        first_line = f"One green bottle standing on the wall,"
        last_line = "There'd be no green bottles standing on the wall!"
    else:
        first_line = f"{numbers[bottle-2]} green bottles standing on the wall,"
        if bottle == 2:
            last_line = f"There'd be one green bottle standing on the wall!"
        else:
            last_line = f"There'd be {numbers[bottle-3].lower()} green bottles standing on the wall!"
    second_line = first_line
    return "\n".join(
        [first_line, second_line,
         "And if one green bottle should accidentally fall,", last_line]
    )


def test_verse():
    """Test a verse"""
    last_verse = verse(1)
    assert last_verse == "\n".join(
        [
            'One green bottle standing on the wall,',
            'One green bottle standing on the wall,',
            'And if one green bottle should accidentally fall,',
            "There'd be no green bottles standing on the wall!",
        ]
    )

    two_bottles = verse(2)
    assert two_bottles == "\n".join(
        [
            "Two green bottles standing on the wall,",
            "Two green bottles standing on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'd be one green bottle standing on the wall!",
]
    )

    three_bottles = verse(3)
    assert three_bottles == "\n".join(
        [
            "Three green bottles standing on the wall,",
            "Three green bottles standing on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'd be two green bottles standing on the wall!",
        ]
    )


# --------------------------------------------------
def main():
    """Start doing stuff here."""

    args = get_args()

    # for n in range(args.num, 1, -1):
    #     print(verse(n) + "\n")
    # print(verse(1))

    #print("\n\n".join([verse(n) for n in range(args.num, 0, -1)]))

    print("\n\n".join(list(map(verse, range(args.num, 0, -1)))))


# --------------------------------------------------
if __name__ == "__main__":
    main()
