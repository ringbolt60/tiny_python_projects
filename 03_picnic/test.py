#!/usr/bin/env python3
"""tests for picnic.py.py"""

import os
import string
from subprocess import getoutput

prg = "./picnic.py"


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ["", "-h", "--help"]:
        out = getoutput(f"{prg} {flag}")
        assert out.lower().startswith("usage")


# --------------------------------------------------
def test_one():
    """one item"""

    out = getoutput(f"{prg} chips")
    assert out.strip() == "You are bringing chips."


# --------------------------------------------------
def test_two():
    """two items"""

    out = getoutput(f'{prg} soda "french fries"')
    assert out.strip() == "You are bringing soda and french fries."


# --------------------------------------------------
def test_more_than_two():
    """more than two items"""

    arg = '"potato chips" coleslaw cupcakes "French silk pie"'
    out = getoutput(f"{prg} {arg}")
    expected = (
        "You are bringing potato chips, coleslaw, " "cupcakes, and French silk pie."
    )
    assert out.strip() == expected


# --------------------------------------------------
def test_two_sorted():
    """two items sorted output"""

    out = getoutput(f"{prg} -s soda candy")
    assert out.strip() == "You are bringing candy and soda."


# --------------------------------------------------
def test_more_than_two_sorted():
    """more than two items sorted output"""

    arg = "bananas apples dates cherries"
    for flag in ["-s", "--sorted"]:
        out = getoutput(f"{prg} {arg} {flag}")
        expected = "You are bringing apples, bananas, cherries, and dates."
        assert out.strip() == expected


# --------------------------------------------------
def test_no_oxford_comma():
    """no Oxford comma if -o switch made"""

    arg = "apples bananas cherries dates"
    for flag in ["-o", "--no_oxford"]:
        out = getoutput(f"{prg} {arg} {flag}")
        expected = "You are bringing apples, bananas, cherries and dates."
        assert out.strip() == expected


# --------------------------------------------------
def test_custom_seperator():
    """uses optional provided seperator instead of comma"""

    arg = '"potato chips" coleslaw cupcakes "French silk pie"'
    out = getoutput(f"{prg} {arg} -S ';'")
    expected = (
        "You are bringing potato chips; coleslaw; " "cupcakes; and French silk pie."
    )
    assert out.strip() == expected


# --------------------------------------------------
def test_invalid_separator_input():
    """Only , ; : - should be used as separators"""

    for sep in "".join((string.ascii_letters, string.digits)):
        out = getoutput(f"{prg} jam -S {sep}")
        assert f"error: {sep} not a valid separator" in out.strip()
