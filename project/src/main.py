tasks = []


def show_menu():
    print("\nConsole ToDo Manager")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")


def add_task():
    title = input("Task title: ").strip()

    if title == "":
        print("Error: Task title cannot be empty!")
        return

    task = {
        "title": title,
        "done": False
    }

    tasks.append(task)
    print("Task added...")


def show_tasks():
    if len(tasks) == 0:
        print("No tasks available...")
        return

    for index, task in enumerate(tasks, start=1):
        status = "done" if task["done"] else "open"
        print(f"{index}. {task['title']} [{status}]")


def mark_task_done():
    show_tasks()

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("Task number to mark as done: "))
        tasks[task_number - 1]["done"] = True
        print("Task marked as done.")
    except (ValueError, IndexError):
        print("Error: Invalid task number!")


def delete_task():
    show_tasks()

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("Task number to delete: "))
        removed_task = tasks.pop(task_number - 1)
        print(f"Deleted task: {removed_task['title']}")
    except (ValueError, IndexError):
        print("Error: Invalid task number!")


while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        mark_task_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option...")