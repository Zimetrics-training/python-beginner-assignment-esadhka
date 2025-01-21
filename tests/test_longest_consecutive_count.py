import pytest
import sys
sys.path.insert(0, './src')  # Add the 'src' directory to the path
from longest_consecutive_count import longest_consecutive  # Replace with actual module name

def test_longest_consecutive():
    # Test with some sample inputs
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([0, 1, 2, 3, 4, 5]) == 6
    assert longest_consecutive([10, 9, 2, 1, 3, 4, 7, 8]) == 4
    assert longest_consecutive([1, 2, 0, 1]) == 2
    assert longest_consecutive([3, 10, 2, 1]) == 3
    assert longest_consecutive([100, 4, 200, 1, 3, 2, 5]) == 5
    assert longest_consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9

if __name__ == "__main__":
    pytest.main()
