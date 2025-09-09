num = int(input("Ingrese el primer numero: "))
suma = 0

while num != 0:
    suma += num
    num = int(input("Ingrese un numero: "))
print(f"La suma total de los numeros ingresados es de {suma}")