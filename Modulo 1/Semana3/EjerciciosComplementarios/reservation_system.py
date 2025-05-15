from datetime import time as dt

flights = {
        
        "AV-321": 
        {
        "origen": "Tokyo",
        "destino": "Medayork",
        "asientos": ["A3", "A2", "B1", "C1"],
        "horario": (16, 40)
        },

        "AV-101": 
        {
        "origen": "Lima",
        "destino": "Bogotá",
        "asientos": ["A1", "A2", "B1", "B2"],
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

def seat_reservation(flight_code:str="",seat:str="")->None:
    for flight in flights:
        if flight == flight_code:
            for seats in flights[flight]["asientos"]:
                if seat == seats:
                    print("reservado.")
                    reserved_flights.append(seat)
                    break
            else:
                print("El asiento ya fue reservado.")
            break
    else:
        print("El codigo del vuelo no fue encontrado.")

reserved_flights:list = []

def percentage_occupation(flight_code:str="")->float:
    totalSeats:int = 0
    percentage:float = 0
    for seats in flights[flight_code]["asientos"]:
        totalSeats += 1
    percentage = len(reserved_flights) / totalSeats
    return percentage * 100

def report_generator():
    report = open("report.txt", "w")
    ordered_list:list = []


    #flights report
    for flight in flights:
        if flights[flight]["horario"][0] <= 23 and flights[flight]["horario"][1] <= 59:
            report.write(f"{flight}\nOrigen: {flights[flight]["origen"]}\nDestino: {flights[flight]["destino"]}\nAsientos: {flights[flight]["asientos"]}\nHorario: {flights[flight]["horario"][0]}:{flights[flight]["horario"][1]}\n")
            report.write("---------------------------------\n")
        else:
            report.write("Invalid schedule.")
    report.close()


def main():
    seat_reservation("AV-121","A3")
    seat_reservation("AV-121","A2")
    print(percentage_occupation("AV-121"))
    print(percentage_occupation("AV-101"))
main()
