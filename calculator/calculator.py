#Created by Joe Habre

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Cannot divide by zero." if y == 0 else x / y

print("Simple Calculator")
print("Select operation: +, -, *, /")

while True:
    op = input("Enter operation (+, -, *, / or q to quit): ")
    if op == 'q': break
    if op not in ('+', '-', '*', '/'):
        print("Invalid operation."); continue
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input."); continue

    print("Result:", {
        '+': add, '-': subtract, '*': multiply, '/': divide
    }[op](num1, num2))
