#Pedimos al usuario que ingrese una contraseña
Contraseña = input("Por favor ingrese una contraseña de entre 8 y 14 caracteres: ")

#Desarrollamos el codigo usando condicionales
Long_Contraseña = len(Contraseña)
if Long_Contraseña >= 8 and Long_Contraseña <=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")