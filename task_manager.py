# Date: 2021 - 09 - 13

# Author: Njabulo Nxumalo

# Purpose: Create a task manager that will read and write tasks to a text file. Allow admin user to register users,
# by writing them to a text file. Allow logged in users to add tasks, view own tasks or all tasks.

import datetime as date

print("Login")
user_now = input("Username: ")
password = input("Password: ")


u_file = open("user.txt", "r") 
userPASS= {}
p_words = []
user_l = u_file.readlines()

# Loop creates password list and, username : paasword dictionary.
for line in user_l:
    user = line.split(", ")[0:2]
    p_words.append(user[1].strip("\n"))
    userPASS[user[0]] = user[1]
    
u_file.close()

# loop check if user exists, or if password exists.
while userPASS.get(user_now) == None or p_words.count(password) == 0:

    # Block asks user for the right username to match the password.
    if  p_words.count(password) > 0 and userPASS.get(user_now) == None:
        while userPASS.get(user_now) == None:
            print("\nUsername does not exist.")
            print("Enter the correct username.")
            user_now = input("Username: ")

    # Block checks if given password matches the existing usernames password.     
    elif userPASS[user_now] != password:
        while userPASS[user_now] != password:
            print("You have entered the wrong password. Try again.")
            password = input("Password: ")
            
    # If both while conditions are false.         
    else:
        print("\nYou have entered the wrong username and password. Try again")
        user_now = input("Username: ")
        password = input("Password: ")
        
# Menu initialized.
menu = input("\nPlease select one of the following options: \n r  - register user " +
             "\n a  - add task \n va - view all tasks \n " +
             "vm - view my tasks \n s - statistics (admin only) \n e  - exit \n\n" )

# menu block for a registered user.
while menu != "e":
     
     
    # Block that registers a user. Writes username and password input to user.txt. Exclusive to admin.
    if menu == "r":
        with open("user.txt", "a") as u_file:
            if user_now == "admin":
                username = input("Username: ")
                password = input("Password: ")
                confirm = input("Confirm password: " + "\n" )
                
                while confirm != password:
                     confirm = input("\nInput does not match password"+ "\n" +
                                     "\n" + "Confirm password: ")
                
                u_file.write(f"\n{username}" + ", " + f"{password}")
            else:
                print("\nOnly admin can register a user.")
                
        u_file = open("user.txt", "r")
        user_l = u_file.readlines()
        u_file.close()

        
    elif menu == "a":
        # Block adds new task to task.txt.
        with open("tasks.txt", "a") as t_f:
            assign = ["Username: ", "Title of the task: " , "Task description: ",
                      "Due date (DD/MM/YYYY): ", date.datetime.now().strftime("%x"),  "No" ]
            
            for value in range(len(assign)):
                # if statement automatically assigns date and task status.
                if value == 4 or value == 5:
                    assign[value] = assign[value]
                else:
                    assign[value] = input(assign[value])

            task_str = ", ".join(assign)
            t_f.write("\n" + task_str)
            
    elif menu == "va" :
         # Block lets user view all tasks. 
         with open("tasks.txt", "r") as t_file:
             for line in t_file.readlines():
                 line_l = line.split(", ")
                 print("-"*35)
                 table = [f"\nAssigned to: {line_l[0]}", f"Task: {line_l[1]}",
                          f"Task description: {line_l[2]}", f"Due date: {line_l[3]}",
                          f"Date created: {line_l[4]}", f"Completion status: {line_l[5]}"]

                 for value in table:
                     print(value)
                     
             print("\n" + "-"*35)
                 
    elif menu == "vm":
      # Block lets user to view all their own tasks. 
      with open("tasks.txt", "r") as t_file:
          print("\nYour tasks are: \n")
          num_tasks = 0

          # Block checks for users tasks, then prints them.         
          for line in t_file.readlines():
              string = line.split(", ")
              if user_now == string[0]:
                  num_tasks += 1
                  print(f"Task Title: {string[1]}")
                  
          if num_tasks == 0:
              print("You currently have no tasks assigned to you.")
                  
                  
    # Statistics block, exclusive to admin.              
    elif menu == "s":
        if user_now == "admin":
            with open("tasks.txt", "r") as t_file:
                 total_tasks = len(t_file.readlines())
                 total_users = len(user_l)
                 print(f"\nTotal of tasks : {total_tasks}\nTotal of users: {total_users}")

        else:
         print("Only admin can view the statistics.")
         
    menu = input("\nPlease select one of the following options: \n r  - register user " +
             "\n a  - add task \n va - view all tasks \n " +
                 "vm - view my tasks \n s - statistics (admin only) \n e  - exit \n\n"  )
        
                          
                   
                  
              
              
                     
                     
             
                        
            
                
                                   
                
        
            
            
        
        
