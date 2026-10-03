expenses = []
def add_expense():
    description = input("Enter expense description: ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    
    category = input("Enter Category: ")
    
    expense = {
        "description": description,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print("Expense added successfully.")


def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n======== EXPENSES ========")

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['description']} - "
            f"Rs. {expense['amount']:.2f} - "
            f"{expense['category']}"
        )


def show_total():
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Expense: Rs. {total:.2f}")


def main():
    while True:
        print("\n==================")
        print("   EXPENSE TRACKER")
        print("==================")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Show Total")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            show_total()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()