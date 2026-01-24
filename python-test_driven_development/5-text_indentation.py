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
    
    # Initialize result string
    result = ""
    i = 0
    length = len(text)
    
    # Process text character by character
    while i < length:
        # Add current character to result
        result += text[i]
        
        # Check for special characters
        if text[i] in ".?:":
            # Add two new lines
            result += "\n\n"
            
            # Skip any spaces immediately after special character
            i += 1
            while i < length and text[i] == ' ':
                i += 1
            continue
        
        i += 1
    
    # Print each line after stripping leading/trailing spaces
    lines = result.split('\n')
    for i, line in enumerate(lines):
        # Remove leading and trailing spaces (only spaces, not other whitespace)
        cleaned_line = line.strip(' ')
        if cleaned_line or i == len(lines) - 1:
            print(cleaned_line, end='' if i == len(lines) - 1 else '\n')
