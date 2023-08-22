#!/usr/bin/env python3
"""tests for howler.py"""

import os
import re
import random
import shutil
import string
from subprocess import getstatusoutput, getoutput

prg = "./howler.py"


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return "".join(random.choices(string.ascii_letters + string.digits, k=k))


# --------------------------------------------------
def out_flag():
    """Either -o or --outfile"""

    return "-o" if random.randint(0, 1) else "--outdir"


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ["-h", "--help"]:
        rv, out = getstatusoutput(f"{prg} {flag}")
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_text_stdout():
    """Test STDIN/STDOUT"""

    out = getoutput(f'{prg} "foo bar baz"')
    assert out.strip() == "FOO BAR BAZ"


# --------------------------------------------------
def test_text_outfile():
    """Test STDIN/outfile"""

    out_dir = random_string()
    if os.path.isdir(out_dir):
        os.remove(out_dir)

    try:
        out = getoutput(f'{prg} {out_flag()} {out_dir} "foo bar baz"')
        assert out.strip() == ""
        assert os.path.join(out_dir, "foo bar baz")
        text = open(os.path.join(out_dir, "foo bar baz")).read().rstrip()
        assert text == "FOO BAR BAZ"
    finally:
        if os.path.isdir(out_dir):
            shutil.rmtree(out_dir)


# --------------------------------------------------
def test_file():
    """Test file in/out"""

    for expected_file in os.listdir("test-outs"):
        try:
            out_file = random_string()
            if os.path.isfile(out_file):
                os.remove(out_file)

            basename = os.path.basename(expected_file)
            in_file = os.path.join("../inputs", basename)
            out = getoutput(f"{prg} {out_flag()} {out_file} {in_file}")
            assert out.strip() == ""
            produced = open(out_file + "/" + basename).read().rstrip()
            expected = open(os.path.join("test-outs", expected_file)).read().strip()
            assert expected == produced
        finally:
            if os.path.isdir(out_file):
                shutil.rmtree(out_file)


# --------------------------------------------------
def test_text_stdout_lower():
    """Test STDIN/STDOUT"""

    for flag in ["-l", "--lower"]:
        out = getoutput(f'{prg} {flag} "FOO BAR BAZ"')
        assert out.strip() == "foo bar baz"


def test_multiple_files():
    """Test files in/out"""

    in_files = ""
    out_dir = random_string()
    if os.path.isdir(out_dir):
        os.remove(out_dir)
    for expected_file in os.listdir("test-outs"):
        basename = os.path.basename(expected_file)
        in_file = os.path.join("../test-outs", basename)
        in_files += in_file + " "
    out = getoutput(f"{prg} -o {out_dir} {in_files}")
    assert out.strip() == ""
    for out_file in os.listdir(out_dir):
        produced = open(out_dir + "/" + out_file).read().rstrip()
        expected = open(os.path.join(out_dir, out_file)).read().strip()
        assert expected == produced

    if os.path.isdir(out_dir):
        shutil.rmtree(out_dir)