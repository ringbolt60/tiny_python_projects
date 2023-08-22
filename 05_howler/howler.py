#!/usr/bin/env python3
"""
Author : Jon Walters <ringbolt60@gmail.com>
Date   : 2023-08-21
Purpose: Howl at people
"""

import argparse
import io
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Howl at people",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "text", metavar="TEXT", help="Input string(s) or file name(s)", type=str, nargs="+",
    )

    parser.add_argument(
        "-o",
        "--outdir",
        help="Output directory",
        metavar="STRING",
        type=str,
        default="",
    )

    parser.add_argument("-l", "--lower", help="Output in lower case", action="store_true")

    args = parser.parse_args()


    """
    for text in args.text:
        if os.path.isfile(text):
            text = open(text)
        else:
            text = io.StringIO(initial_value=text + "\n")
    """
    return args


# --------------------------------------------------
def main():
    """Start doing stuff here."""

    args = get_args()
    if args.outdir and not os.path.isdir(args.outdir):
        os.mkdir("./" + args.outdir)

    for text in args.text:
        text_in = open(text) if os.path.isfile(text) else io.StringIO(initial_value=text + "\n")
        basename = os.path.basename(text)
        out_fh = open(os.path.join("./", args.outdir, basename), "wt") if args.outdir else sys.stdout
        for line in text_in:
            out_line = line.lower() if args.lower else line.upper()
            out_fh.write(out_line)
        out_fh.close()


# --------------------------------------------------
if __name__ == "__main__":
    main()
