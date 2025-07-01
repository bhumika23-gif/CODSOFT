import json
import os

FILENAME = "tasks.json"

# Load tasks from a file if it exists
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

# Save current tasks to the file
def save_tasks(task_list):
    with open(FILENAME, "w") as file:
        json.dump(task_list, file, indent=4)

# Show all tasks with their status
def show_tasks(task_list):
    if not task_list:
        print("\nYour to-do list is empty.\n")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(task_list, start=1):
            status = "Done" if task['done'] else "Pending"
            print(f"{index}. {task['task']} [{status}]")
        print()

# Add a new task
def add_task(task_list):
    task_text = input("Enter the task you want to add: ").strip()
    if task_text:
        task_list.append({"task": task_text, "done": False})
        save_tasks(task_list)
        print("Task added successfully.")
    else:
        print("Task cannot be empty.")

# Mark a task as done
def mark_done(task_list):
    show_tasks(task_list)
    try:
        choice = int(input("Enter the task number you completed: "))
        if 1 <= choice <= len(task_list):
            task_list[choice - 1]['done'] = True
            save_tasks(task_list)
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task(task_list):
    show_tasks(task_list)
    try:
        choice = int(input("Enter the task number to delete: "))
        if 1 <= choice <= len(task_list):
            removed = task_list.pop(choice - 1)
            save_tasks(task_list)
            print(f"Deleted: '{removed['task']}'")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu
def main():
    print("Welcome to the To-Do List Manager\n")
    tasks = load_tasks()

    while True:
        print("Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
