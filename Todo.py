username=input("Enter Your Username")

while username!="Admin":
    print("Invalid Username")
    username = input("Enter Your Username:-")
else:
    password=input("Enter Your Password")

    while password!="abc":
        print("Password denied Pls Re-enter Your Password")
        password = input("Enter Your Password")

    else:
        name=input("Enter Your Name")
        print(f"Welcome Mr./Miss {name}")

todos=[]
while True:
    print("\nType \"add\" to add a todos")
    print("Type \"show\" to view your todos")
    print("Type \"del\" to delete one of your todo")
    print("Type \"exit\" to exit the application\n")
    user_action=input("Enter Your action:-")

    match user_action:
        case "add":
            todo=input("Enter a todo:-")
            todos.append(todo.capitalize())
            print("Todo added successfully \n")
        case "show":
            print("Your Todos has following activies")
            print(todos)
            print("\n")
        case "del":
            delete=input("Enter the todo to remove it")
            todos.remove(delete.capitalize())
            print(f"{delete.capitalize()} removed successfully \n")
        case "exit":
            break

print("Goodbye")
