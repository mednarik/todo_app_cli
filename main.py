import json, os, time
from datetime import datetime

#load the file
with open("data.json", "r") as f:
   data = json.load(f)

toDoList = data["toDo"]
doneList = data["done"]

def show_tasks():
   tab_space = 30

   print(f"\033[4mTo Do\033[0m{"|\033[4mDone\033[0m":>{tab_space+8}}")
   if toDoList == []:
      if doneList == []:
         print(f"No tasks have been added yet{"|":>{tab_space-27}}", end="")
         print(f"No tasks have been added yet")

      else:
         print(f"No tasks have been added yet{"|":>{tab_space-27}}", end="")
         print(doneList[0]["name"])
         for i in range(1, len(doneList)):
            print(f"{"":>{tab_space}}|", end="")
            print(doneList[i]["name"])
      return False

   else:
      if doneList == []:
         print(f"{f"{str(1)}. {toDoList[0]['name']}":<{tab_space}}|No tasks have been added yet")
         for i in range(1, len(toDoList)):
            print(f"{f"{str(i+1)}. {toDoList[i]['name']}":<{tab_space}}|")
      else:
         if len(toDoList) >= len(doneList):
            for i in range(len(doneList)):
               print(f"{f"{str(i+1)}. {toDoList[i]['name']}":<{tab_space}}|{doneList[i]["name"]}")
            for i in range(len(toDoList) - len(doneList)):
               print(f"{f"{str(i+1)}. {toDoList[i]['name']}":<{tab_space}}|")
         else:
            for i in range(len(toDoList)):
               print(f"{f"{str(i+1)}. {toDoList[i]['name']}":<{tab_space}}|{doneList[i]["name"]}")
               for i in range(len(doneList) - len(toDoList)):
                  print(f"{"":<{tab_space}}|{doneList[i]["name"]}")

         return True
   

def add_task():
   #enter the task's name
   print("\nNew task:")
   name = input(">>> ")
   file_name = name.lower().replace(" ","_").replace("ä", "ae").replace("ö", "oe").replace("ü", "ue") + ".txt"

   now = datetime.now()
   now = now.strftime("%Y-%m-%d %H:%M:%S")

   toDoList.append({"name": name, "file": file_name, "date":now})

   

   #add a description txt file to the task_files directory
   with open(f"task_files/{file_name}", "w") as f:
      f.write(f"{now}\n\n")

   
   
   #add the data to the json file
   with open("data.json", "w") as f: 
      json.dump(data, f, indent=4)
      

def remove_task():
   if(show_tasks()):
      
      while True:
         try:
            index = int(input(">>> ")) - 1
            if 0 <= index < len(toDoList):
               os.remove(f"task_files/{toDoList[index]["file"]}")
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

def view_task():
   if(show_tasks()):
      print("Enter the index of the task you want to view:")
      try:
         index = int(input(">>> ")) - 1
         file = toDoList[index]["file"]

         os.system("cls")
         with open(f"task_files/{file}", "r") as f:
            print(f.read())

         extra = input(">>> ")
         with open(f"task_files/{file}", "a") as f:
            f.write(extra)
      except Exception:
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

   print("\n\033[4mControls\033[0m")
   print("Enter 1 to add a task")
   print("Enter 2 to remove a task")
   print("Enter 3 to quit the program")
   print("Enter 4 to change the order")
   print("Enter 5 to view a task")
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
      view_task()
   
   elif action =="6":
      os.system("cls")
      move_to_doneList()
      
   else:
      input("Not a valid action...")






