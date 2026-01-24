#!/usr/bin/python3
"""
Module for printing name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>"
    
    Args:
        first_name: string representing first name
        last_name: string representing last name (default is empty string)
    
    Raises:
        TypeError: if first_name or last_name are not strings
    """
    # Validate first_name
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    # Validate last_name
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    # Print with space even if last_name is empty
    # This will print "My name is Bob " (with space at the end)
    print("My name is {} {}".format(first_name, last_name))
