def potencia(base, exponente):
    #Manejo de casos invalidos
    if base == 0 and exponente == 0:
        return None

    if exponente < 0:
        return None
    if exponente == 0:
        return 1

    return base * potencia(base, exponente - 1)


#Codigo principal
b = float(input("ingrese la base: "))
e = int(input("ingrese el exponente: "))

resultado = potencia(b, e)

if resultado is None:
    print("La potencia no esta definida para los valores ingresados.")
else:
    print(f"{b} elevado a {e} es: {resultado}")
