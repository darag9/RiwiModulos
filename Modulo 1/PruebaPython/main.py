#Inventory test

#Main functionalities

'''
1. add products to inventory: Lets the user add products with atributes such as name, price and quantity.
2. consult products in the inventory: Searches any product depending on his name showing its details (name, price, quantity).
3. update prices of products: Modifies the price of an especific product in the inventory.
4. delete products in the inventory: Lets the user delete an unavailable product depeding on the name of the product.
5. Calculate the total value of the inventory: multiplies the price and the quantity of each product and shows the total value.
'''

#list of products

products:list = []

#add products

def add_products(name:str="",price:float=0,quantity:int=0)->list:   #main functionality 1
    if quantity > 0 and price > 0:
        for product in products:
            if product["name"].lower() == name.lower():
                print("Error: the product you just tried to add was already in the inventory.")
                return products
        products.append({"name":name,"price":price,"quantity":quantity})    #adds the product to the list "products" as a dictionary
        print("\nProduct added!")
        return products
    else:
        print("\nError: Product values must be positive.")

#consult products

def consult_products(name:str="")->None:    #main functionality 2
    for product in products:
        if product["name"].lower() == name.lower():
            print(f"\nThe product {product["name"]} was found.\nname: {product["name"]}\nprice: {product["price"]}\nquantity: {product["quantity"]}")
            break
    else:
        print(f"\nThe product {name} was not found in the inventory.")

#update prices

def update_prices(name:str="",price:float=0)->None:
    if price > 0:    
        for product in products:
            if product["name"].lower() == name.lower():
                product["price"] = price                #main functionality 3
                print(f"\nThe product {product["name"]} was updated with a new price: {product["price"]}")
                break
        else:
            print(f"\nThe product {name} was not found in the inventory.")
    else: print("\nError: Product prices must be positive.")

#delete products

def delete_products(name:str="")->None:     #main functionality 4
    for product in products:
        if product["name"].lower() == name.lower():
            print(f"The product {product["name"]} was found in the inventory. It will be deleted.")
            products.remove(product)    #removes the product from the list "products"
            break
    else:
        print(f"\nError: The product {name} was not found in the inventory.")


#total value

def total_value()->float:
    total:float = 0
    for product in products:
        total += product["price"] * product["quantity"]     #main functionality 5
    return total

#main method

def main():
    opc:int = 0
    print("Inventory Management System. Welcome!")
    while True:
        try:
            opc = int(input('''
            Please select an option:
            1. Add products
            2. Consult products
            3. Update prices
            4. Delete products
            5. Show total value of the inventory
            6. Exit
            '''))
            if opc == 1:
                add_products(input("Product name: "),float(input("Product price: ")),int(input("Product quantity: ")))
            elif opc == 2:
                consult_products(input("What product would you like to consult?: "))
            elif opc == 3:
                update_prices(input("What product would you like to update?: "),float(input("What's the new price going to be?: ")))
            elif opc == 4:
                delete_products(input("What product would you like to delete?: "))
            elif opc == 5:
                print(f"Inventory total value is: {round(total_value(), 2)}")
            elif opc == 6:
                print("Goodbye!")
                break
            else:
                print("Error: Invalid option, please try again.")
        except ValueError:
            print("Error: Unsupported input.")

main()