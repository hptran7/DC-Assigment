print("Press 1 to add task")
print("Press 2 to delete task")
print("Press 3 to view all task")
print("Press q to quit")
choose = input("")
task = {}
task_list=[]
while choose != "q":
    if int(choose) == 1:
        title = input("Please enter your task title: ")
        priority = input("Please enter you task priority: ")
        task["title"] = title
        task["priority"] = priority
        task_list.append(task.copy())
        print(task_list)
    elif int(choose) == 2:
        print("Please see the List of task: ")
        for n in range(0,len(task_list)):
            print(str(n+1) + " - " +task_list[n]["title"] 
            +" - " + task_list[n]["priority"])
        delete = int(input("Please choose the task nunber you wish to delete: "))
        task_list.pop(delete-1)
    elif int(choose) == 3:
        print("Here is the List of tasks:")
        for m in range(0,len(task_list)):
            print(str(m+1) + " - " +task_list[m]["title"] 
            +" - " + task_list[m]["priority"])
    choose = input("Please choose what you want to do next: ")