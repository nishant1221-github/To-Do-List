# ..............To-Do List..............

# Initialize an empty list to hold tasks
added_tasks = []

while True:
    
    # Display menu options
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    
    # Get user choice
    option = input("Enter your choice (1-4): ")

    if option == '1':
        # Add a task
        task = input("Enter the task: ")
        added_tasks.append(task)
        print(f"Task '{task}' added.")
        
    elif option == '2':
        # View tasks
        if added_tasks:
            print("\nYour To-Do List:")
            for index, task in enumerate(added_tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Your To-Do list is empty.")
    
    elif option == '3':
        # Remove a task
        if added_tasks:
            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(added_tasks):
                removed_task = added_tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' removed.")
            else:
                print("Invalid task number.")
        else:
            print("Your To-Do list is empty.")
    
    elif option == '4':
        # Exit the program
        print("Exiting the program...")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
