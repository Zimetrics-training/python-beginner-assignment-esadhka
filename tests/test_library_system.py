import datetime
import pytest
import sys
sys.path.insert(0, './src')  # Add the 'src' directory to the path
from library_system import Book  # Modify this import based on your file structure

def test_book_functions():
    # Test 1: Book Creation and Info
    book = Book("1984", "George Orwell", 1949)
    assert book.get_info() == "1984 by George Orwell (Published: 1949) - available"
    assert not book.is_checked_out()

    # Test 2: Checkout and Checkin
    book.checkout()
    assert book.is_checked_out()
    
    with pytest.raises(Exception):  # assuming you raise an exception if the book is already checked out
        book.checkout()
    
    book.checkin()
    assert not book.is_checked_out()

    # Test 3: Book Age
    assert Book.book_age(2000) == datetime.datetime.now().year-2000
