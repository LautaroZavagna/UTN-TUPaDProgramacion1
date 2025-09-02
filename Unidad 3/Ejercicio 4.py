#Le pedimos al usuario que ingrese su edad
Edad = int(input("Por favor ingrese su edad: "))

#Desarrollamos el codigo
if Edad < 12:
    print("Perteneces a la categoria de Niño/a")
elif Edad >= 12 and Edad < 18:
    print("Perteneces a la categoria de adolescente")
elif Edad >= 18 and Edad <30:
    print("Perteneces a la categoria de adulto/a joven")
else:
    print("Perteneces a la categoria de Adulto/a")