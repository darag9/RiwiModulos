cont = 0
valorTotal = 0
valorDescuento = 0
cantidadProductos = int(input("Ingrese la cantidad de productos que va a llevar: "))
Productos = []
Precios = []

while cont != cantidadProductos:
    Productos.append(input("Ingrese el nombre del producto: "))
    Precios.append(float(input("Ingrese el precio del producto: ")))
    if Precios[cont] < 0:
        print("No fue posible agregar el producto: Error de Precio")
        cont = cont+1
    else:
        print(Productos)
        valorTotal = Precios[cont] + valorTotal
        print(valorTotal)
        print(f"El producto {Productos[cont]} se ha agregado correctamente y tiene un valor de ${Precios[cont]}")
        cont = cont+1

if valorTotal < 50000 and valorTotal > 0:
    print("Se recomienda pagar por metodo de efectivo!")
    valorDescuento = valorTotal - (valorTotal * 0.05)
elif valorTotal >= 50000 and valorTotal <= 100000:
    print("Se recomienda pagar con tarjeta!")
    valorDescuento = valorTotal
elif valorTotal > 100000:
    print("Se recomienda pagar por transferencia!")
    valorDescuento = valorTotal - (valorTotal * 0.02)
else:
    print("No se admiten valores negativos!")


