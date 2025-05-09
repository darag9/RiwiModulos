products:list = []  #Creation of the list of the products

#Method add_products which needs an input of a name, price and quantity, then it gets added as a dictionary to the list and returns the updated list

def add_products(name:str="",price:float=0,quantity:int=0)->list:
    
    for product in products:
        if product["name"] == name:
            print("Error: This item already exists")
            return products
    
    products.append({"name":name,"price":price,"quantity":quantity})
    print("\nProduct added!\n")
    return products

#Method consult_products which needs the input of a name, then it compares the key "name" in the list and prints the price and quantity of the product

def consult_products(name:str="")->None:
    for product in products:
        if product["name"].lower() == name.lower():
            print(f"The product {name} was found with a quantity of {product["quantity"]} each product with a price of {product["price"]}")
            break
    else:
        print("Error: the product was not found.")

#Method update_price which needs a name and a price, then it compares the key "name" in the list and replaces the value of the key "price" with the previous input of price

def update_price(name:str="",price:float=0)->None:
    for product in products:
        if product["name"].lower() == name.lower():
            product["price"] = price
            print(f"The new price for the product {name} is {product["price"]}")
            break
    else:
        print("Error: The product was not found.")

#Method remove_products which needs a name, then it compares the key "name" in the list and using the method .remove() it removes the iterated product

def remove_products(name:str="")->None:
    for product in products:
        if product["name"].lower() == name.lower():
            products.remove(product)
            break
    else:
        print("Error: The product was not found.")

def total_value()->str:

    total:float = sum(map(lambda t: t.get("price", 0) * t.get("quantity", 0), products))
    return f"The total price of the products is {total}"
    

#Method main where all the execution of the codes assembles with a cicle while un til the user presses the option 6 to exit the program

def main():
    print("Welcome to the store! Input an option to select the action required")
    while True:
        try:    
            opc = int(input(f'''
            1. add products
            2. consult list of products
            3. update price of a product
            4. remove products
            5. consult the total price of the products
            6. exit
            '''))
            
            if opc == 1:
                add_products(input("What product would you like to add?: "),float(input("What's the price going to be: ")),int(input("How many products will there be: ")))
            elif opc == 2:
                consult_products(input("What product would you like to consult?: "))
            elif opc == 3:
                update_price(input("What product would you like to update it's price?: "), float(input("How much will it cost?: ")))
            elif opc == 4:
                remove_products(input("What product would you like to remove?: "))
                print(f"The state of the products is: \n{products}")
            elif opc == 5:
                print(total_value())
            elif opc == 6:
                print("Thanks for passing by!")
                break
            else:
                print("\nPlease input an option")
        except ValueError:
            print("Error: The input Value is not supported. Please input a valid value.")
main()