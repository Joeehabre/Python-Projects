# Created by Joe Habre

import random
import string
import secrets

try:
    import pyperclip  # Optional: Auto-copy to clipboard
    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False

def estimate_strength(length, use_upper, use_digits, use_symbols):
    pool_size = len(string.ascii_lowercase)
    if use_upper:
        pool_size += len(string.ascii_uppercase)
    if use_digits:
        pool_size += len(string.digits)
    if use_symbols:
        pool_size += len(string.punctuation)
    entropy = length * (pool_size.bit_length())
    if entropy < 50:
        return "🟥 Weak"
    elif entropy < 75:
        return "🟧 Moderate"
    else:
        return "🟩 Strong"

def generate_password(length, use_upper, use_digits, use_symbols):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if len(chars) == 0:
        return None

    return ''.join(secrets.choice(chars) for _ in range(length))

def main():
    print("🔐 Advanced Password Generator")
    try:
        length = int(input("Password length (8–64 recommended): "))
        if length <= 0:
            raise ValueError
    except ValueError:
        print("❌ Invalid length.")
        return

    use_upper = input("Include UPPERCASE letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_upper, use_digits, use_symbols)

    if not password:
        print("❌ No character sets selected.")
        return

    strength = estimate_strength(length, use_upper, use_digits, use_symbols)

    print(f"\n✅ Generated Password: {password}")
    print(f"🔐 Strength: {strength}")

    if CLIPBOARD_AVAILABLE:
        pyperclip.copy(password)
        print("📋 Password copied to clipboard.")
    else:
        print("📋 Install 'pyperclip' to enable auto-copy.")

if __name__ == "__main__":
    main()
