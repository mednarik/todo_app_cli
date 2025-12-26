import json, os, time
from datetime import datetime

#load the file
with open("data.json", "r") as f:
   data = json.load(f)


toDoList = data["toDo"]
doneList = data["done"]

underline_bold = "\033[1;4m"
reset = "\033[0m"



def show_tasks():
   max_rows = max(len(toDoList), len(doneList))
   tab = 50

   print(f"{underline_bold}{f"To Do":<{tab}}{f"|Done":<{tab}}{reset}")

   if toDoList == []:
      todo_text = "No tasks have been added yet"
   else:
      todo_text = f"1. {toDoList[0]['name']}"

   if doneList == []:
      done_text = "No tasks have been completed yet"
   else:
      done_text = doneList[0]["name"]

   print(f"{todo_text:<{tab}}|{done_text}")
   
   for i in range(1, max_rows):
      if i < len(toDoList):
         todo_text = f"{i+1}. {toDoList[i]['name']}"
      else:
         todo_text = ""
      
      if i < len(doneList):
         done_text = doneList[i]["name"]
      else:
         done_text = ""
      
      print(f"{todo_text:<{tab}}|{done_text}")

   return bool(toDoList)

   

def add_task():
   #enter the task's name
   print("\nNew task:")
   name = input(">>> ")


   now = datetime.now()
   now = now.strftime("%Y-%m-%d %H:%M:%S")

   toDoList.append({"name": name, "description": "", "date":now, "subtasks":[]})

   
   #add the data to the json file
   with open("data.json", "w") as f: 
      json.dump(data, f, indent=4)
      

def remove_task():
   if(show_tasks()):
      
      while True:
         try:
            index = int(input(">>> ")) - 1
            if 0 <= index < len(toDoList):
               toDoList.pop(index)
               break
            
            else:
               input("Not a valid index...")

         except Exception:
            input("Not a valid index...")

      with open("data.json", "w") as f:
         json.dump(data, f, indent=4)

def change_order():
   #show the tasks
   if(show_tasks()):


      #enter the number of the task to move
      print("Enter the index of the task you want to move:")
      index = input(">>> ")
      
      try:
         index = int(index) - 1 

         item = toDoList[index]

         #highlight it somehow
         while True:
            os.system("cls")
            for i in range(len(toDoList)):
               if i == index:
                  print(f"\033[1;43m{str(i+1)}. {data['toDo'][index]['name']}\033[0m")
               else:
                  print(str(i+1) + ". " + toDoList[i]["name"])
            print("\nUse 'W' to move up and 'S' to move down / press enter only to stop")
            
            action = input(">>> ")

            if action == "":
               break

            elif action.lower() == "w" and 0 < index:
            
               toDoList.pop(index)
               index -= 1
               toDoList.insert(index, item)
               

            elif action.lower() == "s" and index < len(toDoList) - 1:
               
               toDoList.pop(index)
               index += 1
               toDoList.insert(index, item)
      except Exception:
         input("Not a valid index...")

         with open("data.json", "w") as f:
               json.dump(data, f, indent=4)

def add_subtasks():
   if(show_tasks()):
      print("Enter the index of the task you want to add a subtask to:")
      try:
         index = int(input(">>> ")) - 1

         os.system("cls")


         with open("data.json", "w") as f:
            json.dump(data, f, indent=4)

      except IndexError:
         input("Not a valid index...")
         
def move_to_doneList():
   if(show_tasks()):
      print("Enter the index of the task you have competed:")
      index = int(input(">>> ")) - 1
      doneList.append(toDoList[index])
      toDoList.pop(index)

      with open("data.json", "w") as f:
         json.dump(data, f, indent=4)
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
   print("Enter 5 to add a subtask")
   print("Enter 6 to move a task from To Do to Done")
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
      add_subtasks()
   
   elif action =="6":
      os.system("cls")
      move_to_doneList()
      
   else:
      input("Not a valid action...")






