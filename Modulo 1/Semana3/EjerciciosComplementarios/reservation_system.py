from datetime import time as dt

vuelos = {
        
        "AV-321": 
        {
        "origen": "Tokyo",
        "destino": "Medayork",
        "asientos": ["A1", "A2", "A3", "A4"],
        "horario": (16, 40)
        },

        "AV-101": 
        {
        "origen": "Lima",
        "destino": "Bogotá",
        "asientos": ["B1", "B2", "B3", "B2"],
        "horario": (15, 30)
        },
    
        "AV-121": 
        {
        "origen": "Tokyo",
        "destino": "Medayork",
        "asientos": ["A3", "A2", "B1", "C1"],
        "horario": (20, 40)
        },

        "AV-123": 
        {
        "origen": "Tokyo",
        "destino": "Medayork",
        "asientos": ["A3", "A2", "B1", "C1"],
        "horario": (24, 40)
        }
}


def reserva_asientos(codigo_vuelo:str="",asiento:str=""):
    for codigo in vuelos:
        if codigo == codigo_vuelo:
            for lugar in vuelos[codigo]["asientos"]:
                if asiento == lugar:
                    print("asiento reservado correctamente.")
                    vuelos[codigo]["asientos"].remove(lugar)
                    print(vuelos[codigo]["asientos"])
                    return 
            else:
                print("El asiento ya fue reservado previamente.")
                return True
    else:
        print("El codigo de vuelo no ha sido encontrado. ")
        return True


    
def porcentaje_ocupacion(codigo_vuelo:str="")->float:
    temp:int = 0
    porcentaje:float = 0
    for codigo in vuelos:
        if codigo == codigo_vuelo:
            for i in vuelos[codigo]["asientos"]:
                temp += 1
    porcentaje = (temp / len(vuelos[codigo]["asientos"])) * 100
    return porcentaje

def report_generator():
    report = open("report.txt", "w")
    vuelos_ordenados = sorted(vuelos.items(), key=lambda x: x[1]["horario"])
    for key, detalles in vuelos_ordenados:
        report.write(f"Codigo del vuelo: {key}\nOrigen:{detalles["origen"]}\nDestino:{detalles["destino"]}\nAsientos:{detalles["asientos"]}\nHorario: {detalles["horario"][0]:02d}:{detalles["horario"][1]:02d}\n")
    print("Reporte generado con exito.")

def main():
    print("Sistema de reservacion.")
    while True:
        try:
            opc = int(input
            ('''
            1. Reservar un asiento
            2. Mostrar porcentaje de ocupacion
            3. Generar un reporte
            4. salir
            '''))
            if opc == 1:
                for vuelo in vuelos:
                    print(vuelo, vuelos[vuelo]["asientos"])
                reserva_asientos(input("Ingrese el vuelo que tomara: ").upper(),input("Ingrese el asiento que va a reservar: ").upper())
            elif opc == 2:
                print(porcentaje_ocupacion(input("Ingrese el vuelo del cual quiere consultar su porcentaje: ").upper()))
            elif opc == 3:
                report_generator()
            elif opc == 4:
                break
            else:
                print("Ingresa una opcion valida.")
        except ValueError:
            print("Valor no valido.")


    # reserva_asientos("AV-121","B1")
    # reserva_asientos("AV-121","C1")
    # reserva_asientos("AV-321","A1")
    # reserva_asientos("AV-121","B1")
    # print(porcentaje_ocupacion("AV-121"))
    # print(porcentaje_ocupacion("AV-321"))
    # report_generator()
    
main()
