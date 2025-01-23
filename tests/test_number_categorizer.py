import pytest
import sys
sys.path.insert(0, './src')  # Add the 'src' directory to the path
from number_categorizer import categorize_numbers, is_prime, is_perfect

def test_categorize_numbers():
    # Test case 1: Mixed numbers
    nums = [6, -3, 15, 28, 13, 0, 1, 4]
    expected = [
        "positive, even, perfect",
        "negative, odd",
        "positive, odd",
        "positive, even, perfect",
        "positive, odd, prime",
        "zero, even",
        "positive, odd",
        "positive, even"
    ]
    assert categorize_numbers(nums) == expected

    # Test case 2: Edge case - empty list
    nums = []
    expected = []
    assert categorize_numbers(nums) == expected

    # Test case 3: Edge case - only negative numbers
    nums = [-1, -2, -3, -4, -5]
    expected = [
        "negative, odd",
        "negative, even",
        "negative, odd",
        "negative, even",
        "negative, odd"
    ]
    assert categorize_numbers(nums) == expected

    # Test case 4: Prime numbers
    nums = [2, 3, 5, 7, 11]
    expected = [
        "positive, even, prime",
        "positive, odd, prime",
        "positive, odd, prime",
        "positive, odd, prime",
        "positive, odd, prime"
    ]
    assert categorize_numbers(nums) == expected

    # Test case 5: Perfect numbers
    nums = [6, 28, 496]
    expected = [
        "positive, even, perfect",
        "positive, even, perfect",
        "positive, even, perfect"
    ]
    assert categorize_numbers(nums) == expected
