#!/usr/bin/python3

"""Prints a text with two new lines after each characters."""


def text_indentation(text):
    """

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
            """checks if we see the required symbols"""
            print(text[i], end="\n\n")
            i += 1
            """prints the character with a newline"""
            while i < len(text) and text[i] == ' ':
                i += 1
                """ignore spaces afther the symbol"""
        else:
            print(text[i], end="")
            i += 1
            """prints current character"""
