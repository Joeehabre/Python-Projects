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
    print(" +  : Addition")
    print(" -  : Subtraction")
    print(" *  : Multiplication")
    print(" /  : Division")
    print(" ^  : Power (x^y)")
    print(" %  : Modulus")
    print(" √  : Square Root")
    print(" !  : Factorial")
    print(" m+ : Save result to memory")
    print(" mr : Recall memory")
    print(" mc : Clear memory")
    print(" h  : View history")
    print(" q  : Quit")

memory = 0
history = []
last_result = None

while True:
    display_menu()
    op = input("\nEnter operation: ").strip()

    if op == 'q':
        print("👋 Exiting calculator. Bye!")
        break

    if op == 'm+':
        if last_result is not None and isinstance(last_result, (int, float)):
            memory = last_result
            print("💾 Result saved to memory.")
        else:
            print("❌ No valid result to save.")
        continue

    if op == 'mr':
        print(f"📥 Memory: {memory}")
        continue

    if op == 'mc':
        memory = 0
        print("🧹 Memory cleared.")
        continue

    if op == 'h':
        print("📜 History:")
        if not history:
            print("  (No history yet)")
        for i, r in enumerate(history, 1):
            print(f"  {i}. {r}")
        continue

    if op in ('√', '!'):
        try:
            num = float(input("Enter number: "))
            result = square_root(num) if op == '√' else factorial(num)
        except ValueError:
            result = "❌ Invalid number."

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
            result = "❌ Invalid input. Please enter numbers."
    else:
        result = "❌ Invalid operation."

    print(f"✅ Result: {result}")
    last_result = result
    if isinstance(result, (int, float)):
        history.append(result)
