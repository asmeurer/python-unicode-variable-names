# Python Unicode Variable Names

http://www.asmeurer.com/python-unicode-variable-names/

A page listing all the Unicode characters that are valid in Python variable names

To generate the page, use

    python3 generate.py

This will generate the files `docs/start-characters.md` and
`docs/continue-characters.md`. The files should be committed to the repo.
Don't edit these files directly. To update their contents, update the script
`generate.py`.

Note that different versions of Python are build with different versions of
the Unicode standard, and thus will produce different lists of characters.
This can differ even between minor versions. You should always generate this
page with the latest released version of Python.

GitHub pages will automatically convert the generated Markdown to HTML, which
can be viewed at http://www.asmeurer.com/python-unicode-variable-names/.

# Contributing

Contributions are welcome. Please open a PR.

# License

MIT
