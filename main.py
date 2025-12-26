import json, os, time
from datetime import datetime

#load the file
with open("data.json", "r") as f:
   data = json.load(f)


doneList = data["done"]

underline_bold = "\033[1;4m"
reset = "\033[0m"

navigation_stack = [("root/",data["toDo"])]


def get_path() -> str: #returns the path
    path = []
    for level in navigation_stack:
        path.append(level[0])
    path = "".join(path)
    return path

def update_file():
   with open("data.json", "w") as f:
      json.dump(data, f, indent=4)

def show_tasks():
   current_level = navigation_stack[-1][1]
   max_rows = max(len(current_level), len(doneList))
   tab = 50


   print(f"{underline_bold}Path{reset}: {get_path()}")
   print()
   print(f"{underline_bold}{f"To Do":<{tab}}{f"|Done":<{tab}}{reset}")

   if current_level == []:
      todo_text = "No tasks have been added yet"
   else:
      todo_text = f"1. {current_level[0]['name']}"

   if doneList == []:
      done_text = "No tasks have been completed yet"
   else:
      done_text = doneList[0]["name"]

   print(f"{todo_text:<{tab}}|{done_text}")
   
   for i in range(1, max_rows):
      if i < len(current_level):
         todo_text = f"{i+1}. {current_level[i]['name']}"
      else:
         todo_text = ""
      
      if i < len(doneList):
         done_text = doneList[i]["name"]
      else:
         done_text = ""
      
      print(f"{todo_text:<{tab}}|{done_text}")

   return bool(current_level)

   

def add_task():
   #enter the task's name
   print("\nNew task:")
   name = input(">>> ")

   current_level = navigation_stack[-1][1]

   now = datetime.now()
   now = now.strftime("%Y-%m-%d %H:%M:%S")

   current_level.append({"name": name, "description": "", "date":now, "subtasks":[]})

   
   #add the data to the json file
   update_file()
      

def remove_task():
   if(show_tasks()):
      current_level = navigation_stack[-1][1]
      
      while True:
         try:
            index = int(input(">>> ")) - 1
            if 0 <= index < len(current_level):
               current_level.pop(index)
               break
            
            else:
               input("Not a valid index...")

         except Exception:
            input("Not a valid index...")

      update_file()

def change_order():
   #show the tasks
   if(show_tasks()):

      current_level = navigation_stack[-1][1]

      #enter the number of the task to move
      print("Enter the index of the task you want to move:")
      index = input(">>> ")
      
      try:
         index = int(index) - 1 

         item = current_level[index]

         #highlight it somehow
         while True:
            os.system("cls")
            for i in range(len(current_level)):
               if i == index:
                  print(f"\033[1;43m{str(i+1)}. {current_level[index]['name']}\033[0m")
               else:
                  print(str(i+1) + ". " + current_level[i]["name"])
            print("\nUse 'W' to move up and 'S' to move down / press enter only to stop")
            
            action = input(">>> ")

            if action == "":
               break

            elif action.lower() == "w" and 0 < index:
            
               current_level.pop(index)
               index -= 1
               current_level.insert(index, item)
               

            elif action.lower() == "s" and index < len(current_level) - 1:
               
               current_level.pop(index)
               index += 1
               current_level.insert(index, item)
      except Exception:
         input("Not a valid index...")

      update_file()
         

def open_task():
   if(show_tasks()):
      try:
            
         print("")
         print(f"\n{underline_bold}Controls{reset}")
         print('Enter the task index to go inside')
         print('Enter A/a to go back')
         user_input = input(">>> ")

         current_level = navigation_stack[-1][1]

         os.system("cls")

         

         if user_input.lower() == "a":
            if len(navigation_stack) > 1:
               navigation_stack.pop()
            else:
               input("Already at root level...")
         
         
         else:
            index = int(user_input) - 1
            task = current_level[index]
            navigation_stack.append((f"{task['name']}/", task["subtasks"]))

            

      except IndexError:
         input("Invalid index (Index out of range)...")

      except ValueError:
         input("Invalid index (Indices must be numbers)...")
         
def move_to_doneList():
   if(show_tasks()):
      current_level = navigation_stack[-1][1]
      print("Enter the index of the task you have competed:")
      index = int(input(">>> ")) - 1
      doneList.append(current_level[index])
      current_level.pop(index)

      update_file()

def clear_done():
   doneList.clear()
   update_file()

#handle the controls
while True:
   os.system("cls")
   #print the content
   show_tasks()

   print(f"\n{underline_bold}Controls{reset}")
   print("Enter 1 to add a task")
   print("Enter 2 to remove a task")
   print("Enter 3 to quit the program")
   print("Enter 4 to change the order")
   print("Enter 5 to open a task")
   print("Enter 6 to move a task from To Do to Done")
   print("Enter 7 to clear Done")
   action = input(">>> ")
   if action == "1":
      os.system("cls")
      add_task()
      
   elif action == "2":
      os.system("cls")
      remove_task()

   elif action =="3":
      break

   elif action =="4":
      os.system("cls")
      change_order()
   
   elif action =="5":
      os.system("cls")
      open_task()
   
   elif action =="6":
      os.system("cls")
      move_to_doneList()

   elif action =="7":
      os.system("cls")
      clear_done()
      
   else:
      input("Not a valid action...")






