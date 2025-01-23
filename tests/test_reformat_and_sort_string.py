import pytest
import sys
sys.path.insert(0, './src')  # Add the 'src' directory to the path
from reformat_and_sort_string import reformat_and_sort

def test_reformat_and_sort():
    # Test case 1: Regular string with spaces and multiple words
    assert reformat_and_sort("  worLD heLLO xyZ hI  ") == "Hello Hi World Xyz"
    
    # Test case 2: String with no spaces
    assert reformat_and_sort("hello") == "Hello"
    
    # Test case 3: String with single word and extra spaces
    assert reformat_and_sort("   python  ") == "Python"
    
    # Test case 4: String with multiple words and mixed case
    assert reformat_and_sort("  aPPLE baNaNA  chErry") == "Apple Banana Cherry"
    
    # Test case 5: Empty string
    assert reformat_and_sort("") == ""
    
    # Test case 6: String with leading, trailing spaces, and mixed case words
    assert reformat_and_sort("   gOOd mOrninG fRiEnD   ") == "Friend Good Morning"
    
    # Test case 7: String with only one word
    assert reformat_and_sort("   onlyoneword   ") == "Onlyoneword"
    
    # Test case 8: String with multiple spaces between words
    assert reformat_and_sort(" hello     world   ") == "Hello World"
    
    # Test case 9: String with numbers
    assert reformat_and_sort(" 123 456 abc") == "123 456 Abc"
    
    # Test case 10: Performance test (long string)
    long_string = "  ".join(["word"] * 10000)
    assert reformat_and_sort(long_string) == ("Word " * 10000).strip()
