# Created by Joe Habre
import math
import os
import secrets
import string
from datetime import datetime

try:
    import pyperclip
    CLIPBOARD = True
except ImportError:
    CLIPBOARD = False

AMBIGUOUS = set("Il1O0")


def build_charset(use_upper, use_digits, use_symbols, exclude_ambiguous):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    if exclude_ambiguous:
        chars = "".join(c for c in chars if c not in AMBIGUOUS)
    return chars


def ensure_requirements(password, chars, use_upper, use_digits, use_symbols):
    """Guarantee at least one character from each enabled set."""
    required = []
    if use_upper:
        pool = [c for c in string.ascii_uppercase if c in chars]
        if pool:
            required.append(secrets.choice(pool))
    if use_digits:
        pool = [c for c in string.digits if c in chars]
        if pool:
            required.append(secrets.choice(pool))
    if use_symbols:
        pool = [c for c in string.punctuation if c in chars]
        if pool:
            required.append(secrets.choice(pool))

    pw = list(password)
    for i, ch in enumerate(required):
        pos = secrets.randbelow(len(pw))
        pw[pos] = ch
    return "".join(pw)


def generate_password(length, use_upper, use_digits, use_symbols, exclude_ambiguous):
    chars = build_charset(use_upper, use_digits, use_symbols, exclude_ambiguous)
    if not chars:
        return None, 0
    pw = "".join(secrets.choice(chars) for _ in range(length))
    pw = ensure_requirements(pw, chars, use_upper, use_digits, use_symbols)
    entropy = length * math.log2(len(chars))
    return pw, entropy


def strength_label(entropy):
    if entropy < 40:  return "🟥 Very Weak"
    if entropy < 60:  return "🟧 Weak"
    if entropy < 80:  return "🟨 Moderate"
    if entropy < 100: return "🟩 Strong"
    return "💎 Very Strong"


def ask_yn(prompt, default="y"):
    tag = "(Y/n)" if default == "y" else "(y/N)"
    answer = input(f"{prompt} {tag}: ").strip().lower() or default
    return answer == "y"


def save_to_file(passwords):
    path = os.path.join(os.path.dirname(__file__), "passwords.txt")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(path, "a") as f:
        f.write(f"\n# Generated {timestamp}\n")
        for pw in passwords:
            f.write(pw + "\n")
    print(f"💾 Saved to {path}")


def main():
    print("🔐 Password Generator\n")

    try:
        length = int(input("Password length (8–128 recommended): ").strip())
        if not (4 <= length <= 512):
            raise ValueError
    except ValueError:
        print("❌ Invalid length.")
        return

    use_upper    = ask_yn("Include UPPERCASE letters?")
    use_digits   = ask_yn("Include digits?")
    use_symbols  = ask_yn("Include symbols?")
    excl_ambig   = ask_yn("Exclude ambiguous characters (I, l, 1, O, 0)?")

    try:
        count = int(input("How many passwords to generate? (default 1): ").strip() or "1")
        if count < 1:
            raise ValueError
    except ValueError:
        print("❌ Invalid count, using 1.")
        count = 1

    passwords = []
    entropy = 0
    for _ in range(count):
        pw, entropy = generate_password(length, use_upper, use_digits, use_symbols, excl_ambig)
        if pw is None:
            print("❌ No character sets selected.")
            return
        passwords.append(pw)

    print()
    for i, pw in enumerate(passwords, 1):
        label = f"  {i}. " if count > 1 else "  "
        print(f"{label}{pw}")

    # Entropy depends only on length and charset, so it is identical for every
    # password generated with these settings.
    print(f"\n  🔐 Entropy   : ~{entropy:.1f} bits")
    print(f"  💪 Strength  : {strength_label(entropy)}")

    if CLIPBOARD and count == 1:
        pyperclip.copy(passwords[0])
        print("  📋 Copied to clipboard.")
    elif not CLIPBOARD:
        print("  📋 Install 'pyperclip' to enable auto-copy.")

    if ask_yn("\nSave to file?", default="n"):
        save_to_file(passwords)


if __name__ == "__main__":
    main()
