#!/usr/bin/python3
def text_indentation(text):
    """prints a text with two new line"""
    if type(text) != str:
        raise TypeError("text must be a string")
    y = ['.','?',':']
    for x in text:
        print(x,end='')
        if x in y:
        print("\n\n",end='')
