todo_list = []
while True:
    print("#TO-DO-LIST MENU")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("enter Your Choice(1-5):")

    if choice == "1":
        if len(todo_list) == 0:
            print("No tasks yet!")
        else: 
            print("Your Tasks:")
            for i, t in enumerate(todo_list, start=1):
                print(f"{i}. {t}")
     
    elif choice == "2":
        task = input("Enter a new task:")
        todo_list.append(task)
        print(f"'{task}' added successfully!")
    
    elif choice == "3":
        if len(todo_list) == 0:
            print("Nothing to update.")
        else:
            for i, t in enumerate(todo_list, start=1):
                print(f"{i}. {t}")
            try:
                num = int(input("Which task number to update?"))
                if 1 <= num <= len(todo_list):
                    new_task = input("Enter the new task:")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter only numbers.")
    elif choice == "4":
        if len(todo_list) == 0:
            print("Nothing to delete.") 
        else:
            for i, t in enumerate(todo_list, start=1):
                print(f"{i}. {t}")
                try:
                    num = int(input("Which task number to delete?"))
                    if 1 <= num <= len(todo_list):
                        removed = todo_list.pop(num - 1)
                        print(f" '{removed}' deleted successfully!")
                    else:
                        print("Invalid number.")
                except ValueError:
                    print("Please enter only numbers.")
    elif choice == "5":
        print("Exiting...Good luck with your tasks")
        break
    else:
        print("Please select a valid option!")
                              
        