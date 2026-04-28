# R-2.1 Give three examples of life-critical software applications.

# - Aircraft flight control systems, Medical decices(insulin pumps), Automotive safety systems

# R-2.2 Give an example of a software application in which adaptability can mean
# the difference between a prolonged lifetime of sales and bankruptcy.

# - Smartphone operating system (android in contrast to microsoft)

# R-2.4 Write a Python class, Flower, that has three instance variables of type str,
# int, and float, that respectively represent the name of the flower, its number
# of petals, and its price. Your class must include a constructor method
# that initializes each variable to an appropriate value, and your class should
# include methods for setting the value of each type, and retrieving the value
# of each type.


class Flower:
    """
    A class representing a flower with name, price and number of petals
    """

    def __init__(self, name: str, petals: int, price: float):
        """
        Constructor to initialize the flower with name, number of petals and price
        """
        self._name = name
        self._petals = petals
        self._price = price

    # Setting
    def set_name(self, name: str):
        self._name = name

    def set_petals(self, petals: int):
        self._petals = petals

    def set_price(self, price: float):
        self._price = price

    # Getting
    def get_name(self):
        return self._name

    def get_petals(self):
        return self._petals

    def get_price(self):
        return self._price


# Creating a Flower object
rose = Flower("Rose", 25, 2.99)

rose.set_name("Red Rose")
rose.set_petals(30)
rose.set_price(3.49)
print(rose.get_name())
print(rose.get_petals())
print(rose.get_price())


# Credit Card class
class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance.

        The initial balance is zero.

        customer the name of the customer (e.g., John Bowman )
        bank the name of the bank (e.g., California Savings )
        acnt the acount identifier (e.g., 5391 0375 9387 5309 )
        limit credit limit (measured in dollars)
        """
        self.customer = customer
        self.bank = bank
        self.account = acnt
        self.limit = limit
        self.balance = 0

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank s name."""
        return self.bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; False if charge was denied.
        """
        if price + self.balance > self.limit:  # if charge would exceed limit,
            return False  # cannot accept charge
        else:
            self.balance += price
        return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self.balance -= amount


# R-2.5 Use the techniques of Section 1.7 to revise the charge and make payment
# methods of the CreditCard class to ensure that the caller sends a number
# as a parameter.


def charge(self, price):
    """Charge given price to the card, assuming sufficient credit limit.

    Return True if charge was processed; False if charge was denied.
    """
    if not isinstance(price, (int, float)):
        raise TypeError("price must be a numbers")
    price = float(price)

    if price + self._balance > self.limit:  # if charge would exceed limit,
        return False  # cannot accept charge
    else:
        self._balance += price
    return True


def make_payment(self, amount):
    """Process customer payment that reduces balance."""
    if not isinstance(amount, (int, float)):
        raise TypeError("Charge must be in numbers")

    amount = float(amount)

    if amount <= 0:
        raise ValueError("Amount must be positive")
    else:
        self.balance -= amount


# R-2.6 If the parameter to the make payment method of the CreditCard class
# were a negative number, that would have the effect of raising the balance
# on the account. Revise the implementation so that it raises a ValueError if
# a negative value is sent.


def make_payment(self, amount):
    """Process customer payment that reduces balance."""
    if not isinstance(amount, (int, float)):
        raise TypeError("Charge must be in numbers")

    amount = float(amount)

    if amount <= 0:
        raise ValueError("Amount must be positive")
    else:
        self.balance -= amount


# R-2.7 The CreditCard class of Section 2.3 initializes the balance of a new account
# to zero. Modify that class so that a new account can be given a
# nonzero balance using an optional fifth parameter to the constructor. The
# four-parameter constructor syntax should continue to produce an account
# with zero balance.


class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit, balance=0):
        """Create a new credit card instance.

        The initial balance is zero.

        customer the name of the customer (e.g., John Bowman )
        bank the name of the bank (e.g., California Savings )
        acnt the acount identifier (e.g., 5391 0375 9387 5309 )
        limit credit limit (measured in dollars)
        """
        self.customer = customer
        self.bank = bank
        self.account = acnt
        self.limit = limit
        self.balance = float(balance)


# R-2.8 Modify the declaration of the first for loop in the CreditCard tests, from
# Code Fragment 2.3, so that it will eventually cause exactly one of the three
# credit cards to go over its credit limit. Which credit card is it?

if __name__ == "__main__":
    wallet = []
    wallet.append(
        CreditCard("John Bowman", "California Savings", "5391 0375 9387 5309", 2500)
    )
    wallet.append(
        CreditCard("John Bowman", "California Federal", "3485 0399 3395 1954", 3500)
    )
    wallet.append(
        CreditCard("John Bowman", "California Finance", "5391 0375 9387 5309", 5000)
    )

    # Modified for loop as requested in R-2.8
    for val in range(1, 59):
        wallet[0].charge(val)  # charges: 1, 2, 3, ..., 16
        wallet[1].charge(2 * val)  # charges: 2, 4, 6, ..., 32
        wallet[2].charge(3 * val)  # charges: 3, 6, 9, ..., 48

# Wallet 3 is the first to exceed the limit
