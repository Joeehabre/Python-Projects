# Created by Joe Habre
import math


def add(x, y):        return x + y
def subtract(x, y):   return x - y
def multiply(x, y):   return x * y
def power(x, y):      return x ** y
def modulus(x, y):    return x % y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y

def square_root(x):
    if x < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(x)

def factorial(x):
    if x < 0 or not float(x).is_integer():
        raise ValueError("Factorial requires a non-negative integer.")
    return math.factorial(int(x))

def fmt(value):
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)

BINARY_OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '^': power,
    '%': modulus,
}

UNARY_OPS = {
    '√': square_root,
    '!': factorial,
}


def display_menu():
    print("\n📌 Operations:")
    print("  Binary : + - * / ^ %")
    print("  Unary  : √  !")
    print("  Memory : m+  mr  mc")
    print("  Other  : h (history)  cls (clear history)  q (quit)")
    print("  Tip    : type 'ans' to reuse the last result as input")


def get_number(prompt, ans):
    raw = input(prompt).strip().lower()
    if raw == 'ans':
        if ans is None:
            raise ValueError("No previous result to use.")
        print(f"  (using ans = {fmt(ans)})")
        return ans
    return float(raw)


def main():
    memory = 0
    history = []
    ans = None

    display_menu()

    while True:
        op = input("\nEnter operation: ").strip()

        if op == 'q':
            print("👋 Goodbye!")
            break

        elif op == 'm+':
            if ans is not None and isinstance(ans, (int, float)):
                memory = ans
                print(f"💾 Saved {fmt(ans)} to memory.")
            else:
                print("❌ No valid result to save.")

        elif op == 'mr':
            print(f"📥 Memory: {fmt(memory)}")

        elif op == 'mc':
            memory = 0
            print("🧹 Memory cleared.")

        elif op == 'h':
            print("📜 History:")
            if not history:
                print("  (empty)")
            else:
                for i, entry in enumerate(history, 1):
                    print(f"  {i}. {entry}")

        elif op == 'cls':
            history.clear()
            print("🧹 History cleared.")

        elif op in UNARY_OPS:
            try:
                num = get_number("Enter number: ", ans)
                result = UNARY_OPS[op](num)
                label = f"{op}{fmt(num)} = {fmt(result)}"
                print(f"✅ {label}")
                history.append(label)
                ans = result
            except (ValueError, OverflowError) as e:
                print(f"❌ {e}")

        elif op in BINARY_OPS:
            try:
                num1 = get_number("Enter first number: ", ans)
                num2 = get_number("Enter second number: ", ans)
                result = BINARY_OPS[op](num1, num2)
                label = f"{fmt(num1)} {op} {fmt(num2)} = {fmt(result)}"
                print(f"✅ {label}")
                history.append(label)
                ans = result
            except (ValueError, ZeroDivisionError, OverflowError) as e:
                print(f"❌ {e}")

        elif op == 'menu' or op == '?':
            display_menu()

        else:
            print("❌ Unknown operation. Type 'menu' to see available operations.")


if __name__ == "__main__":
    main()
