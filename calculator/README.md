# 🧮 Calculator

A terminal calculator that goes beyond basic math — with `ans` chaining, memory, full expression history, and clean integer output.

---

## ✨ Features

| Feature | Detail |
|---|---|
| Basic ops | `+` `-` `*` `/` `^` `%` |
| Unary ops | `√` (square root), `!` (factorial) |
| `ans` keyword | Reuse the last result as input for chaining |
| Memory | `m+` save · `mr` recall · `mc` clear |
| History | `h` view · `cls` clear — stores full expressions (`3 + 4 = 7`) |
| Error handling | Divide by zero, negative sqrt, non-integer factorial |

---

## 🚀 Run

```bash
python calculator.py
```

No dependencies — stdlib only.

---

## 💻 Demo

```
Enter operation: +
Enter first number: 100
Enter second number: 23
✅ 100 + 23 = 123

Enter operation: *
Enter first number: ans        ← reuses 123
Enter second number: 2
✅ 123 * 2 = 246
```

---

## 🎮 Commands

| Command | Action |
|---|---|
| `+` `-` `*` `/` `^` `%` | Binary operation |
| `√` `!` | Unary operation |
| `ans` | Use last result as a number input |
| `m+` / `mr` / `mc` | Memory save / recall / clear |
| `h` | View history |
| `cls` | Clear history |
| `menu` or `?` | Show operation menu |
| `q` | Quit |
