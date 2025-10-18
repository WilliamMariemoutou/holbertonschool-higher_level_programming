#!/usr/bin/python3

"""Prints a text with one new line after each of the characters `.`, `?`, and `:`."""

def text_indentation(text):
    """
    Prints a text with one new line after each of these characters: `.`, `?`, and `:`.

    Parameters:
        text (str): The string to print, which must be of type string.

    Raises:
        TypeError: If `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if any(c in text for c in ['.', '?', ':']):
        i = 0
        while i < len(text):
            if text[i] in ['.', '?', ':']:
                print(text[i], end="\n")
                i += 1

                while i < len(text) and text[i] == ' ':
                    i += 1
            else:
                print(text[i], end="")
                i += 1
    else:
        print(text)

