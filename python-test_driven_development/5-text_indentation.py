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
    
    # Initialize variables
    i = 0
    length = len(text)
    
    # Process text character by character
    while i < length:
        # Print current character
        print(text[i], end='')
        
        # Check for special characters
        if text[i] in ".?:":
            # Print two new lines
            print("\n")
            
            # Skip any spaces immediately after the special character
            i += 1
            while i < length and text[i] == ' ':
                i += 1
            continue
        
        i += 1
    
    # Print a newline at the end
    print()
