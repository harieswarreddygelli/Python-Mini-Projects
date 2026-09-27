import math

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y

def divide(x, y):
    if y == 0: return "Error! Division by zero."
    return x / y

def power(x, y): return x ** y

def square_root(x):
    if x < 0: return "Error! Cannot calculate square root of a negative number."
    return math.sqrt(x)

def show_history(history_list):
    """Displays the current session history."""
    if not history_list:
        print("\n[ History is empty ]")
    else:
        print("\n=== Calculation History ===")
        for index, item in enumerate(history_list, 1):
            print(f"{index}. {item}")

def calculator():
    history = []
    print("=== Advanced Python Calculator Mini-Project ===")
    
    while True:
        print("\nSelect an operation:")
        print("1. Basic Math (+, -, *, /)")
        print("2. Power / Exponentiation (x^y)")
        print("3. Square Root (√x)")
        print("4. View History")
        print("5. Delete / Clear History")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ").strip()
        
        if choice == '6':
            print("Exiting calculator. Goodbye!")
            break
            
        # 1. Basic Math Operations
        if choice == '1':
            print("\n[ Basic Math ] 1. Add | 2. Subtract | 3. Multiply | 4. Divide")
            sub_choice = input("Select operation (1-4): ").strip()
            if sub_choice not in ('1', '2', '3', '4'):
                print("Invalid operational choice.")
                continue
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue
            
            if sub_choice == '1':
                res = add(num1, num2)
                record = f"{num1} + {num2} = {res}"
            elif sub_choice == '2':
                res = subtract(num1, num2)
                record = f"{num1} - {num2} = {res}"
            elif sub_choice == '3':
                res = multiply(num1, num2)
                record = f"{num1} * {num2} = {res}"
            elif sub_choice == '4':
                res = divide(num1, num2)
                record = f"{num1} / {num2} = {res}"
            
            print(f"Result: {res}")
            history.append(record)

        # 2. Power Expansion
        elif choice == '2':
            try:
                base = float(input("Enter base number (x): "))
                exponent = float(input("Enter exponent power (y): "))
            except ValueError:
                print("Invalid numerical input.")
                continue
            res = power(base, exponent)
            record = f"{base} ^ {exponent} = {res}"
            print(f"Result: {res}")
            history.append(record)

        # 3. Square Root Expansion
        elif choice == '3':
            try:
                num = float(input("Enter number: "))
            except ValueError:
                print("Invalid numerical input.")
                continue
            res = square_root(num)
            record = f"√{num} = {res}"
            print(f"Result: {res}")
            history.append(record)

        # 4. View History
        elif choice == '4':
            show_history(history)

        # 5. Delete History
        elif choice == '5':
            if not history:
                print("\nHistory is already clean.")
            else:
                history.clear()
                print("\n[ Success: Calculation history deleted! ]")
        else:
            print("Invalid main menu choice! Please select 1 to 6.")

if __name__ == "__main__":
    calculator()
