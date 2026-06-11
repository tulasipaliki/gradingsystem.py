tasks = []

def show_menu():
    print("\n===== TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                status = "✓" if task["completed"] else "✗"
                print(f"{i}. {task['task']} [{status}]")

    elif choice == "3":
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['task']}")
            try:
                task_num = int(input("Enter task number to mark completed: "))
                tasks[task_num - 1]["completed"] = True
                print("Task marked as completed!")
            except (ValueError, IndexError):
                print("Invalid task number.")

    elif choice == "4":
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['task']}")
            try:
                task_num = int(input("Enter task number to delete: "))
                removed_task = tasks.pop(task_num - 1)
                print(f"Deleted task: {removed_task['task']}")
            except (ValueError, IndexError):
                print("Invalid task number.")

    elif choice == "5":
        print("Exiting Task Manager...")
        break

    else:
        print("Invalid choice. Please try again.")