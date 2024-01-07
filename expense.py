#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from datetime import datetime

class Expense:
    """
    Represents an expense with name, category, and amount.

    Attributes:
        name (str): The name of the expense.
        category (str): The category of the expense.
        amount (float): The amount of the expense.
        _private_attribute (str): A private attribute for internal use.
    """

    def __init__(self, name, category, amount, creation_date=None) -> None:
        """
        Initializes a new Expense object.

        Args:
            name (str): The name of the expense.
            category (str): The category of the expense.
            amount (float): The amount of the expense.
            creation date (datetime): The creation date of the expense.
        """
        self.name = name
        self.category = category
        self.amount = amount
        self.is_approved = False
        self._date_created = datetime.now()
        
    
    def __repr__(self):
        """
        Returns a string representation of the Expense object.
        """
        return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f}, {self._date_created.strftime('%Y-%m-%d %H:%M:%S.%f')}>"
    
    def __eq__(self, other):
        """
        Compare two instances to see if they have the same category and name.
        """
        return self.name == other.name and self.category == other.category

    def __add__(self, other):
        """
        Add two instances together, combining their amounts if they have the same category and name.
        """
        if self == other:
            return Expense(name=self.name, category=self.category, amount=self.amount + other.amount)
        else:
            raise ValueError("Expenses must have the same category and name to be added")

    def approve(self):
        """Approve the expense."""
        self.is_approved = True
    
    def is_expense_approved(self):
        """Check if the expense is approved."""
        return self.is_approved
    
    def _calculate_days_since_creation(self, current_date=None):
        """Calculate the number of days since the expense was created."""
        if current_date is None:
            current_date = datetime.now()

        days_since_creation = (current_date - self._date_created).days

        return days_since_creation



   
   



