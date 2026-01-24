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
    result = ""
    i = 0
    length = len(text)
    
    # Process the text character by character
    while i < length:
        result += text[i]
        
        # Check for special characters
        if text[i] in ".?:":
            # Add two new lines
            result += "\n\n"
            
            # Skip any spaces immediately after the special character
            i += 1
            while i < length and text[i] == ' ':
                i += 1
            continue
        
        i += 1
    
    # Print the result without trailing spaces for each line
    lines = result.split('\n')
    for line in lines:
        print(line.strip())
