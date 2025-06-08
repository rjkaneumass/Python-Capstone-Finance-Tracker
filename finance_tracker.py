#Project: Personal Finance Tracker
#Step 1: Set up the project
print("Welcome to the Personal Finance Tracker!")
global expenses_dictionary
expenses_dictionary = {}
#Step 2: Add Expenses
def add_expense():
    while True:
        try:
            expense_description = input("Enter expense description (or exit if done): ")
            if expense_description == "":
                raise ValueError("Expense description cannot be empty.")
            if expense_description.lower() == "exit":
                break
            expense_category = input("Enter expense category: ")
            if expense_category == "":
                raise ValueError("Expense category cannot be empty.")
            expense_amount = float(input("Enter expense amount: "))
            if expense_amount < 0:
                raise ValueError("Expense amount cannot be negative.")
            if expense_category in expenses_dictionary:
                expenses_dictionary[expense_category].append((expense_description, expense_amount))
            else:
                expenses_dictionary[expense_category] = [(expense_description, expense_amount)]
        except ValueError:
            print("Invalid input. Please try again.")
    print("Expenses added successfully!")
#Step 3: View All Expenses
def view_expenses():
    for category, expenses in expenses_dictionary.items():
        print("Category:", category)
        for description, amount in expenses:
            print("- ", description, ": $", amount)
#Step 4: View Summary by Category
def view_summary():
    print("Summary: ")
    for category, expenses in expenses_dictionary.items():
        sum = 0
        for description, amount in expenses:
            sum += amount
        print("", category, ": $", sum)
#Step 6: Main Menu Function
def main_menu():
    while True:
        print("What would you like to do?")
        print("1. Add Expenses")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Exit")
        try:
            user_choice = int(input("Choose an option: "))
            if user_choice == 1:
                add_expense()
            elif user_choice == 2:
                view_expenses()
            elif user_choice == 3:
                view_summary()
            elif user_choice == 4:
                print("Thank you for using the Personal Finance Tracker!")
                break
            else:
                raise ValueError("Invalid option. Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please try again.")
    exit()
main_menu()
