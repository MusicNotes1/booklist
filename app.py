import database
help = """Add: adds a new book
Read: Marks book as read
Select: Selects a book
Delete: Deletes a book
Quit: Quits the program
"""
options = {"add": database.AddBook,
           "read": database.ReadBook,
           "select": database.ShowBook,
           "delete": database.RemoveBook
           }

def menu():
    #Basic Menu (Not much to say here)
    user_input = input("Enter a command (press h for help): ").lower()
    while(user_input != "quit"):
        if user_input in options:
            function = options[user_input]
            try:
                function()
            except ValueError:
                print("Book Not Found!")
        elif user_input == "h":
            print(help)
        else:
            print("Unknown Command!")
        user_input = input("Enter a command (press h for help): ").lower()

menu()