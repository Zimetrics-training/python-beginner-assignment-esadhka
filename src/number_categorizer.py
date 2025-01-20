"""
Problem:
Task: Write a program that processes a list of integers and categorizes them into the following groups:

1. Positive: Numbers greater than 0.
2. Negative: Numbers less than 0.
3. Zero: Numbers equal to 0.
4. Even: Numbers divisible by 2.
5. Odd: Numbers not divisible by 2.
6. Prime: Numbers greater than 1 and divisible only by 1 and themselves.
7. Perfect: Numbers that are equal to the sum of their divisors (excluding themselves).

For each number in the list, create a category that consists of a combination of these conditions. 
The format should be a list of strings where each string is a combination of categories, 
separated by commas (e.g., "positive, even", "negative, odd", "prime", "zero, even" etc.).

Write a function categorize_numbers(nums: List[int]) -> List[str] that implements this transformation.

Additionally, create helper functions:
1. is_prime(num: int) -> bool: returns True if the number is prime.
2. is_perfect(num: int) -> bool: returns True if the number is perfect.
"""
from typing import List

def is_prime(num: int) -> bool:
    # Your code to check if a number is prime
    pass

def is_perfect(num: int) -> bool:
    # Your code to check if a number is perfect
    pass

def categorize_numbers(nums: List[int]) -> List[str]:
    result = []
    for num in nums:
        # Your code to categorize each number based on the conditions
        pass
    
    return result
