#Main interface (20231282-S.S.Rajendra)
# Initialize variables

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
  print("\n   1) Add a new project to existing projects.")
  print("   2) Remove a completed project from existing projects.")
  print("   3) Add new workers to available workers group.")
  print("   4) Update details on ongoing projects.")
  print("   5) Project Statistics")
  print("   6) Exit")

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
    # choice selected is invalid
    print("choice selected is invalid")

  # 2nd figure ICW program

def add_new_project():
  # Get the new project details from the user.
  print("\n----------------XYZ company----------------")
  print("             Add a new project               ")
  project_code = int(input("\nproject code: "))
  if project_code == 0:
    return main()
  client_name = str(input("\nclient name: "))
  from datetime import date 
  start_date = input("start date (DD/MM/YYYY): ")
  expected_end_date = input("expected end date (DD/MM/YYYY): ")
  number_of_workers = int(input("number of workers: "))
  project_status = str(input("project status (ongoing, on hold, or completed): "))
  if (project_status == "completed"):
     input("Actual end date (DD/MM/YYYY): ")
  # Prompt the user to save the project
  Do_you_want_to_save_the_project = str(input("\nDo you want to save the project (yes/no)?: "))
  # Save the new project if user wants to.
  if (Do_you_want_to_save_the_project == "yes"):
     print("The new project has been added.")
  else :
     print("The new project has not been added.")
  
   # 3rd figure ICW program

def remove_completed_project():
    # Get the existing project details from the user.
    print("\n----------------XYZ company----------------")
    print("          Remove Completed Project         ")
    project_code = int(input("\nproject code: "))
    Do_you_want_to_remove_the_project = str(input("do you want to remove the project (yes/no)?: "))
    # Remove the existing project if user wants to.
    if (Do_you_want_to_remove_the_project == "yes"):
        print("The existing project has been removed.")
    else:
       print("The project has not been removed.")
   
    # 4th figure ICW program

def add_new_workers():
    # Identify how many workers to add.
    print("\n----------------XYZ company----------------")
    print("              Add new workers              ")
    number_workers_to_add = int(input("\nnumber of workers to add: "))
    # Prompt the user to add workers or not.
    Do_you_want_to_add = str(input("do you want to add (yes/no)?: "))
    # Add the new workers if the user wants to.
    if (Do_you_want_to_add == "yes"):
        print("New workers have been added.")
    else:
       print("New workers have not been added.")

    # 5th figure ICW program

def update_ongoing_projects():
    # Ask which project needs to be updated.
    print("\n----------------XYZ company----------------")
    print("           Update Project details          ")
    Project_update_code = int(input("\nEnter project code: "))
    if Project_update_code == 0:
       main()
    Client_name = str(input("\nClient name: "))
    Start_date = str(input("start date (DD/MM/YYYY): "))
    Expected_end_date = str(input("expected end date (DD/MM/YYYY): "))
    Number_of_workers = int(input("number of workers: "))
    project_status_2 = str(input("project status (ongoing, on hold, or complete): "))
    if (project_status_2 == "completed"):
      input("Actual end date (DD/MM/YYYY): ")
    # Prompt the user to update the project details or not.
    Do_you_want_to_update_details = str(input("\ndo you want to update project details (yes/no)?: "))
    # Update the ongoing project if the user wants to.
    if (Do_you_want_to_update_details == "yes") :
        print("The project has been updated.")
    else:
        print("The project is not updated.")

    # 6th figure ICW program

def project_statistics():
    #Get the project statistics from user.
    print("\n----------------XYZ company----------------")
    print("               Project statistics            ")
    number_of_ongoing_projects = int(input("\nenter the num of ongoing projects: "))
    number_of_on_hold_projects = int(input("enter the number of on hold projects: "))
    number_of_available_workers_to_assign = int(input("number of workers available: "))
    # saving the project
    do_you_want_to_add_the_project = str(input("\ndo you want to add the project (yes/no)?:"))
    # Ask if the user wants to update project stats.
    if (do_you_want_to_add_the_project == "yes"):
        print("project statistics have been updated.") 
    else:
        print("project statistics have not been updated.")

def exit_program():
    print("      Exiting the program...")
     

if __name__ == "__main__":
  main()

                                 
                                     
    
    
    
        
        

    
    



    
