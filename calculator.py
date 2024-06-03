# Basic Arithmetic Calculator Program

def add(x, y):
    """This function adds two numbers"""
    return x + y

def subtract(x, y):
    """This function subtracts two numbers"""
    return x - y

def multiply(x, y):
    """This function multiplies two numbers"""
    return x * y

def divide(x, y):
    """This function divides two numbers"""
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return

        if choice == '1':
            print(f"The result of {num1} + {num2} is {add(num1, num2)}")

        elif choice == '2':
            print(f"The result of {num1} - {num2} is {subtract(num1, num2)}")

        elif choice == '3':
            print(f"The result of {num1} * {num2} is {multiply(num1, num2)}")

        elif choice == '4':
            result = divide(num1, num2)
            print(f"The result of {num1} / {num2} is {result}")

    else:
        print("Invalid Input! Please enter a valid operation number.")

if _name_ == "_main_":
    main()
