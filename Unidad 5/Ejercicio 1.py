#Crear una lista con las notas de 10 estudiantes.
#Mostrar la lista completa.
#Calcular y mostrar el promedio.
#Indicar la nota más alta y la más baja.

#creamos la lista con valores aleatorios
notas = [7.3, 4.1, 9.8, 6, 3, 7, 8.9, 10, 5, 8.5]
cantidad_notas = len(notas) #Hacemos este paso para saber la cantidad exacta de valores que tiene la lista
promedio = (sum(notas)) / 10 #Calculamos el promedio
promedio = round(promedio, 2) #Redondeamos el promedio a dos numeros despues de la coma para que no regrese un numero largo

#Definimos las variables de las notas altas y bajas
nota_alta = 0
nota_baja = float('+inf')

#Usamos un ciclo For para que se impriman los valores de la lista 1 por 1
for i in range(cantidad_notas):
    print(notas[i])
    if notas[i] > nota_alta:
        nota_alta = notas[i]
    elif notas[i] < nota_baja:
        nota_baja = notas[i]

print("----")
print(f"La nota mas alta es {nota_alta}")
print(f"La nota mas baja es {nota_baja}")
print(f"El promedio de todas las notas es {promedio}")