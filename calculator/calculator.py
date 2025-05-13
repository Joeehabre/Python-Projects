# Created by Joe Habre
import math

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "❌ Cannot divide by zero." if y == 0 else x / y
def power(x, y): return x ** y
def modulus(x, y): return x % y
def square_root(x): return math.sqrt(x)
def factorial(x): return math.factorial(int(x)) if x >= 0 and float(x).is_integer() else "❌ Invalid input for factorial"

def display_menu():
    print("\n📌 Available Operations:")
    print(" + : Addition")
    print(" - : Subtraction")
    print(" * : Multiplication")
    print(" / : Division")
    print(" ^ : Power (x^y)")
    print(" % : Modulus")
    print(" √ : Square Root")
    print(" ! : Factorial")
    print(" q : Quit")

while True:
    display_menu()
    op = input("\nEnter operation: ").strip()

    if op == 'q':
        print("👋 Exiting calculator. Bye!")
        break

    # Unary operations
    if op in ('√', '!'):
        try:
            num = float(input("Enter number: "))
            result = square_root(num) if op == '√' else factorial(num)
        except ValueError:
            result = "❌ Invalid number."
    # Binary operations
    elif op in ('+', '-', '*', '/', '^', '%'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = {
                '+': add,
                '-': subtract,
                '*': multiply,
                '/': divide,
                '^': power,
                '%': modulus
            }[op](num1, num2)
        except ValueError:
            result = "❌ Invalid input. Please enter valid numbers."
    else:
        result = "❌ Invalid operation."

    print(f"✅ Result: {result}")
