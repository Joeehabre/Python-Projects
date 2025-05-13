# Created by Joe Habre

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

def exponentiate(x, y):
    return x ** y

def calculator():
    print("Welcome to the Enhanced Calculator!")
    print("Available operations: +, -, *, /, **")
    print("Type 'exit' to quit the program.\n")

    while True:
        op = input("Enter operation (+, -, *, /, **): ")
        if op.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        if op not in ('+', '-', '*', '/', '**'):
            print("Invalid operation. Please try again.\n")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.\n")
            continue

        if op == '+':
            result = add(num1, num2)
        elif op == '-':
            result = subtract(num1, num2)
        elif op == '*':
            result = multiply(num1, num2)
        elif op == '/':
            result = divide(num1, num2)
        elif op == '**':
            result = exponentiate(num1, num2)

        print(f"Result: {result}\n")

if __name__ == "__main__":
    calculator()
