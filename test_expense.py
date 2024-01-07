#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

import unittest
from expense import Expense

class TestExpenseClassMethods(unittest.TestCase):
    """Test methods of the Expense class."""

    def test_approve_method(self):
        """Test the approve method of the Expense class."""
        expense = Expense(name="Test Expense", category="Test Category", amount=100.0)
        self.assertFalse(expense.is_expense_approved())  # Initial state

        # Call the approve method
        expense.approve()

        # Assert that the expense is now approved
        self.assertTrue(expense.is_expense_approved())

    def test_add_method(self):
        """Test the __add__ method of the Expense class."""
        expense1 = Expense(name="Expense 1", category="Category", amount=50.0)
        expense2 = Expense(name="Expense 1", category="Category", amount=30.0)

        # Call the __add__ method
        result = expense1 + expense2

        # Assert that the result is a new Expense object with the combined amount
        self.assertIsInstance(result, Expense)
        self.assertEqual(result.amount, 80.0)

if __name__ == '__main__':
    unittest.main()

