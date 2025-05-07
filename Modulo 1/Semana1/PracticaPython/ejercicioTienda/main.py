nombreProducto = input("Ingrese el nombre del producto: ")
precioProducto = float(input("Ingrese el precio del producto: "))
valorTotal = 0

if precioProducto < 50000 and precioProducto > 0:
    print("Se recomienda pagar por metodo de efectivo!")
    valorTotal = precioProducto - (precioProducto * 0.05)
elif precioProducto >= 50000 and precioProducto <= 100000:
    print("Se recomienda pagar con tarjeta!")
    valorTotal = precioProducto
elif precioProducto > 100000:
    print("Se recomienda pagar por transferencia!")
    valorTotal = precioProducto - (precioProducto * 0.02)
else:
    print("No se admiten valores negativos!")

print(f"El precio final del producto: {nombreProducto} es de: ${valorTotal}")