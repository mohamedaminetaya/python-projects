tasks = []

while True:

    print("\n=== TO-DO LIST ===")
    print("1 Add task")
    print("2 Show tasks")
    print("3 Delete task")
    print("4 Exit")

    choice = int(input("Enter option : "))

    if choice == 1:

        task = input("Enter task : ")

        tasks.append(task)

        print("Task added successfully")

    elif choice == 2:

        if len(tasks) == 0:

            print("No tasks found")

        else:

            print("\n=== Tasks ===")

            for task in tasks:

                print("-", task)

    elif choice == 3:

        delete_task = input("Enter task to delete : ")

        if delete_task in tasks:

            tasks.remove(delete_task)

            print("Task deleted successfully")

        else:

            print("Task not found")

    elif choice == 4:

        print("Program closed")

        break

    else:

        print("Invalid choice")
