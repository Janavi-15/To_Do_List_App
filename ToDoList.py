tasks = []
no = int(input("Enter the number of tasks to be done:"))
for task in range(no):
    task = input("Enter Task:")
    tasks.append(task)
print("===========TO DO LIST===========")
for i, task in enumerate(tasks, start=1):
    print("[]", task)

print("CHOOSE OPERATIONS:")
print("1. Add Task")
print("2. View Tasks")
print("3. Delete Tasks")
print("4. Exit ")
choice = int(input("Enter your choice:"))

if(choice == 1):
    add = input("Enter the task to be added:")
    tasks.append(add)
    print("Task added successfully !")
    print("==========TO DO LIST==========")
    print(tasks)

elif(choice == 2):
    if(len(tasks) == 0):
        print("No tasks available")
    else:
        for i, task in enumerate(tasks, start=1):
            print(i,".", task)

elif(choice == 3):
    if(len(tasks) == 0):
        print("No task available to delete")
    else:
        delete = input("Enter the task to delete")
        tasks.remove(delete)
        print("Task deleted successfully !")
        print("=========TO DO LIST=========")
        print(tasks)

elif(choice == 4):
    print("Exiting To Do List. Goodbye !")


else:
    print("Invalid Choice ! Try Again !")