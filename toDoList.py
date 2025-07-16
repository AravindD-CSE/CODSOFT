def show_menu():
    print("\nTo-Do List")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def main():
    todo_list = []

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nYour tasks:")
            if not todo_list:
                print("No tasks yet!")
            else:
                for idx, task in enumerate(todo_list, start=1):
                    print(f"{idx}. {task}")

        elif choice == '2':
            task = input("Enter new task: ")
            todo_list.append(task)
            print("Task added to list")

        elif choice == '3':
            if not todo_list:
                print("No tasks to remove!")
            else:
                for idx, task in enumerate(todo_list, start=1):
                    print(f"{idx}. {task}")
                try:
                    task_num = int(input("Enter task number to remove: "))
                    if 1 <= task_num <= len(todo_list):
                        removed = todo_list.pop(task_num - 1)
                        print(f"Removed task: {removed}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == '4':
            print("Thank you!")
            break

if __name__ == "__main__":
    main()
