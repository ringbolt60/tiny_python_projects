#!/usr/bin/env python3
"""tests for crowsnest.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = './crowsnest.py'
consonant_words = [
    'brigantine', 'clipper', 'dreadnought', 'frigate', 'galleon', 'haddock',
    'junk', 'ketch', 'longboat', 'mullet', 'narwhal', 'porpoise', 'quay',
    'regatta', 'submarine', 'tanker', 'vessel', 'whale', 'xebec', 'yatch',
    'zebrafish'
]
vowel_words = ['aviso', 'eel', 'iceberg', 'octopus', 'upbound']
disallowed_words = ['7haret', '_tresd', '!aargh', '2@!']
larboard_template = 'Ahoy, Captain, {} {} off the larboard bow!'
starboard_template = 'Ahoy, Captain, {} {} off the starboard bow!'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_consonant():
    """brigantine -> a brigantine"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == larboard_template.format('a', word)


# --------------------------------------------------
def test_consonant_upper():
    """brigantine -> a Brigatine"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word.title()}')
        assert out.strip() == larboard_template.format('A', word.title())


# --------------------------------------------------
def test_vowel():
    """octopus -> an octopus"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == larboard_template.format('an', word)


# --------------------------------------------------
def test_vowel_upper():
    """octopus -> an Octopus"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word.upper()}')
        assert out.strip() == larboard_template.format('An', word.upper())


# --------------------------------------------------
def test_vowel_case_agreement():
    """Octopus -> An Octopus"""

    for word in vowel_words:
        cap_word = word.title()
        out = getoutput(f'{prg} {cap_word}')
        assert out.strip() == larboard_template.format('An', cap_word)


# --------------------------------------------------
def test_consonant_case_agreement():
    """Brigantine -> A Brigantine"""

    for word in consonant_words:
        cap_word = word.title()
        out = getoutput(f'{prg} {cap_word}')
        assert out.strip() == larboard_template.format('A', cap_word)


# --------------------------------------------------
def test_starboard_flag():
    """starboard bow if flag on"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word} -s')
        assert out.strip() == starboard_template.format('a', word)


# --------------------------------------------------
def test_starboard_flag_full():
    """starboard bow if flag on"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word} --starboard')
        assert out.strip() == starboard_template.format('a', word)


# --------------------------------------------------
def test_reject_non_letter_start():
    """7haret is rejected at command line"""

    for word in disallowed_words:
        out = getoutput(f'{prg} {word}')
        assert f"error: name {word} must start with letter" in out.strip()
