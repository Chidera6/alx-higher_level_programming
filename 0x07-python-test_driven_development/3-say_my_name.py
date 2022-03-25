#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """Prints a string.
    Validates string inputs, the display
    the full name"""

    if first_name != str:
        raise TypeError("first_name must be a string")
    elif last_name != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
