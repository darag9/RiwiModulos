Prueba de Desempeño Riwi - Python

Por: Daniel Ramirez Agudelo

1. Introduction

In this code I am creating a menu to manage an inventory where the user is going to be able to add diferent products
to the inventory, consult their quantity and price, update them, remove any product and lastly calculate the total value of the products the user added.

2. Detailed execution instructions

2.1. When the code is executed, a menu on the terminal will be displayed with 6 options, add products, consult products, update products, delete products,
show the total value of the inventory and exit option.

2.2. First of all the user is going to need to add a product, this product will have 3 attributes, a name, price and quantity, all the process with it's 
due validations. In the process of this method the product will be added as a dictionary item on the list products in this position 0 of the list. 
after the execution of the method the user will return to the menu. If the user added another product with the same name,  an error message will be shown.

2.3. the next method will be consult products, where the user is going to need to input the product's name in the method for it to be able to display 
the consulted product's attributes including name, price and quantity. If the requested product was not found, the algorythm will show an error message.

2.4. the next method will be update prices, where the user is going to need to input the product's name and also the updated price, 
the method will search for the product's name, if the name's found, it will replace the old price with the new one. 
if the name couldn't be found an error message will be shown.

2.5. the next method will be delete products, where the user is going to need to input the product's name.
the method will look for the name on the list, if found, the dictionary of the product will be removed. If it doesn't
find the products name, an error message will be shown.

2.6. the next method will be total value, where the user is not going to input anything, but the method needs to find at least
any product in the products list, for it to return a total value, else it will only return 0.

3. Input and output examples

- The algorythm is always going to ask for the user to input the values.
