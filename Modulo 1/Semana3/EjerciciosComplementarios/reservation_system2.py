vuelos = {
    "codigo": 
    {
    "origen": "Lima",
    "destino": "Bogotá",
    "asientos": ["A1", "A2", "B1", "B2"],
    "horario": (15, 30)
    }
}

asientos_reservados:dict = {"codigo"}

def agregar_vuelo(codigo:str="",origen:str="",destino:str="",asientos:list=[],horario:tuple=())->dict:
    for vuelo in vuelos:
        if codigo == vuelos["codigo"]:
            print("El codigo del vuelo ya se ha agregado anteriormente.")
            return vuelos
    vuelos.update({"codigo":{"origen":origen,"destino":destino,"asientos":asientos,"horario":horario}})
    return vuelos

def reservacion_asiento(codigo:str="",asiento:str="")->None:
    pass

def main():
    print(agregar_vuelo("AV-101","Medellin","Bogota",["A1","A2","A3","B1","B2","B3"],(20, 30)))

main()