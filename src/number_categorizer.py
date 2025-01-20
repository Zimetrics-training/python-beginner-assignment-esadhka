"""
Problem:
Task: Write a program that processes a list of integers and categorizes them into the following groups:

1. Positive: Numbers greater than 0.
2. Negative: Numbers less than 0.
3. Zero: Numbers equal to 0.
4. Even: Numbers divisible by 2.
5. Odd: Numbers not divisible by 2.
6. Prime: Numbers greater than 1 and divisible only by 1 and themselves.
7. Perfect: Numbers that are equal to the sum of their divisors (excluding themselves). Perfect numbers are greater than zero.

For each number in the list, create a category that consists of a combination of these conditions. 
The format should be a list of strings where each string is a combination of categories, 
separated by commas (e.g., "positive, even, zero", "negative, odd", "prime", etc.).

Write a function categorize_numbers(nums: List[int]) -> List[str] that implements this transformation.

Additionally, create helper functions:
1. is_prime(num: int) -> bool: returns True if the number is prime.
2. is_perfect(num: int) -> bool: returns True if the number is perfect.
"""
from typing import List

def is_prime(num: int) -> bool:
    # Your code to check if a number is prime
    count = 0
    if num>1:
        for i in range(1, num+1, 1):
            if num%i == 0:
                count = count + 1
        if count == 2:
            return True
    return False

def is_perfect(num: int) -> bool:
    # Your code to check if a number is perfect
    if num>0:
        divisor_list = []
        for i in range(1, num, 1):
            if num%i == 0:
                divisor_list.append(i)
        if num ==sum(divisor_list):
            return True
    return False


def categorize_numbers(nums: List[int]) -> List[str]:
    result = []
    for num in nums:
        str_new = []
        # Your code to categorize each number based on the conditions
        if num>0:
            str_new.append("positive")
        if num<0:
            str_new.append("negative")
        if num==0:
            str_new.append("zero")
        if num%2==0:
            str_new.append("even")
        if num%2==1:
            str_new.append("odd")
        if is_prime(num):
            str_new.append("prime")
        if is_perfect(num):
            str_new.append("perfect")
        result1 = ', '.join(str_new)
        result.append(result1)
    return result


print(categorize_numbers(nums = [6, -3, 15, 28, 13, 0, 1, 4, 41]))
