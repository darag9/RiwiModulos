Productos = ["gaseosa", "leche", "tinta"]
Precios = [5600, 50000, 50000]
valortotal = 0

totalProductos = Precios[0] + Precios[1] + Precios[2]

print(f'''
        Su Compra esta lista!
        Productos:
        {Productos[0]} : ${Precios[0]}
        {Productos[1]} : ${Precios[1]}
        {Productos[2]} : ${Precios[2]}
      ''')

if totalProductos < 50000 and totalProductos > 0:
    print("Se recomienda pagar por metodo de efectivo!")
    valorTotal = totalProductos - (totalProductos * 0.05)
elif totalProductos >= 50000 and totalProductos <= 100000:
    print("Se recomienda pagar con tarjeta!")
    valorTotal = totalProductos
elif totalProductos > 100000:
    print("Se recomienda pagar por transferencia!")
    valorTotal = totalProductos - (totalProductos * 0.02)
else:
    print("No se admiten valores negativos!")

print(f"El total de su compra es de: {valorTotal}")