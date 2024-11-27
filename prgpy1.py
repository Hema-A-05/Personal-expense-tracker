import pandas as pd 
import matplotlib.pyplot as plt
#intialize an empty dataframe to store expenses
expenses=pd.DataFrame(columns=['Date','Category','Description','Amount'])

def add_expense(date,category,description,amount):
    global expenses
    new_expense = pd.DataFrame({'Date': [date], 'Category': [category], 'Description': [description], 'Amount': [amount]})
    expenses = pd.concat([expenses, new_expense], ignore_index=True)

def view_expenses():
    global expenses
    print(expenses)

def save_expenses(file_name):
    global expenses
    expenses.to_csv(file_name, index=False)
    print(f"Expenses saved to {file_name}")

def load_expenses(file_name):
    global expenses
    expenses = pd.read_csv(file_name)
    print(f"Expenses loaded from {file_name}")

def plot_expenses():
    global expenses
    expenses['Amount'] = expenses['Amount'].astype(float)
    expenses.groupby('Category')['Amount'].sum().plot(kind='bar')
    plt.title('Expenses by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Amount')
    plt.show()

def main():
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Save Expenses")
        print("4. Load Expenses")
        print("5. Plot Expenses")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD): ")
            category = input("Enter the category: ")
            description = input("Enter the description: ")
            amount = input("Enter the amount: ")
            add_expense(date, category, description, amount)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            file_name = input("Enter the file name to save (e.g., expenses.csv): ")
            save_expenses(file_name)
        elif choice == '4':
            file_name = input("Enter the file name to load (e.g., expenses.csv): ")
            load_expenses(file_name)
        elif choice == '5':
            plot_expenses()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

