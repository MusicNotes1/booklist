import json
TEMPLATE = """Name: {}
Author: {}
Status: {}"""
#Imports a previous book list from the database.json file, if it exists
with open("database.json", "r") as file:
    books = json.load(file)

#Updates the database.json file with some content
def UpdateJson(content):
    with open("database.json", "w") as file:
        json.dump(content, file)

#Ask for all the detail, appends them to the list and runs the UpdateJson function
def AddBook():
    book_name = input("Enter the books name: ")
    book_author = input("Enter books author: ")
    book_read = input("Have you already read the book (y or n)? ")
    if book_read.lower() == "y":
        book_read = True
    else:
        book_read = False
    books.append({"name": book_name, "author": book_author, "status": book_read})
    UpdateJson(books)

#Removes a book from the list
def RemoveBook():
    user_input = input("Which book: ").lower()
    for index, book in enumerate(books):
        if book["name"].lower() == user_input:
            del books[index]
            UpdateJson(books)
            return
    raise ValueError

#Shows all books with their respective number
def All():
    for index, book in enumerate(books, start=1):
        read = None
        if book["status"] == True:
            read = "Read"
        else:
            read = "Not Read"
        string = TEMPLATE.format(book["name"], book["author"], read)
        print(f"Number {index}\n{string}\n")

#Shows a specific book or all books
def ShowBook():
    user_input = input('Which Book (type "all" for all the books): ').lower()
    for book in books:
        read = None
        if book["status"] == True:
            read = "Read"
        else:
            read = "Not Read"
        #NOTE: Probably their is a better way to do this, but I can't figure out how to print all books without the All function :/
        if book["name"].lower() == user_input and user_input != "all":
            print(TEMPLATE.format(book["name"], book["author"], read))
            return
        elif user_input == "all":
            All()
            return
        raise ValueError

#Changes the status key to True from a specific book
def ReadBook():
    user_input = input("Which Book: ").lower()
    for book in books:
        if book["name"].lower() == user_input:
            book["status"] = True
            UpdateJson(books)
            return
    raise ValueError
