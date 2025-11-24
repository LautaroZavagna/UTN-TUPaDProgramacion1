def decimal_a_binario(n):
    #base especial
    if n == 0:
        return "0"
    
    #base general
    if n == 1:
        return "1"

    return decimal_a_binario(n // 2) + str(n % 2)


#programa principal
num = int(input("ingresa un numero entero positivo: "))

if num < 0:
    print("Error, ingresa un numero positivo.")
else:
    binario = decimal_a_binario(num)
    print(f"El numero {num} en binario es: {binario}")
