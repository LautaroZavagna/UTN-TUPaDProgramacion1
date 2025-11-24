def suma_digitos(n):
    #digito unico
    if n < 10:
        return n
    
    #ultimo digito + recursion sobre resto
    return (n % 10) + suma_digitos(n // 10)


#prueba del programa
num = int(input("Ingrese un numero entero positivo: "))
print(f"La suma de los digitos es: {suma_digitos(num)}")
