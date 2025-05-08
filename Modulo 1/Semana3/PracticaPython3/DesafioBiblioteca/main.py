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
        elif opc == "si":
            add_books(input("title: "), input("author: "),input("genre: "), int(input("published year: ")), int(input("copies: ")), float(input("reposition price: ")))
            return
        else:
            print(f"option {opc} not recognized. Going back to menu.")

def update_book_prices(title:str="",copies:int=0,repo_price:float=0)->None:
    if copies < 0:  
        for book in books_list:
            if book["title"].lower() == title.lower():
                book["copies"] = copies
                repo_price["repo_price"] = repo_price
                print(f"the book {book["title"]} was updated with the new reposition price of {book["repo_price"]} and copies of {book["copies"]}")
            else:
                print(f"The book {book["title"]} was not found")
    else:
        print("Books need to be have more than 1 copy.")

def remove_books(title:str="")->None:
    for book in books_list:
        if book["title"].lower() == title.lower():
            opc:str = input(f"The book {book["title"]} was found. Please enter the books name again to remove it.")
            if opc.lower() == book["title"].lower():
                books_list.remove(book)
                break
            else:
                print("Error: Book titles doesn't match. Book was not removed.")
                break

def books_report()->None:
    pass

def main():
    add_books("vultures","kanye","edgy",2024,1,19000)
    add_books("808","kanye",":v",2008,0,19000)
    search_books("vultures")
    search_books("808")
    search_books("graduation")
    update_book_prices()
    print(books_list)

main()

