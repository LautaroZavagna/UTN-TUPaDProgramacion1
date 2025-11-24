agenda = {
    ("Lunes", "09:30"): "Matematica",
    ("Martes", "10:00"): "Historia",
    ("Miercoles", "14:00"): "Quimica",
    ("Jueves", "19:00"): "Fisica",
}

#consultamos la agenda
dia = input("Ingrese el dia: ").capitalize() #Normalizamos la primera letra mayuscula
hora = input("Ingrese la hora: ")

actividad = (dia, hora)

if actividad in agenda:
    print(f"La actividad programada es: {agenda[actividad]}")
else:
    print("No hay actividad programada para ese dia y/o horario")