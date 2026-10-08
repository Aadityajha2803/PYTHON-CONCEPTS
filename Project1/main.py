expenses = []
print("Welcome to expense tracker")
while True:
    print("===Menu===")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View total expenses")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))

    expense = {
        "date":date,
        "category":category,
        "description":description,
        "amount":amount
    }
    expenses.append(expense)
    print("Expense added successfully!")

    if (choice == 2):
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            print("===Expenses===")
            count = 1
            for eachkharcha in expenses:
                print(f"{count}. Date: {eachkharcha['date']}, Category: {eachkharcha['category']}, Deescription: {eachkharcha['description']}, Amount: {eachkharcha['amount']}")
                count = count+1

    if (choice == 3):
        total = 0
        for eachkharcha in expenses:
            total = total + eachkharcha['amount']
        print("\nTotal expenses: ", total)

    if (choice == 4):
        print("Thank you for using expense tracker!")
        break


