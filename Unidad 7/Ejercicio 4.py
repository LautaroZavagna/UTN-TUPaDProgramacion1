agenda = {}

#Bloque para que el usuario agregue los contactos
for i in range(5):
    nombre = str(input("Ingresa el nombre del contacto: "))
    numero = input("Ingrese el numero de telefono: ")
    agenda[nombre.lower()] = numero


#Consultar los contactos
consulta = input("Ingrese el nombre que quiera buscar: ")

if consulta in agenda:
    print(f"El numero de {consulta} es {agenda[consulta]}")
else:
    print("Ese contacto no existe")