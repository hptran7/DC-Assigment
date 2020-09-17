#Function
from function import *
def listing():
    for m in range(0,len(task_list)):
        print(str(m+1)+ f' - {task_list[m]["title"]} - {task_list[m]["priority"]}')

#Code Assignment:
print("Press 1 to add task")
print("Press 2 to delete task")
print("Press 3 to view all task")
print("Press q to quit")
task_list=[]
choose = input("please make your choose: ")
while choose != "q":
    if int(choose) == 1:
        task = input("Please enter your task: ")
        priority = input("Please enter the priority: ")
        task_list.append(add_task(task,priority))
        print("Here is your new list:")
        listing()
    elif int(choose) ==2 :
        if task_list:
            print("Please see the list of task:")
            listing()
            delete = int(input("Please choose the task nunber you wish to delete: "))
            task_list.pop(delete-1)
            print("Here is your new list:")
            listing()
        else:
            print("Your list is empty")
    elif int(choose) == 3:
        if task_list:
            print("Here is the List of tasks:")
            listing()
        else:
            print("your task list is empty")
    choose = input("Please make your choice again: ")