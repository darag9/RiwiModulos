#inicializacion de las variables
costoTotal = 0
descuentoTotal = 0
valorTotal = 0
#variable para asegurar la repeticion del ciclo
cont = True
#ciclo para consultar el precio de mas de un producto
while cont == True:
    print("Bienvenido a la tienda mayorista")
    #obtencion de datos del usuario
    nombreProducto = input("Ingrese el nombre del producto: ")
    precioUnitario = float(input("Ingrese el precio del producto: "))
    if (precioUnitario <= 0):
        print("El precio debe ser mayor a 0 pesos")
        cont == False
        break
    cantidadProducto = int(input("Ingrese la cantidad de productos que llevara: "))
    if (cantidadProducto <= 0):
        print("no puede llevar 0 productos")
        cont == False
        break
    porcentajeDescuento = int(input("Ingrese el porcentaje del descuento: "))
    if (porcentajeDescuento < 0 or porcentajeDescuento >= 100):
        print("El descuento no puede ser negativo, ni mayor o igual que 100")
        cont == False
        break
    #calcular el costo, descuento, y el valor total con el descuento
    costoTotal = (precioUnitario*cantidadProducto)
    descuentoTotal = costoTotal * porcentajeDescuento/100
    valorTotal = costoTotal - descuentoTotal
    #Impresion de los datos del producto
    print(f'''
    Producto: {nombreProducto}
    Precio Unitario: {precioUnitario}
    Cantidad: {cantidadProducto}
    Descuento: {porcentajeDescuento}%
    Valor Total: {valorTotal}
    ''')
    #Pregunta si desea calcular el valor de otro producto
    opc = input("desea llevar otro producto? ")
    if opc == "no":
        cont = False
    else:
        print("Reiniciando... ")
#termina el programa
print("Fin de ejecucion")



    


