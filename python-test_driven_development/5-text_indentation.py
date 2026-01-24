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
    
    # Process text
    result = []
    i = 0
    n = len(text)
    
    # Skip leading spaces
    while i < n and text[i] == ' ':
        i += 1
    
    while i < n:
        # Start building current segment
        segment = ""
        
        # Collect characters until special char or end
        while i < n and text[i] not in ".?:":
            segment += text[i]
            i += 1
        
        # If we found special character, add it
        if i < n and text[i] in ".?:":
            segment += text[i]
            i += 1
            
            # Skip spaces after special character
            while i < n and text[i] == ' ':
                i += 1
        
        # Strip trailing spaces from segment
        if segment:
            result.append(segment.rstrip())
    
    # Join with double newlines and print
    print("\n\n".join(result), end='')
