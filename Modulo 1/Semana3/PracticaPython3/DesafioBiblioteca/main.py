#Desafio biblioteca

books_list:list = []

def add_books(title:str="",author:str="",genre:str="",publish_year:int=0,copies:int=0,repo_price:float=0)->list:
    for book in books_list:
        if book["title"].lower() == title.lower():
            print("Error: This book has already been added.")
            return books_list
        
    books_list.append({"title":title,"author":author,"genre":genre,"publish year":publish_year,"copies":copies,"repo_price":repo_price})
    print(f"The book was added!\n")
    return books_list

def books_validations(books_list:list)->list:
    for book in books_list:
        if book["publish year"] > 2024 or book["publish year"] < 1800:
            print(f"Error: Books can't register in the date {book["publish year"]}")
            books_list.remove(book)
            return books_list
        
        if book["repo_price"] < 0:
            print(f"Error: Book's reposition price must be a positive value.")
            books_list.remove(book)
            return books_list
        
        if book["copies"] < 0:
            print(f"Error: Book copies must be a positive value.")
            books_list.remove(book)
            return books_list
    

def search_books(title:str="")->None:
    for book in books_list:
        if book["title"].lower() == title.lower():
            print(f"The book {book["title"]} was found in the database.")
            if book["copies"] <= 0:
                print(f"{book["title"]} is not available at the moment.")
                break
            else:
                print(f"The book {book["title"]} is currently available.")
                break
    else:
        opc:str = input(f"The book {title} was not found. Would you like to register it?: ")
        if opc == "no":
            return
        elif opc == "yes":
            books_validations(add_books(input("title: "), input("author: "),input("genre: "), int(input("published year: ")), int(input("copies: ")), float(input("reposition price: "))))
            return
        else:
            print(f"option {opc} not recognized. Going back to menu.")

def update_book_prices(title:str="",copies:int=0,repo_price:float=0)->None:
    try:
        if copies > 0:  
            for book in books_list:
                if book["title"].lower() == title.lower():
                    book["copies"] = copies
                    book["repo_price"] = repo_price
                    print(f"the book {book["title"]} was updated with the new reposition price of {book["repo_price"]} and copies of {book["copies"]}")
                    break
            else:
                print(f"The book {title} was not found")
        else:
            print("Books need to be have more than 1 copy.")
    except:
        print("Error: Theres no books added in the inventory. Please add before updating prices.")

def remove_books(title:str="")->None:
    for book in books_list:
        if book["title"].lower() == title.lower():
            opc:str = input(f"The book {book["title"]} was found. Please enter the book's name again to remove it: ")
            if opc.lower() == book["title"].lower():
                print(f"The book {book["title"]} was removed.")
                books_list.remove(book)
                break
            else:
                print("Error: titles doesn't match. Book was not removed.")
                break
    else:
        print(f"The book {title} was not found.")

def books_report()->None:
    suma:float = 0
    for book in books_list:
        suma = (book["copies"] * book["repo_price"]) + suma

def main():
    print("Welcome to the Library!")
    while True:
        opc = int(input
('''
-------------------------------------------------
            Please select an option:
            1. add books
            2. search books
            3. update books reposition price and copies
            4. remove books
            5. show all books report
            6. exit menu
-------------------------------------------------
'''))
        if opc == 1:
            books_validations(add_books(input("title: "), input("author: "),input("genre: "), int(input("published year: ")), int(input("copies: ")), float(input("reposition price: "))))
        elif opc == 2:
            search_books(input("Book's name: "))
        elif opc == 3:
            books_validations(update_book_prices(input("Book's name: "), int(input("Update Invetory of copies: ")), float(input("Update reposition price: "))))
        elif opc == 4:
            remove_books(input("What book would you like to remove?: "))
        elif opc == 5:
            books_report()
        elif opc == 6:
            print("See you later!")
            break
        else:
            print("Error: Unknown option")


main()

