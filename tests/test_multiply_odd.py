import pytest
import sys
#sys.path.insert(0, './src')  # Add the 'src' directory to the path
sys.path.insert(0, '../src')  # Add the 'src' directory relative to 'tests' folder
from multiply_odd import multiply_odd_numbers

def test_multiply_odd_numbers():
    # Test case 1: Normal case with mixed odd and even numbers

    assert multiply_odd_numbers([1, 2, 3, 4, 5]) == 15  # Odd numbers: 1, 3, 5 -> Product: 1*3*5 = 15

    # Test case 2: Case with only even numbers (no odd numbers)
    assert multiply_odd_numbers([2, 4, 6, 8]) == 1  # No odd numbers

    # Test case 3: Case with only odd numbers
    assert multiply_odd_numbers([7, 9, 11]) == 693  # Odd numbers: 7, 9, 11 -> Product: 7*9*11 = 693
    
    # Test case 4: Case with an empty list
    assert multiply_odd_numbers([]) == 1  # No odd numbers
    
    # Test case 5: Case with single odd number
    assert multiply_odd_numbers([5]) == 5  # Odd number: 5 -> Product: 5
    
    # Test case 6: Case with negative odd numbers
    assert multiply_odd_numbers([-1, -3, -5]) == -15  # Odd numbers: -1, -3, -5 -> Product: -1*-3*-5 = -15
    
    # Test case 7: Case where no odd numbers exist
    assert multiply_odd_numbers([2, 4, 6, 8, 10]) == 1  # No odd numbers
    
    # Test case 8: Case with zero and positive odd numbers
    assert multiply_odd_numbers([0, 3, 7]) == 21  # Odd numbers: 3, 7 -> Product: 3*7 = 21
