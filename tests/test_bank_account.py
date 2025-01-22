# test_bank_account.py
import pytest
import sys
sys.path.insert(0, './src')  # Add the 'src' directory to the path
from bank_account import BankAccount, InsufficientFundsError

def test_bank_account():
    # Create two bank accounts
    account1 = BankAccount("Alice", 1000.0)
    account2 = BankAccount("Bob", 500.0)

    # Test deposit method
    account1.deposit(500)
    assert account1.get_balance() == 1500.0
    with pytest.raises(ValueError):
        account1.deposit(-100)

    # Test withdraw method
    account1.withdraw(200)
    assert account1.get_balance() == 1300.0
    with pytest.raises(ValueError):
        account1.withdraw(-50)
    with pytest.raises(InsufficientFundsError):
        account1.withdraw(2000)

    # Test transfer method
    account1.transfer(account2, 300)
    assert account1.get_balance() == 1000.0
    assert account2.get_balance() == 800.0
    with pytest.raises(ValueError):
        account1.transfer(account2, -100)
    with pytest.raises(InsufficientFundsError):
        account1.transfer(account2, 2000)

    # Test __str__ method
    assert str(account1) == "AccountHolder: Alice, Balance: 1000.0"
