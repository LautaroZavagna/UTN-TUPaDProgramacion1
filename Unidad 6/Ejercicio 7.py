#Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de:
#sumarlos, restarlos, multiplicarlos y dividirlos.
#Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, division, multiplicacion

a = float(input("Por favor ingrese el primer numero: "))
b = float(input("Por favor ingrese el segundo numero: "))

resultados = operaciones_basicas(a, b)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")