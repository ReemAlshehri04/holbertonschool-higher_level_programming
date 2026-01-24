#!/usr/bin/python3
"""
Module for text indentation
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    
    Args:
        text: string to be formatted
    
    Raises:
        TypeError: if text is not a string
    """
    # Validate input
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # If empty string, print newline and return
    if text == "":
        print()
        return
    
    # Clean the text - remove leading/trailing spaces
    text = text.strip()
    
    # Initialize variables
    i = 0
    length = len(text)
    new_text = ""
    
    # Build new text with proper formatting
    while i < length:
        new_text += text[i]
        
        if text[i] in ".?:":
            new_text += "\n\n"
            i += 1
            # Skip spaces
            while i < length and text[i] == ' ':
                i += 1
            continue
        
        i += 1
    
    # Clean each line (remove trailing spaces)
    lines = [line.rstrip() for line in new_text.split('\n')]
    
    # Print with proper formatting
    for i, line in enumerate(lines):
        if line:  # Only print non-empty lines
            print(line, end='' if i == len(lines) - 1 else '\n')
