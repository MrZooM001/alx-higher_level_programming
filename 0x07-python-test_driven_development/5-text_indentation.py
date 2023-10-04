#!/usr/bin/python3
"""Module to print a text with 2 new lines

This supplies one function, print_square(). For example:
>>> text_indentation("Question? A: The answer. Done")
Question?
<BLANKLINE>
A:
<BLANKLINE>
The answer.
<BLANKLINE>
Done
"""


def text_indentation(text):
    """Function that  prints a text with 2 new lines
    after each of these characters . ? :

    Args:
        text (str): text that contains characters ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if (text[i] == '\n' or text[i] == '.' or
                text[i] == '?' or text[i] == ':'):
            if text[i] in ".?:":
                print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
