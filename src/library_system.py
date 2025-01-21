"""
Problem Statement: Library System
You are tasked with creating a Book class to represent a book in a library system. 
The Book class should have the following methods:

1. Initialization: The class should be initialized with title, author, year_of_publication, and status. 
The status indicates whether the book is checked out or available. Default it to "available".

2. Methods:
    checkout(): Marks the book as checked out. If the book is already checked out, 
                it should raise an exception.
    checkin(): Marks the book as available. If the book is already available, 
                it should raise an exception.
    get_info(): Returns a string containing the book's title, author, year of publication, 
                and its current status (either "checked out" or "available").
    is_checked_out(): Returns True if the book is checked out, otherwise False.

3. Static Method:
    book_age(year: int): A static method that returns the age of the book based on the current year. 
                         It takes the year of publication as a parameter.
"""
import datetime

class Book:
    def __init__(self, title: str, author: str, year_of_publication: int, status: str = "available"):
        # Initialize the book with title, author, year_of_publication, and status
        pass

    def checkout(self) -> None:
        # Mark the book as checked out, raise an exception if already checked out
        pass

    def checkin(self) -> None:
        # Mark the book as available, raise an exception if already available
        pass

    def get_info(self) -> str:
        # Return the book's title, author, year_of_publication, and status as a formatted string
        pass

    def is_checked_out(self) -> bool:
        # Return True if the book is checked out, else False
        pass

    @staticmethod
    def book_age(year_of_publication: int) -> int:
        # Return the age of the book based on the current year
        pass
