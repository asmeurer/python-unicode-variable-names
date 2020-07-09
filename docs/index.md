<!-- WARNING: This file is generated automatically, do not edit it
directly. Rather, edit the file generate_names.py which generates this file.
-->

# Python Unicode Variable Names

This page lists all the characters that are valid in Python 3 variable names.
In Python 2, variable names could only contain the ASCII characters a-z, A-Z,
0-9, and _, but in Python 3, a much larger set of Unicode characters are
allowed.

The source code for this page is on
[GitHub](https://github.com/asmeurer/python-unicode-variable-names).

The full details of which Unicode characters are allowed is described in the
[documentation](https://docs.python.org/3/reference/lexical_analysis.html#identifiers).

Be warned that Python always applies
[NFKC](https://en.wikipedia.org/wiki/Unicode_equivalence#Normalization)
normalization to characters. Therefore, two distinct characters may actually
produce the same variable name. For example:

    >>> ª = 1 # FEMININE ORDINAL INDICATOR
    >>> a # LATIN SMALL LETTER A (i.e., ASCII lowercase 'a')
    1

Normalization also combines accents, so it is possible for a valid name to
contain characters that are not present below. For example, `á` consists of
two characters, LATIN SMALL LETTER A (i.e., ASCII lowercase `a`) and COMBINING
ACUTE ACCENT. The second character, COMBINING ACUTE ACCENT, is not present in
the list below because it is not valid in an identifier by itself. However,
when it follows `a`, the two characters together NFKC normalize to the single
character `á` (LATIN SMALL LETTER A WITH ACUTE).

You can normalize strings with Python using the `unicodedata` module:

    >>> a = 'á'
    >>> len(a)
    2
    >>> import unicodedata
    >>> unicodedata.normalize("NFKC", a)
    'á'
    >>> len(_)
    1

The below table lists characters that normalize to other characters, but be
aware that other combinations of characters such as combining accents may not
be listed below but may still normalize to a character listed below.

Characters that are not on this list cannot be used in variable names. The
valid characters are primarily characters that are "like" alphanumeric +
underscore. It doesn't include things like mathematical symbols (except for
Greek letters because those are letters) or emoji.

    >>> ∫x = 1
      File "<stdin>", line 1
        ∫x = 1
         ^
    SyntaxError: invalid character in identifier
    >>> 💩 = 'Python 2'
      File "<stdin>", line 1
        💩 = 'Python 2'
        ^
    SyntaxError: invalid character in identifier

## Should I use these characters in my Python code?

[PEP 8](https://www.python.org/dev/peps/pep-0008/#source-file-encoding)
specifies:

> For Python 3.0 and beyond, the following policy is prescribed for the standard library (see PEP 3131): All identifiers in the Python standard library MUST use ASCII-only identifiers, and SHOULD use English words wherever feasible (in many cases, abbreviations and technical terms are used which aren't English). In addition, string literals and comments must also be in ASCII. The only exceptions are (a) test cases testing the non-ASCII features, and (b) names of authors. Authors whose names are not based on the Latin alphabet (latin-1, ISO/IEC 8859-1 character set) MUST provide a transliteration of their names in this character set.
>
> Open source projects with a global audience are encouraged to adopt a similar policy.

The key issue is that for many people, typing non-ASCII characters is not
easy. It is usually only possible by copying and pasting. If you are 100%
certain that your code will only be read and run by people who speak the same
language as you and are able to easily type characters you are using, it is
probably fine to do so. One possibility would be to provide aliases for names
that are part of a public API, so that users can choose which to use (for
example, `pi = π`).

If you do decide to use non-ASCII characters for variable names, be aware of
the normalization issues described above. It is advisable to always insert
variable names in source files using their normalized form.

# Unicode character list

There are two types of valid characters, "start" and "continue" characters.
"Start" characters can be anywhere in an identifier. They correspond to
"letters and underscore" in the old ASCII-only identifiers. "Continue"
characters cannot be the first character in an identifier. They correspond to
"numbers" in the old ASCII-only way. A valid identifier can be any "start"
character followed by any number of "start" or "continue" characters.

The pages can be viewed here:

**WARNING: the pages are quite large and may cause issues in some browsers.**

[**Start Characters**](start-characters.html) (<a href="start-characters.md">raw markdown</a>)

[**Continue Characters**](continue-characters.html) (<a href="continue-characters.md">raw markdown</a>)

