#!/usr/bin/python3

def text_indentation(text):
    """
    Prints a text with two new lines after each of these characters: `.`, `?`, and `:`.

    Parameters:
        text (str): The string to print, which must be of type string.

    Raises:
        TypeError: If `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] in ['.', '?', ':']:
            print(text[i], end="\n\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            print(text[i], end="")
            i += 1
