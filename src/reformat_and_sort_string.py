"""
Problem: "Reformat and Sort String"
Problem Description: You are given a string s containing words separated by spaces. Your task is to:

1. Remove any leading or trailing spaces.
2. Reverse the order of the words in the string.
3. Capitalize the first letter of each word.
4. Sort the words alphabetically in the resulting string.
Example:

Input: "  chErry aPPLE baNaNA  "
Output: "Brown Fox Quick The"
"""

def reformat_and_sort(s: str) -> str:
    # Step 1: Strip leading and trailing spaces
    s = s.strip()
    
    # Step 2: Split the string into a list of words
    words = s.split()

    # Step 3: Reverse the order of the words
    words.reverse()

    # Step 4: Capitalize the first letter of each word
    words = [word.capitalize() for word in words]

    # Step 5: Sort the words alphabetically
    words.sort()

    # Step 6: Join the words back into a string with spaces in between
    return " ".join(words)
