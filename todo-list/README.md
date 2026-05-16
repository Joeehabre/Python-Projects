# ✅ To-Do List

A terminal task manager with priorities, due dates, search, sort, and JSON persistence.

---

## ✨ Features

- 🔴🟡🟢 **Priorities** — High / Medium / Low
- 📅 **Due dates** with validation (`YYYY-MM-DD`)
- 🔍 **Search** tasks by keyword
- 🔃 **Sort** by priority, due date, or name
- ☑️ **Toggle** done / undone (not one-way)
- 🧹 **Clear completed** in one shot
- 💾 Saved to `tasks.json` — survives restarts and handles special characters properly
- `[done/total]` count in the header

---

## 🚀 Run

```bash
python todo.py
```

No dependencies — stdlib only. Tasks are saved to `tasks.json` next to the script.

---

## 💻 Demo

```
📝 To-Do List  [1/3 done]

   1. ✅ [🔴 High]   Buy groceries         📅 2026-05-17
   2. ⬜ [🟡 Medium] Review pull request
   3. ⬜ [🟢 Low]    Clean desktop

Options:
  [1] Add task        [2] Remove task
  [3] Toggle done     [4] Search
  [5] Sort            [6] Clear completed
  [7] Quit
```
