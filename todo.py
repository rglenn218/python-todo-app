# List to store all tasks
tasks = []

# Display the menu options
def show_menu():
    print("\nWelcome to the To-Do List App!")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Exit")
    
# Add a new task to the list    
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")
    
# Display all tasks in the list    
def view_tasks():
    if len(tasks) == 0:
        print("You have no tasks to view.")
    else:
        print("\nYour tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Delete a task from the list
def delete_task():
    if len(tasks) == 0:
        print("You have no tasks to delete.")
    else:
        view_tasks()
        
        try:
            task_number = int(input("Enter the task number to delete: "))
            deleted_task = tasks.pop(task_number - 1)
            print(f'"{deleted_task}" was deleted.')
        
        except ValueError:
            print("Please enter a valid number.")
        
        except IndexError:
            print("That task does not exist.")
            
        else:
            print(f'"{deleted_task}" was deleted.')
        
        finally: 
            print("Delete action complete.")
            
# Run the main program loop
def main():
    while True:
        show_menu()
        choice = input("Choose an option:")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")
            
main()