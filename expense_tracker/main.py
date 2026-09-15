expenses = []

def expenses_tracker():
    while True:

        expense = input("Enter expense: ")
        amount = float(input("Enter amount: "))
        one_expense = {
            expense: amount
        }
        expense + amount
        expenses.append(one_expense)
        another = input("Do you want another expenses? (yes/no): ")
        if another == "no" or another == "n":
            break
    print(expenses)
        
expenses_tracker()
