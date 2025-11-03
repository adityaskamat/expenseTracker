import csv
from datetime import datetime

# File to store expenses
FILE_NAME = "expenses.csv"

# Create file if it doesn't exist
try:
    open(FILE_NAME, "x").close()
except FileExistsError:
    pass

def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (e.g., Food, Travel, Rent): ").capitalize()
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    print("✅ Expense added successfully!")

def view_expenses():
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            total = 0
            print("\n--- All Expenses ---")
            for row in reader:
                if row:
                    print(f"{row[0]} | {row[1]} | {row[2]} | ${row[3]}")
                    total += float(row[3])
            print(f"\nTotal Spent: ${total:.2f}\n")
    except FileNotFoundError:
        print("No expenses found.")

def summary_by_category():
    totals = {}
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    category = row[1]
                    amount = float(row[3])
                    totals[category] = totals.get(category, 0) + amount
        print("\n--- Spending by Category ---")
        for category, total in totals.items():
            print(f"{category}: ${total:.2f}")
    except FileNotFoundError:
        print("No expenses found.")

def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Summary by Category")
        print("4. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summary_by_category()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
