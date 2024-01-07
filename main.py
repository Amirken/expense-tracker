#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 

"""

from expense import Expense
import calendar
import datetime
import csv
from colorama import Back

BUDGET = 2000 # CONSTANT variable

def main():
    """
    Main function to run the Expense Tracker application.
    """
    print("🎯 Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    
    expense = get_user_expense()
    
    print(f"Expense created at: {expense._date_created}")
    
    expense.approve()
    if expense.is_expense_approved():
        print("Expense is approved!")
    else:
        print("Expense is not approved yet.")
    
    days_since_creation = expense._calculate_days_since_creation()
    print(f"Days since creation: {days_since_creation}")
    
    # Read file and summarize expenses.
    save_expense_to_file(expense, expense_file_path)
    summarize_expenses(expense_file_path, BUDGET)
      

def get_user_expense():
    """
    Get user input for expense.

    Returns:
        Expense: The created Expense object.
    """
    print("🎯 Getting User Expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))

    expense_categories = {
        1: "🍔 Food",
        2: "🏠 Home & Utilities",
        3: "🚘 Transportation",
        4: "🩺 Health & Personal Care",
        5: "🎉 Shopping and Entertainment",
        6: "💼 Work",
        7: "🛩️ Travel",
        8: "💸 Charity",
        9: "📚 Education",
        10: "✨ Misc",
    }

    while True:
        print("Select a category: ")
        for key, category_name in expense_categories.items():
            print(f"  {key}. {category_name}")

        value_range = f"[{len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: "))

        if selected_index in expense_categories:
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount
            )
            return new_expense
        else:
            print("Invalid category. Please try again!")

def save_expense_to_file(expense, expense_file_path):
    """
    Save the expense to a CSV file, keeping track of creation dates and modifications.

    Args:
        expense (Expense): The Expense object to be saved.
        expense_file_path (str): The file path to save the expenses to.
    """
    print(f"🎯 Saving User Expense: {expense} to {expense_file_path}")
    expenses = []
    headers = ["Expense name", "Amount in $", "Category", "Date of Creation"] 

    # Read existing expenses from the file
    try:
        with open(expense_file_path, "r") as f:
            reader = csv.reader(f)
            headers = next(reader)  # Read the header row
            for line in reader:
                expense_name, expense_amount, expense_category, creation_date = line[0], line[1], line[2], line[3]
                line_expense = Expense(
                    name=expense_name, amount=float(expense_amount), category=expense_category
                )
                # Assign the creation date to the existing expenses
                line_expense._date_created = datetime.datetime.strptime(creation_date, "%Y-%m-%d %H:%M:%S.%f")
                expenses.append(line_expense)
    except FileNotFoundError:
        pass  # If the file doesn't exist yet, proceed with an empty list of expenses
                
    # Check if the expense is already in the list
    if expense in expenses:
        # If it is, find the index and add the amounts together
        index = expenses.index(expense)
        expenses[index] += expense
    else:
        # If it's not, add the new expense to the list
        expenses.append(expense)

    # Write the updated list of expenses to the file
    with open(expense_file_path, "w", newline='') as f:  # Use newline='' to avoid extra newlines in CSV
        csv_writer = csv.writer(f)
        # Include the creation date in the header row
        csv_writer.writerow(headers)  
        for expense in expenses:
            # Write each expense along with the creation date to the CSV file
            csv_writer.writerow([expense.name, expense.amount, expense.category, expense._date_created])

        
            

def summarize_expenses(expense_file_path, BUDGET):
    """
    Summarize user expenses.

    Args:
        expense_file_path (str): The file path to read expenses from.
        budget (float): The budget for expenses.
    """
    print("🎯 Summarizing User Expense")
    expenses = []

    try:
        with open(expense_file_path, "r") as f:
            next(f)
            lines = f.readlines()
            for line in lines:
                expense_name, expense_amount, expense_category, expense_date_created  = line.strip().split(",")
                line_expense = Expense(
                    name=expense_name, amount=float(expense_amount), category=expense_category
                )
                line_expense._date_created = datetime.datetime.strptime(expense_date_created, "%Y-%m-%d %H:%M:%S.%f")
                expenses.append(line_expense)

    except FileNotFoundError:
        print(f"File '{expense_file_path}' not found. No expenses to summarize.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    else:
        amount_by_category = {}
        for exp in expenses:
            key = exp.category
            if key in amount_by_category:
                amount_by_category[key] += exp.amount
            else:
                amount_by_category[key] = exp.amount
     

        print("Expenses By Category 📈:")
        for key, amount in amount_by_category.items():
            print(f"  {key}: ${amount:,.2f}")
        
    unique_expenses = []
    for exp in expenses:
        if exp not in unique_expenses:
            unique_expenses.append(exp)
        else:
            index = unique_expenses.index(exp)
            unique_expenses[index] += exp
    total_spent = sum([x.amount for x in expenses])
    print(f"💵 Total Spent: ${total_spent:,.2f}")

    remaining_budget = BUDGET - total_spent
    if remaining_budget < 0:
        print("❌ Oops..You're run out of money")
    else:
        print(f"✅ Budget Remaining ${remaining_budget:,.2f}")
        now = datetime.datetime.now()
        days_in_month = calendar.monthrange(now.year, now.month)[1]
        remaining_days = days_in_month - now.day

        daily_budget = remaining_budget / remaining_days
        print(f"👉{Back.GREEN} Budget Per Day: ${daily_budget:,.2f}")

if __name__ == "__main__":
    main()


