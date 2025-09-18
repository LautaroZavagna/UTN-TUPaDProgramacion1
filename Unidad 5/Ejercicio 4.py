#Crear una nueva lista sin elementos repetidos.
#Mostrar el resultado.

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datos_actualizados = []

for i in datos:
    if i not in datos_actualizados:
        datos_actualizados.append(i)

print(f"La lista original es: {datos}")
print(f"La lista sin datos repetidos es: {datos_actualizados}")