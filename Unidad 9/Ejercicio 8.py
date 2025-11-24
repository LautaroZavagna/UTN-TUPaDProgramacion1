def contar_digito(numero, digito):
    #si el numero llega a 0 se detiene la cuenta
    if numero < 10:
        return 1 if numero == digito else 0
    
    
    #tomamos el ultimo digito
    ultimo = numero % 10
    
    #comparamos si coincide
    if ultimo == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)


n = int(input("Ingresa un numero entero positivo: "))
d = int(input("Ingresa un digito (0-9): "))

if n <= 0:
    print("Debes ingresar un número entero POSITIVO.")
    exit()

if d < 0 or d > 9:
    print("Debes ingresar un dígito entre 0 y 9.")
    exit()


print(f"El digito aparece: {contar_digito(n, d)} veces")
