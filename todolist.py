''' To-DO-List '''
#task list
tasks=[]
while True:
    #task menu button
    print("\n To-Do List Menu")
    print("1. View Task")
    print("2. Add a New Task")
    print("3. Remove a Task")
    print("4. Exit")
    print("5. Clear All task")
    choice = input("Enter your choice (1-4):")
    # Veiwing available task 
    if choice == '1':
        if not tasks:
            print("Your task list is empty")
        else:
            print("Your Task:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
    # Adding a tasks
    elif choice == '2':
        new_task = input("Enter the task here :")
        tasks.append(new_task)
        print(f"Task '{new_task}' added.")
    # removing a task
    elif choice == '3':
        if not tasks:
            print("No tasks to remove")
        else:
            for i , task in enumerate(tasks, start='1'):
                print(f"{i}. {task}")
            try:
                task_num=int(input("Enter the task number to remove here:"))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"Task '{removed}' removed")
                else:
                    print("Invalid Task Number")
            except ValueError:
                print("Please enter a valid number")
    # exiting the App
    elif choice == "4":
        print("Exiting To-DO List App. Goodbye!!!")
    # deleting All Availabe task
    elif choice == '5':
        confirm = input("Are you sure you want to clear all the tasks (yes/no):").lower()
        if confirm == 'yes':
            del tasks[:]
            print("All tasks cleared")
        else:
            print("Clear cancelled")
            break
    else:
        print("Invalid Choice. Please enter 1-4")
                
                

    
