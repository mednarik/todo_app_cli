#show the user all the already added tasks and give a small controls menu below it (add task, remove task)


import json, os, time
from datetime import datetime

def show_tasks():
   if data["tasks"] == []:
      print("No tasks have been added yet")
      return False
   else:
      for i in range(len(data["tasks"])):
         print(str(i+1) + ". " + data["tasks"][i]["name"])
      return True
   

def add_task():
   #enter the task's name
   print("\nNew task:")
   name = input(">>> ")
   file_name = name.lower().replace(" ","_").replace("ä", "ae").replace("ö", "oe").replace("ü", "ue") + ".txt"

   now = datetime.now()
   now = now.strftime("%Y-%m-%d %H:%M:%S")

   data["tasks"].append({"name": name, "file": file_name, "date":now})

   

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
            if 0 <= index < len(data["tasks"]):
               os.remove(f"task_files/{data["tasks"][index]["file"]}")
               data["tasks"].pop(index)
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

         item = data["tasks"][index]

         #highlight it somehow
         while True:
            os.system("cls")
            for i in range(len(data["tasks"])):
               if i == index:
                  print(f"\033[1;43m{str(i+1)}. {data['tasks'][index]['name']}\033[0m")
               else:
                  print(str(i+1) + ". " + data["tasks"][i]["name"])
            print("\nUse 'W' to move up and 'S' to move down / press enter only to stop")
            
            action = input(">>> ")

            if action == "":
               break

            elif action.lower() == "w" and 0 < index:
            
               data["tasks"].pop(index)
               index -= 1
               data["tasks"].insert(index, item)
               

            elif action.lower() == "s" and index < len(data["tasks"]) - 1:
               
               data["tasks"].pop(index)
               index += 1
               data["tasks"].insert(index, item)
      except Exception:
         input("Not a valid index...")

         with open("data.json", "w") as f:
               json.dump(data, f, indent=4)

def view_task():
   if(show_tasks()):
      print("Enter the index of the task you want to view:")
      try:
         index = int(input(">>> ")) - 1
         file = data["tasks"][index]["file"]

         with open(f"task_files/{file}", "r") as f:
            print(f.read())

         extra = input(">>> ")
         with open(f"task_files/{file}", "a") as f:
            f.write(extra)
      except Exception:
         input("Not a valid index...")
         
         

      
         
         
#load the file
with open("data.json", "r") as f:
   data = json.load(f)


#handle the controls
while True:
   os.system("cls")
   #print the content
   show_tasks()

   print("\nControls:")
   print("Enter 1 to add a task")
   print("Enter 2 to remove a task")
   print("Enter 3 to quit the program")
   print("Enter 4 to change the order")
   print("Enter 5 to view a task")
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
      
   else:
      input("Not a valid action...")






