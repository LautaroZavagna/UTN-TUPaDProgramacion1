#Le pedimos al usuario los datos
nombre = str(input("Por favor ingresa tu nombre: "))
print("Selecciona la opcion deseada:")
print("1. Convertir tu nombre en mayusculas")
print("2. Convertir tu nombre en minusculas")
print("3. Convertir la primera letra de tu nombre en mayusculas")
opcion = int(input("Selecciona la opcion deseada: "))

if opcion == 1:
    nombre_final = nombre.upper()
    print(nombre_final)
elif opcion == 2:
    nombre_final = nombre.lower()
    print(nombre_final)
elif opcion == 3:
    nombre_final = nombre.title()
    print(nombre_final)
else:
    print("Por favor selecciona una opcion valida")