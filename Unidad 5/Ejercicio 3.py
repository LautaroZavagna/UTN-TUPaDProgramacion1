#Generar una lista con 15 números enteros al azar entre 1 y 100.
#Crear una lista con los pares y otra con los impares.
#Mostrar cuántos números tiene cada lista.

import random

num_random = []
num_pares = []
num_impares = []

for i in range(15):
    num_random.append(random.randint(1, 100))

for par_impar in num_random:
    if par_impar % 2 == 0:
        num_pares.append(par_impar)
    else:
        num_impares.append(par_impar)

print(f"Lista de numeros aleatorios: {num_random}")
print(f"Lista de numeros pares: {num_pares}")
print(f"Lista de numeros impares: {num_impares}")
