def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)
    
def remove_expense(expenses, amount, category):
    for expense in expenses:
        if expense['amount'] == amount and expense['category'] == category:
            expenses.remove(expense)
            print(f'Expense {amount} in {category} removed successfully.')
            return
    print(f'[!] Expense {amount} in {category} not found')

def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Remove category')
        print('6. Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            try:
                amount = float(input('Enter amount: '))
                if amount < 1:
                    print("[!] Invalid amount")
                else:
                    category = input('Enter category: ')
                    add_expense(expenses, amount, category)
                    print("Expense added successfully.")
            except ValueError:
                print('[!] Invalid amount')
        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
        elif choice == '5':
            try:
                amount = float(input('Enter amount to remove: '))
                category = input(f'Enter category to remove {amount}: ')
                remove_expense(expenses, amount, category)
                print(f'Category {category} removed successfully.')
            except ValueError:
                print('[!] Invalid amount')
        elif choice == '6':
            print('Exiting the program.')
            break
        else:
            print('Invalid choice. Please enter a number between 1-5.')
main()