todo_list = []

# Function to display the to-do list
def display_todo_list():
    print("Your To-Do List:")
    if not todo_list:
        print("No tasks in the list.")
    else:
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

# Function to add a task to the to-do list
def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")
    display_todo_list()

# Function to remove a task from the to-do list
def remove_task(task_index):
    if task_index >= 1 and task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the list.")
        display_todo_list()
    else:
        print("Invalid task index.")

# Main function
def main():
    while True:
        print("\n1. Display To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_todo_list()
        elif choice == '2':
            task = input("Enter task to add: ")
            add_task(task)
        elif choice == '3':
            display_todo_list()
            task_index = int(input("Enter index of task to remove: "))
            remove_task(task_index)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
