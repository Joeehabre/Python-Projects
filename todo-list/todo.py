import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        f.writelines(task + "\n" for task in tasks)

def show_tasks(tasks):
    print("\n📝 Your To-Do List:")
    if not tasks:
        print(" (empty)")
    for i, task in enumerate(tasks, 1):
        print(f" {i}. {task}")

def main():
    tasks = load_tasks()
    while True:
        show_tasks(tasks)
        print("\nOptions: [a]dd  [r]emove  [c]lear  [q]uit")
        choice = input("Choose an option: ").strip().lower()

        if choice == 'a':
            task = input("Enter new task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
        elif choice == 'r':
            try:
                index = int(input("Enter task number to remove: "))
                if 1 <= index <= len(tasks):
                    tasks.pop(index - 1)
                    save_tasks(tasks)
            except:
                print("❌ Invalid input.")
        elif choice == 'c':
            confirm = input("Clear all tasks? (y/n): ").lower()
            if confirm == 'y':
                tasks.clear()
                save_tasks(tasks)
        elif choice == 'q':
            break

if __name__ == "__main__":
    main()
