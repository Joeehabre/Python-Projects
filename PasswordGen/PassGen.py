# Created by Joe Habre
---

## 🔐 **3. Password Generator**

### 📁 Folder: `password-generator/generator.py`

```python
import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    print("🔐 Password Generator")
    length = int(input("Enter desired length: "))
    pw = generate_password(length)
    print(f"Generated password: {pw}")
