tasks=[]
def addTask():
    task=input(" please Enter task:")
    tasks.append(task)
    print(f"Task '{task}' added.")

def deleteTask():
    listTasks()
    try:
        taskToDelete=int(input("Choose the # to delete: "))
        if taskToDelete>=0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been removed.")
        else:
            print(f"Task # {taskToDelete} was not found")    

    except:
        print("Invalid input")
def listTasks():
    if not tasks:
        print("There arre no tasks currently")
    else:
        print("Current tasks: ")
        for index, task in enumerate(tasks):
            print(f"Task #{index}, {task}")\
if __name__=='__main__':
    print("Welcome to the todo list app:")
    while True:
        print("what would you like to do?")
        print("please select one following option: ")
        print("------------------------------------")
        print("1.Add a new task")
        print("2.Delete a task")
        print("3. List tasks")
        print("4. Quit")

        cho=input("Enter your choice : ")
        if cho=="1":
            addTask()

        elif cho=="2":
            deleteTask()
        
        elif cho=="3":
            listTasks()

        elif cho=="4":
            break
        else:
            print("Invalid choice")
    print("Goodbye!!")
    


