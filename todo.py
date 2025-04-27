import json

class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)

def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as f:
            return [Task(**data) for data in json.load(f)]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    category = input("Enter task category (e.g., Work, Personal, Urgent): ")
    task = Task(title, description, category)
    tasks.append(task)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, start=1):
        status = "Completed" if task.completed else "Pending"
        print(f"{idx}. [{status}] {task.title} - {task.description} ({task.category})")

def mark_task_completed(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_no = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_no <= len(tasks):
            tasks[task_no - 1].mark_completed()
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_no = int(input("Enter the task number to delete: "))
        if 1 <= task_no <= len(tasks):
            removed_task = tasks.pop(task_no - 1)
            print(f"Task '{removed_task.title}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- Personal To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
