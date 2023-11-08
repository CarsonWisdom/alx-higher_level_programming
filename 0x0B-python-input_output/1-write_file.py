#!/usr/bin/python3
"""Module containing the function write_file"""


def write_file(filename="", text=""):
    """Writes a string to a text(file text) file (UTF8) and returns the number
    of characters written.

    Args:
        filename (str, optional): name of file. Defaults to "".
        text (str, optional): string of text to write to file. Defaults to "".

    Returns:
        int: number of characters written to file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        """This method returns da namber of characters written to a file."""
        return f.write(text)
