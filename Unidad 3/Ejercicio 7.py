#Pedimos al usuario que ingrese una frase o palabra
Frase = input("Por favor, ingresa una frase o una palabra: ")

#Desarrollamos el codigo
Ultima_Letra = Frase[-1]
if Ultima_Letra == ("a") or ("e") or ("i") or ("o") or ("u"):
    print(f"{Frase}!")
else:
    print(Frase)