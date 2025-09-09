#Inicializamos la variable suma
suma_total = 0

#Le pedimos al usuario que ingrese un numero
num = int(input("Por favor ingrese un numero: "))

for i in range (0,num):
    suma_total += i

print(f"La suma total de los numeros entre 0 y {num} es de {suma_total}")