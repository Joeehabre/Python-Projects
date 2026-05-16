# Created by Joe Habre
import json
import os
from datetime import datetime

TASKS_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")

PRIORITIES = {"1": "🔴 High", "2": "🟡 Medium", "3": "🟢 Low"}


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE) as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def make_task(name, priority="2", due=None):
    return {
        "name": name,
        "done": False,
        "priority": priority,
        "due": due,
        "created": datetime.now().strftime("%Y-%m-%d"),
    }


def display_tasks(tasks, subset=None):
    items = [(i, t) for i, t in enumerate(tasks)] if subset is None else subset
    total = len(tasks)
    done_count = sum(1 for t in tasks if t["done"])

    print(f"\n📝 To-Do List  [{done_count}/{total} done]")
    if not items:
        print("  (empty)")
        return

    for i, task in items:
        status = "✅" if task["done"] else "⬜"
        pri = PRIORITIES.get(task.get("priority", "2"), "🟡 Medium")
        due = f"  📅 {task['due']}" if task.get("due") else ""
        print(f"  {i+1:>2}. {status} [{pri}] {task['name']}{due}")


def pick_task(tasks, prompt):
    display_tasks(tasks)
    try:
        idx = int(input(prompt)) - 1
        if 0 <= idx < len(tasks):
            return idx
        print("❌ Number out of range.")
    except ValueError:
        print("❌ Invalid input.")
    return None


def add_task(tasks):
    name = input("Task description: ").strip()
    if not name:
        print("❌ Task cannot be empty.")
        return

    print("Priority: 1=High  2=Medium  3=Low (default: 2)")
    priority = input("Choose: ").strip() or "2"
    if priority not in PRIORITIES:
        priority = "2"

    due = input("Due date (YYYY-MM-DD) or leave blank: ").strip() or None
    if due:
        try:
            datetime.strptime(due, "%Y-%m-%d")
        except ValueError:
            print("⚠️  Invalid date format — saving without due date.")
            due = None

    tasks.append(make_task(name, priority, due))
    save_tasks(tasks)
    print(f"✅ Added: {name}")


def remove_task(tasks):
    idx = pick_task(tasks, "Enter task number to remove: ")
    if idx is not None:
        removed = tasks.pop(idx)
        save_tasks(tasks)
        print(f"🗑️  Removed: {removed['name']}")


def toggle_task(tasks):
    idx = pick_task(tasks, "Enter task number to toggle done/undone: ")
    if idx is not None:
        tasks[idx]["done"] = not tasks[idx]["done"]
        state = "✅ Marked done" if tasks[idx]["done"] else "⬜ Marked undone"
        save_tasks(tasks)
        print(f"{state}: {tasks[idx]['name']}")


def search_tasks(tasks):
    query = input("Search: ").strip().lower()
    if not query:
        return
    results = [(i, t) for i, t in enumerate(tasks) if query in t["name"].lower()]
    print(f"\n🔍 Results for '{query}':")
    display_tasks(tasks, results)


def sort_tasks(tasks):
    print("Sort by: 1=Priority  2=Due date  3=Name")
    choice = input("Choose: ").strip()
    if choice == "1":
        tasks.sort(key=lambda t: t.get("priority", "2"))
    elif choice == "2":
        tasks.sort(key=lambda t: (t.get("due") or "9999-99-99"))
    elif choice == "3":
        tasks.sort(key=lambda t: t["name"].lower())
    else:
        print("❌ Invalid choice.")
        return
    save_tasks(tasks)
    print("✅ Sorted.")


def clear_done(tasks):
    before = len(tasks)
    tasks[:] = [t for t in tasks if not t["done"]]
    removed = before - len(tasks)
    if removed:
        save_tasks(tasks)
        print(f"🧹 Cleared {removed} completed task(s).")
    else:
        print("No completed tasks to clear.")


def main():
    tasks = load_tasks()

    while True:
        display_tasks(tasks)
        print("\nOptions:")
        print("  [1] Add task        [2] Remove task")
        print("  [3] Toggle done     [4] Search")
        print("  [5] Sort            [6] Clear completed")
        print("  [7] Quit")

        choice = input("\nChoose: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            toggle_task(tasks)
        elif choice == "4":
            search_tasks(tasks)
        elif choice == "5":
            sort_tasks(tasks)
        elif choice == "6":
            clear_done(tasks)
        elif choice == "7":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
