# Date: 2021 - 09 - 13

# Author: Njabulo Nxumalo

# Purpose: Create a task manager that will read and write tasks to a text file. Allow admin user to register users,
# by writing them to a text file. Allow logged in users to add tasks, view own tasks or all tasks.

import datetime as date
import math

# Function converts string list elements into integers
def str_int(str_list):
    for string in range(len(str_list)):
        str_list[string] = int(str_list[string])

    return str_list


# Menu function requests input on specific options depending on user type. Takes logged in username string
def menu(user_now):
    if user_now== "admin":
        menu = input("-"*43 + "\nPlease select one of the following options: \n" 
                     +"-"*43 + "\n" + " r  - Register user " +
                     "\n a  - Add task \n va - View all tasks \n " +
                     "vm - View my tasks \n gr - Generate reports \n ds - Display statistics \n e  - Exit \n\n" )
    else:
        menu = input("-"*43 + "\nPlease select one of the following options: \n" 
                     +"-"*43 + "\n" + 
                     "\n a  - Add task \n va - View all tasks \n " +
                     "vm - View my tasks \n e  - Exit \n\n" )
    return menu  
  

# Function checks if a username exists in given dictionary. Username argument is a string.
def username_check(username,dictionary):
    if dictionary.get(username) == None:
        return False
    else:
        return True
    

# Function registers user. Takes argument.
def reg_user(user_file, dictionary):
    username = input("Username: ")
    while username_check(username,dictionary) == True:
        print("Username already exists. Enter new username")
        username = input("Username: ")
        
    password = input("Password: ")
    confirm = input("Confirm password: " + "\n" )
    
    while confirm != password:
         confirm = input("\nInput does not match password"+ "\n" +
                         "\n" + "Confirm password: ")
    
    user_file.write(f"\n{username}" + ", " + f"{password}")
    

# Definition returns list of task values, indexed according to the order of attributes in task file.
def add_task():
    assign = ["Username: ", "Title of the task: " , "Task description: ",
                      "Due date (DD/MM/YY): ", date.datetime.now().strftime("%x"),  "No" ]
    
    for value in range(len(assign)):
        # if statement automatically assigns date and task status.
        if value == 4 or value == 5:
            assign[value] = assign[value]
        else:
            assign[value] = input(assign[value])

    return assign


# Prints all tasks in task file in readable table format. One file argument. 
def view_all(task_file):
    for line in task_file.readlines():
        line_l = line.split(", ")
        print("-"*45)
        
        table = [f"\n{'Assigned to':17s}: {line_l[0]}", 
                 f"{'Task':17s}: {line_l[1]}",
                 f"{'Task description':17s}: {line_l[2]}", 
                 f"{'Due date':17s}: {line_l[3]}",
                 f"{'Date created':17s}: {line_l[4]}", 
                 f"{'Completion status':17s}: {line_l[5]}"]

        for value in table:
            print(value)

# Function prints out the tasks of the logged in user and takes two arguments.
def view_mine(user_now):
    task_file = open("tasks.txt", "r")
    num_tasks = 0
    task_list = []
    
    for line in task_file.readlines():
        task = line.split(", ")
        task_list.append(task)
        
        if user_now == task[0]:
            num_tasks += 1
            print(f"{num_tasks} - Task Title: {task[1]}")
            print("-"*44)
            
    task_file.close 
       
    if num_tasks > 0:
        choice = int(input("\n" + "1 - Choose task to edit or mark as complete: \n" 
                           + "(-1) - Exit menu" + "\n\n" ))
        print("-"*44)
        action = choice
        
        while action != -1:
            print("-"*33)
            action = int(input("1 - Assign task to different user\n" +
                               "2 - Change due date\n" +
                               "3 - Mark task as completed\n" +
                               "-1 to EXIT menu" + "\n\n"))
            print("-"*33)
            count = 0
            
            # Completion status change block.
            if action == 3:
                for task in task_list:
                    if task[0] == user_now:
                        count += 1
                        if choice == count:
                            if task[5].strip("\n") == "No":
                                task[5] = "Yes\n"
                                print("\nStatus changed")
                                break
                            
                            elif task[-1] == "Yes":
                                print("Task has already been completed." + "\n")
                                
            # Change user that task is assigned to.
            elif action == 1:
                for task in task_list:
                    if task[0] == user_now:
                        count += 1
                        if choice == count:
                            name = input("Enter new name to assign task to: ")
                            task[0] = name
                            
            # Change due date of task.     
            elif action == 2:
                for task in task_list:
                    if task[0] == user_now:
                        count += 1
                        if choice == count:
                            new_date = input("Enter a new due date (DD/MM/YY): ")
                            task[-3] = new_date.strip()
                                  
        task_file = open("tasks.txt" , "w")
        task_file.close
        task_file = open("tasks.txt" , "a")
        for line in task_list:
            line = ", ".join(line)
            task_file.write(line)

        task_file.close
        
    elif num_tasks == 0:
        print("You currently have no tasks assigned to you.")

# Function writes task report values to text file.
def task_overview():
    task_file = open("tasks.txt", "r")
    task_list = task_file.readlines()
    task_file.close()
    total_tasks = len(task_list)
    complete_tasks = 0
    overdue_tasks = 0
    date_now = str_int(date.datetime.now().strftime("%x").split("/"))
    
    for task in task_list:
        task_properties = task.split(", ")
        due_date = str_int(task_properties[3].split("/"))
        
        for day in reversed(range(3)):
            overdue = date_now[day] > due_date[day]
            if overdue == True:
                overdue_tasks += 1
                break
            
        if task_properties[5].lower().strip("\n") == "yes":
            complete_tasks += 1
     
    incomplete_tasks = total_tasks - complete_tasks
    over_incomplete = incomplete_tasks + overdue_tasks
    incomplete_percent = round((incomplete_tasks/total_tasks)*100,2)
    overdue_percent = round((overdue_tasks/total_tasks)*100,2)
    
    report = [str(total_tasks)+"\n", str(complete_tasks) + 
              "\n",str(incomplete_tasks) +
              "\n",str(over_incomplete) + "\n",
               str(incomplete_percent) + "\n", 
               str(overdue_percent) + "\n"]

     
    with open("task_overview.txt","w") as t_ov:
        t_ov.writelines(report)


# Function writes user report values in textfile.
def user_overview():
    task_file = open("tasks.txt","r")
    task_list = task_file.readlines()
    task_file.close()
    total_tasks = len(task_list)
    user_file = open("user.txt","r")
    user_list = user_file.readlines()
    user_file.close()
    total_users = len(user_list)
    
    stats = [str(total_users) + "\n", str(total_tasks) + "\n"]
    
    for user in user_list:
        user = user.split(", ")[0]
        user_tasks = 0
        completed =  0
        due_incomplete = 0
        user_stats = [user + ","]
        complete_100 = 0
        incomplete_100 = 0
        due_incomplete_100 = 0
        
        # loop counts user tasks.
        for task in task_list:
            if task.startswith(user) == True:
                user_tasks += 1
                due_date  = str_int(task.split(", ")[3].split("/"))
                date_now = str_int(date.datetime.now().strftime("%x").split("/"))

                # users task completion check.
                if task.strip("\n").endswith("Yes") == True:
                    completed += 1
                
                # checks if incomplete task is overdue.
                else:
                    for day in reversed(range(3)):
                        overdue = date_now[day] > due_date[day]
                        if overdue == True:
                            due_incomplete += 1
                            break
                    
        task_100 = round((user_tasks/total_tasks)*100,2)
        
        if user_tasks > 0:
            complete_100 = round((completed/user_tasks)*100,2)
            incomplete_100 = 100 - complete_100
            due_incomplete_100 = round((due_incomplete/user_tasks)*100,2)
            
        
        
        stat_list = [str(user_tasks),str(task_100), str(complete_100), str(incomplete_100),
                     str(due_incomplete_100)]
        stat_list = ",".join(stat_list) + "\n"

        user_stats += stat_list
        stats += user_stats
        
    with open("user_overview.txt","w") as u_ov:
        u_ov.writelines(stats)

# Extraction of usernames and passwords     
u_file = open("user.txt", "r") 
userPASS = {}
p_words = []
user_l = u_file.readlines()

# Loop creates password list and, username : password dictionary.
for line in user_l:
    user = line.split(", ")[0:2]
    p_words.append(user[1].strip("\n"))
    userPASS[user[0]] = user[1].strip("\n")
    
u_file.close()
    

print("Login")
user_now = input("Username: ")
password = input("Password: ")



# loop check if user exists, or if password exists.
while userPASS.get(user_now) == None or p_words.count(password) == 0 or userPASS[user_now] != password:

    # Block asks user for the right username to match the password.
    if  p_words.count(password) > 0 and userPASS.get(user_now) == None:
        while userPASS.get(user_now) == None:
            print("\nUsername does not exist.")
            print("Enter the correct username.")
            user_now = input("Username: ")

    # Block checks if given password matches the existing usernames password.     
    if userPASS[user_now] != password:
        while userPASS[user_now] != password:
            print("You have entered the wrong password. Try again.")
            password = input("Password: ")
            
    # If both while conditions are false.         
    else:
        print("\nYou have entered the wrong username and password. Try again")
        user_now = input("Username: ")
        password = input("Password: ")
        
        
# Menu initialized.
menu1 = menu(user_now)
print("\n")


# menu block for a registered user.
while menu1 != "e":
     
    # Block that registers a user. Writes username and password input to user.txt. Exclusive to admin.
    if menu1 == "r":
        
        with open("user.txt", "a") as user_file:
            if user_now == "admin":
                reg_user(user_file, userPASS)
            else:
                print("\nOnly admin can register a user.")
                
        # Updates user list for statistics block use         
        u_file = open("user.txt", "r")
        user_list = u_file.readlines()
        u_file.close()

    # Block adds new task to task.txt.    
    elif menu1 == "a":
        
        with open("tasks.txt", "a") as task_file:
            assign = add_task()
            
            task_string = ", ".join(assign)
            task_file.write("\n" + task_string)
            
    # Block lets user view all tasks        
    elif menu1 == "va" :
         
         with open("tasks.txt", "r") as task_file:
             view_all(task_file)        
             print("\n" + "-"*45)
             
    # Block lets user view all their own tasks.             
    elif menu1 == "vm":
       
      print("\nYour tasks are: \n")
      view_mine(user_now)
                  
                  
    # Statistics block, exclusive to admin.              
    elif menu1 == "ds":
        if user_now == "admin":
            task_file = open("tasks.txt", "r") 
            total_tasks = len(task_file.readlines())
            task_file.close()
            user_file = open("user.txt", "r")
            total_users = len(user_file.readlines())
            user_file.close()
            print("Statistics")
            print("-"*11)
            print(f"\nTotal tasks: {total_tasks}\nTotal users: {total_users}")

        else:
         print("Only admin can view the statistics.")
         
    # Generate reports block, exclusiv to admin 
    elif menu1 == "gr":
        if user_now == "admin":
            task_overview()
            user_overview()
            user_ov = open("user_overview.txt", "r")
            user_report = user_ov.readlines()
            user_ov.close
            
            print(f"Total number of users : {user_report[0]}\n" + 
                  f"Total number of tasks : {user_report[1]}")
            
            space = " | "
            print("-"*115)
            # User stats table header.
            print(f"{'User':14s}{space}{'Total tasks':12s}{space}{'% out of all tasks':18s}{space}{'% of tasks done':15s}{space}{'% remaining tasks':17s}{space}{'% overdue & incomplete':22s} |")
            print("-"*115)
            for user in range(2,len(user_report)):
                user_stats = user_report[user].split(",")
                print(f"{user_stats[0]:14s}{space}{user_stats[1]:12s}{space}{user_stats[2]:18s}{space}{user_stats[3]:15s}{space}{user_stats[4]:17s}{space}{user_stats[5]:22s}")
                
            print("\n")
            task_ov = open("task_overview.txt", "r")
            task_report = task_ov.readlines()
            task_ov.close()
            print(f"{'Total number of tasks':37s}: {task_report[0]}\n" + 
                  f"{'Total number of completed tasks':37s}: {task_report[1]}\n" +
                  f"{'Total number of incomplete tasks':37s}: {task_report[2]}\n" +
                  f"{'Total of incomplete and overdue tasks':37s}: {task_report[3]}\n" +
                  f"{'Percent of incomplete tasks':37s}: {task_report[4]}" +
                  f"{'Percent of overdue tasks':37s}: {task_report[5]}")
                 
    menu1 = menu(user_now)
        
                          
                   
                  
              
              
                     
                     
             
                        
            
                
                                   
                
        
            
            
        
        
