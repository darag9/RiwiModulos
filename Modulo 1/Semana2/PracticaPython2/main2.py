texto1:str ="" 
texto2:str ="" 
texto3:str="" 
texto4:str="" 

numero1:float=0.0 
numero2:float=0.0 
sumar:float =0 
lista:list[float] = []

texto1="mundo" 
texto2="hola" 
texto1="pedro" 


texto1= input("Ingrese las calificaciones separadas por notas sin espacios: ")

for i in texto1: 
    if i != ",": 
        texto4 = texto4.__add__(i)
    else: 
        numero:float = float(texto4)
        lista.append(numero)
        print(lista)
        texto4=""
        sumar=sumar+numero