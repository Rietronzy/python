# todo_list.py

tasks = []

def view_tasks():
    print("\nTasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added.")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to remove: "))
        tasks.pop(task_num - 1)
        print("Task removed.")
    except (ValueError, IndexError):
        print("Invalid task number.")

def main():
    while True:
        print("\n1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()