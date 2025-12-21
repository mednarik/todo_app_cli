#show the user all the already added tasks and give a small controls menu below it (add task, remove task)

import json, os
 
def show_tasks():
   if data["tasks"] == []:
      print("No tasks have been added yet")
      return False
   else:
      for i, task in enumerate(data["tasks"]):
         print(str(i+1) + ". " + task)
      return True
   

def add_task():
   #enter the task's name
   print("\nNew task:")
   name = input(">>> ")


   data["tasks"].append(name)
   
   
   #add the data to the json file
   with open("data.json", "w") as f: 
      json.dump(data, f, indent=4)
      


def remove_task():
   if(show_tasks()):
      print("\nRemove Task (enter the index):")
      index = int(input(">>> ")) - 1

      while True:
         if index <= len(data["tasks"]):
            data["tasks"].pop(index)
            break
         else:
            input("Not a valid index...")

      with open("data.json", "w") as f:
         json.dump(data, f, indent=4)
      
         
   


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
   action = input(">>> ")
   if action == "1":
      os.system("cls")
      add_task()
      
   elif action == "2":
      os.system("cls")
      remove_task()
   elif action =="3":
      break
      
   else:
      input("Not a valid action...")






