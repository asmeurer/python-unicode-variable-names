#!/usr/bin/env python
"""
Generate a list of all Unicode characters that are valid in Python identifiers

Documentation reference: https://docs.python.org/3/reference/lexical_analysis.html#identifiers
"""

import sys
import unicodedata

WARNING = """\
<!-- WARNING: This file is generated automatically, do not edit it
directly. Rather, edit the file generate_names.py which generates this file.
-->

"""

FOOTER = """

[^unknown]: The Unicode name for this character is not present in the
            `unicodedata` database. You may be able to find more by searching
            the character on
            [fileformat.info](http://www.fileformat.info/info/unicode/char/search.htm)
            or [Wikipedia](https://www.wikipedia.org/).
"""

def generate_characters():
    start_characters = []
    continue_characters = []
    for i in range(0x110000):
        c = chr(i)
        if c.isidentifier():
            start_characters.append(c)
        elif ('a' + c).isidentifier():
            continue_characters.append(c)

    return start_characters, continue_characters

def write_character(f, c):
    try:
        name = unicodedata.name(c)
    except ValueError:
        name = "(unknown) [^unknown]"
    n = unicodedata.normalize('NFKC', c)
    f.write(f"| U+{ord(c):04X} | {c} | {name}")
    if c != n:
        names = ', '.join(unicodedata.name(i) for i in n)
        f.write(f" (normalizes to {', '.join('U+{x:04X}'.format(x=ord(i)) for i in n)}: {n} ({names}))")
    f.write('|\n')

def main():
    start_characters, continue_characters = generate_characters()

    header = f"""\
This page was generated using Python version {sys.version.split()[0]}, which
uses Unicode version {unicodedata.unidata_version}

"""

    table_header = """\
| Code point | Character | Name |
|------------|-----------|------|
"""

    with open("docs/start-characters.md", 'w') as f:
        f.write(WARNING)
        f.write("## Start Characters\n\n")
        f.write("""
These are the characters that are valid as any character in a Python variable
name. For a list of characters that are valid for any character other than the
first, see the [Continue Characters](continue-characters).

You can also view the <a href="start-characters.md">raw markdown</a> for this page.

""")
        f.write(header)
        f.write(f"There are a total of {len(start_characters)} characters in this list.\n\n")
        f.write(table_header)
        for c in start_characters:
            write_character(f, c)
        f.write(FOOTER)

    with open('docs/continue-characters.md', 'w') as f:
        f.write(WARNING)
        f.write("## Continue Characters\n\n")
        f.write("""
These are the characters that are valid as any character other than the first
in a Python variable name. For a list of characters that are valid for any
character including the first, see the [Start Characters](start-characters).

You can also view the <a href="continue-characters.md">raw markdown</a> for this page.

""")
        f.write(header)
        f.write(f"There are a total of {len(continue_characters)} characters in this list.\n\n")
        f.write(table_header)
        for c in continue_characters:
            write_character(f, c)
        f.write(FOOTER)

if __name__ == '__main__':
    main()
