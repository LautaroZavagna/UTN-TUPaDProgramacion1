def fibonacci(n):
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input("ingresa una posicion entera positiva: "))

if num < 0:
    print("Debes ingresar un número mayor o igual a 0.")
else:
    print("Serie de Fibonacci:")
    for i in range(num + 1):
        valor = fibonacci(i)
        print(valor)
