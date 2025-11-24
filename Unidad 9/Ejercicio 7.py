def contar_bloques(n):
    #validacion
    if n < 1:
        return None
    if n == 1:
        return 1
    
    return n + contar_bloques(n - 1)


num = int(input("Ingresa el numero de bloques en el nivel mas bajo: "))
resultado = contar_bloques(num)

if resultado is None:
    print("Debes ingresar un numero entero mayor o igual a 1.")
else:
    print(f"En total se necesitan {resultado} bloques")
