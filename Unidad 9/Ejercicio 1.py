def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Ingresa un numero entero positivo: "))

if num < 0:
    print("Debes ingresar un entero mayor o igual a 0.")
else:
    for i in range(0, num + 1):
        resultado = factorial(i)
        print(f"El factorial de {i} es: {resultado}")
