# 🔐 Password Generator

Cryptographically secure password generator with real entropy scoring, batch output, and save-to-file.

---

## ✨ Features

- 🎲 Uses `secrets` module (CSPRNG — not `random`)
- 💎 **Real entropy** calculated as `length × log₂(pool size)` in bits
- 💪 5-tier strength scale: Very Weak → Very Strong
- ✅ **Guaranteed character requirements** — if you enable uppercase, at least one will always appear
- 🚫 **Exclude ambiguous characters** option (`I`, `l`, `1`, `O`, `0`)
- 🔢 **Batch mode** — generate multiple passwords at once
- 💾 **Save to file** — appends to `passwords.txt` with a timestamp
- 📋 Auto-copy to clipboard (requires `pyperclip`, single password only)

---

## 🚀 Run

```bash
pip install pyperclip   # optional
python PassGen.py
```

---

## 💻 Demo

```
🔐 Password Generator

Password length (8–128 recommended): 20
Include UPPERCASE letters? (Y/n): y
Include digits? (Y/n): y
Include symbols? (Y/n): y
Exclude ambiguous characters (I, l, 1, O, 0)? (Y/n): y
How many passwords to generate? (default 1): 3

  1. rK#9mQv$wXp@2nBzTe!f
  2. Jd&8sYqN%cW3hPvR!mGx
  3. Bt*5nFjH@kQ7wZrC#pMy

  🔐 Entropy   : ~131.1 bits
  💪 Strength  : 💎 Very Strong
```
