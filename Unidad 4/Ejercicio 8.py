#Definimos todas las variables
numeros_pares = 0
numeros_impares = 0
numeros_positivos = 0
numeros_negativos = 0

#Desarrollamos el codigo usando repetitivas y condicionales
for i in range(1,101):
    num = int(input("Ingrese un numero: "))
    if num % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1
    if num >= 0:
        numeros_positivos += 1
    else:
        numeros_negativos += 1

#Imprimimos cada variable usada
print(f"La cantidad de numeros pares es de {numeros_pares}")
print(f"La cantidad de numeros impares es de {numeros_impares}")
print(f"La cantidad de numeros positivos es de {numeros_positivos}")
print(f"La cantidad de numeros negativos es de {numeros_negativos}")