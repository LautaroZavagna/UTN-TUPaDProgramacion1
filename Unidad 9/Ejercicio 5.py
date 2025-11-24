def es_palindromo(palabra):
    #longitud 0 o 1 → es palindromo
    if len(palabra) <= 1:
        return True
    
    #Si los extremos no coinciden, no es palindromo
    if palabra[0] != palabra[-1]:
        return False
    
    #Llamada recursiva
    return es_palindromo(palabra[1:-1])


#prueba del codigo
texto = input("Ingresa una palabra sin espacios ni tildes: ")
print(es_palindromo(texto))
