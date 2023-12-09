#Main interface (20231282-S.S.Rajendra)

ongoing = [[] for _ in range(46)]
onhold = [[] for _ in range(46)]
completed = [[] for _ in range(46)]

#List for the data entries
projectEntry = []

ongoingProjects = []
onholdProjects = []
completedProjects = []

# Initialize variables
workers = 0
code = 0

def add_new_project():
  print("Add a new project to existing projects.")

def remove_completed_project():
  print("Remove a completed project from existing projects.")

def add_new_workers():
  print("Add new workers to available workers group.")

def update_ongoing_projects():
  print("Update details on ongoing projects.")

def project_statistics():
  print("Display project statistics.")

def exit_program():
  print("Exit the program.")

def main():
  # Display the main menu panel.
  print("----------------XYZ Company----------------")
  print("                 Main Menu                 ")
  print("\n1) Add a new project to existing projects")
  print("2) Remove a completed project from existing projects")
  print("3) Add new workers to available workers group")
  print("4) Update details on ongoing projects")
  print("5) Project Statistics")
  print("6) Exit")


  # Identify User's choice.
  choice = input("                                        Your Choice: ")

  # Refer to user's choice.
  if choice == "1":
    add_new_project()
  elif choice == "2":
    remove_completed_project()
  elif choice == "3":
    add_new_workers()
  elif choice == "4":
    update_ongoing_projects()
  elif choice == "5":
    project_statistics()
  elif choice == "6":
    exit_program()
  else:
      main()

  # 2nd figure ICW program

def add_new_project():  
  # Get the new project details from the user.
  print("\n----------------XYZ company----------------")
  print("             Add a new project               ")
  code = int(input("\nEnter project code **'0' to exit : "))
  if code == 0:
    return main()
  if code > 0 :
    projectEntry.append(code)
  else:
    add_new_project()

  client_name = str(input("\nclient name: "))
  projectEntry.append(client_name)

  start_date = input("start date (DD/MM/YYYY): ")
  projectEntry.append(start_date)

  expected_end_date = input("expected end date (DD/MM/YYYY): ")
  projectEntry.append(expected_end_date)

  number_of_workers = int(input("number of workers: "))
  projectEntry.append(number_of_workers)

  project_status = str(input("project status (ongoing, on hold, or completed): "))
  projectEntry.append(project_status)
  
  if (project_status == "completed"):
     input("Actual end date (DD/MM/YYYY): ")

  # Prompt the user to save the project
  Save_project = str(input("\nDo you want to add the project (Y/N)?: "))
  
  #save the project if user wants to.
  if Save_project == "Y":
    
   if project_status == ("ongoing"):
    ongoing[code] = projectEntry
    ongoingProjects.append(code)
    
   elif project_status == ("onhold"):
    onhold[code] = projectEntry
    onholdProjects.append(code)

   elif project_status == ("completed"):
    completed[code] = projectEntry
    completedProjects.append(code)

   print("The new project has been added.")
   return main()

  if Save_project == "N":
   print("An error occured!")
   return main()
    
   # 3rd figure ICW program


def remove_completed_project():
  # Get the existing project details from the user.
  print("\n----------------XYZ company----------------")
  print("          Remove Completed Project         ")
  project_code = int(input("\nproject code: "))
  # Remove the existing project if user wants to.
  removethe_project = str(input("Do you want to remove the project (Y/N)?:"))
  if removethe_project == "Y":
   if project_code in ongoingProjects:
    print(ongoing)
    ongoing[project_code]=[]
    del(ongoingProjects[code])
    print
    print("press enter key to enter main menu...")
    input(completed)
    return main()
  
   elif project_code in onholdProjects:
    print(onhold)
    onhold[project_code]=[]
    del(onholdProjects[code])
    print
    print("press enter key to enter main menu...")
    input(onhold)
    return main()
    
  else:
    print("error occured while removing project!")
    return main()
   
    # 4th figure ICW program

def add_new_workers():  # sourcery skip: extract-duplicate-method
    # Identify how many workers to add.
    global workers
    print("\n----------------XYZ company----------------")
    print("              Add new workers              ")
    workersto_add = int(input("\nnumber of workers to add ('0' to exit): "))
    if workersto_add == '0':
     return main()
    elif workersto_add > 0:
     workersto_add += workersto_add
     print("Workers added succesfully")
     print("press enter key to enter main menu...")
     input()
     return main()
    else:
     print ("Not enough workers")
     print("press enter key to enter main menu...")
     input()
     add_new_workers
     return workersto_add

    # 5th figure ICW program

def update_ongoing_projects():
    # Ask which project needs to be updated.
    print("\n----------------XYZ company----------------")
    print("           Update Project details          ")
    Project_update_code = int(input("\nEnter project code (1-25) '0' to exit: "))
    if Project_update_code == 0:
       main()
    if Project_update_code in ongoingProjects:
      ongoing[Project_update_code][0] = Project_update_code
    elif Project_update_code in onholdProjects:
      onhold[Project_update_code][0] = Project_update_code
    elif Project_update_code in completedProjects:
      completed[Project_update_code][0] = Project_update_code
    else:
      print ("Project not found!")
      return main()
    
    Client_name = str(input("\nClient name: "))
    projectEntry.append(Client_name)

    start_date = input("start date (DD/MM/YYYY): ")
    projectEntry.append(start_date)

    expected_end_date = input("expected end date (DD/MM/YYYY): ")
    projectEntry.append(expected_end_date)

    number_of_workers = int(input("number of workers: "))
    projectEntry.append(number_of_workers)

    status = str(input("project status (ongoing, on hold, or completed): "))
    projectEntry.append(status)
    
    # Prompt the user to update the project details or not.
    update_details = str(input("\nDo you want to update project details (Y/N)?: "))
    # Update the ongoing project if the user wants to.
    if (update_details == "Y"):
      if status == "ongoing":
        ongoing[Project_update_code] = projectEntry
        ongoingProjects.append(Project_update_code)
        if Project_update_code in completedProjects:
          completedProjects.remove(Project_update_code)
          completed[Project_update_code] = []
        if Project_update_code in onholdProjects:
          onholdProjects.remove(Project_update_code)
          onhold[Project_update_code] = []
          print("The project has been updated.")
          
      elif status == "onhold":
       
        onhold[Project_update_code] = projectEntry
        onholdProjects.append(Project_update_code)
        if Project_update_code in ongoingProjects:
          ongoingProjects.remove(Project_update_code)
          ongoing[Project_update_code] = []
        if Project_update_code in completedProjects:
          completedProjects.remove(Project_update_code)
          completed[update_details] = []
          print("The project has been updated.")

      elif status == "completed":
       
        completed[Project_update_code] = projectEntry
        completedProjects.append(Project_update_code)
        if Project_update_code in ongoingProjects:
          ongoingProjects.remove(Project_update_code)
          ongoing[Project_update_code] = []
        if Project_update_code in onholdProjects:
          onholdProjects.remove(Project_update_code)
          onhold[Project_update_code] = []

          print("The project has been updated.")
    else:
        print("The project is not updated.")
    return main()

    # 6th figure ICW program

def project_statistics():
    #Get the project statistics from user.
    print("\n----------------XYZ company----------------")
    print("               Project statistics            ")
    #print the stats
    print(f"\n - Number of ongoing projects: {len(ongoingProjects)}")
    print(f" - Number of on-hold projects: {len(onholdProjects)}")
    print(f" - Number of complete projects: {len(completedProjects)}")
    availableworkers = ("workers - number_of_workers")
    print(f" - Number of available workers: {workers}")
    # saving the project
    exit_gate = str(input("\nEnter '0' to exit: "))
    if exit_gate == '0':
      return main()


def exit_program():
    print("   Exiting the program...")
    return main()
     
if __name__ == "__main__":
  main()