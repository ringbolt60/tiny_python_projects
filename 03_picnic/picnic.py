#!/usr/bin/env python3
"""
Author : Jon Walters <ringbolt60@gmail.com>
Date   : 2023-08-21
Purpose: Go on a picnic
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Picnic game",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "items", metavar="str", nargs="+", help="Item(s) to bring", type=str
    )
    parser.add_argument(
        "-S",
        "--separator",
        metavar="str",
        help="custom separator (; or : or -)",
        type=str,
        default=",",
    )

    parser.add_argument("-s", "--sorted", help="Sort the items", action="store_true")
    parser.add_argument(
        "-o", "--no_oxford", help="Print without Oxford comma", action="store_true"
    )

    args = parser.parse_args()
    if args.separator not in ",:;-":
        parser.error(
            f"{args.separator} not a valid separator requires , or : or ; or -"
        )
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Start doing stuff here."""

    args = get_args()
    items = args.items
    sep = args.separator + " "
    number_of_items = len(items)
    if args.sorted:
        items.sort()
    if number_of_items == 1:
        items_brought = items[0]
    elif number_of_items == 2:
        items_brought = " and ".join(items)
    else:
        final_item = f"{sep}and {items.pop()}"
        if args.no_oxford:
            final_item = final_item[1:]
        items_brought = sep.join(items) + final_item

    print(f"You are bringing {items_brought}.")


# --------------------------------------------------
if __name__ == "__main__":
    main()
