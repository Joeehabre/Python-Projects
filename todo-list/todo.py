# Created by Joe Habre
import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(tasks):
    print("\n📝 Your To-Do List")
    if not tasks:
        print(" (empty)")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task.startswith("[x]") else "⬜"
        print(f" {i}. {status} {task[4:] if task.startswith('[x]') else task}")

def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)

def remove_task(tasks):
    try:
        index = int(input("Enter task number to remove: "))
        if 1 <= index <= len(tasks):
            del tasks[index - 1]
            save_tasks(tasks)
    except:
        print("❌ Invalid input.")

def mark_complete(tasks):
    try:
        index = int(input("Enter task number to mark as done: "))
        if 1 <= index <= len(tasks):
            if not tasks[index - 1].startswith("[x]"):
                tasks[index - 1] = "[x] " + tasks[index - 1]
                save_tasks(tasks)
    except:
        print("❌ Invalid input.")

def clear_tasks(tasks):
    confirm = input("Are you sure you want to clear all tasks? (y/n): ").lower()
    if confirm == 'y':
        tasks.clear()
        save_tasks(tasks)

def main():
    tasks = load_tasks()

    while True:
        display_tasks(tasks)
        print("\nOptions:")
        print(" [1] Add Task")
        print(" [2] Remove Task")
        print(" [3] Mark Task as Complete")
        print(" [4] Clear All")
        print(" [5] Quit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            mark_complete(tasks)
        elif choice == '4':
            clear_tasks(tasks)
        elif choice == '5':
            print("👋 Exiting To-Do List. Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
