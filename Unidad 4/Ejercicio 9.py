#Definimos las variables
promedio = 0
suma = 0

for i in range (1,101):
    num = int(input("Por favor ingrese un numero: "))
    suma += num

#Calculamos el promedio
promedio = suma / 100

print(f"El promedio de todos los numeros ingresados es {promedio}")