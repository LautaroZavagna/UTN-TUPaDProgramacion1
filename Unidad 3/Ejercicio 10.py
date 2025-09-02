#Pedimos al usuario los datos
print("Por favor seleccione en que hemisferio se encuentra:")
print("1. Hemisferio norte")
print("2. Hemisferio sur")
hemisferio = int(input("Ingrese la opcion correspondiente: "))
print("Por favor seleccione el mes actual:")
print("1. Enero")
print("2. Febrero")
print("3. Marzo")
print("4. Abril")
print("5. Mayo")
print("6. Junio")
print("7. Julio")
print("8. Agosto")
print("9. Septiembre")
print("10. Octubre")
print("11. Noviembre")
print("12. Diciembre")
mes = int(input("Por favor, seleccione el mes correspondiente: "))
dia = int(input("Por favor ingrese el numero del dia: "))

if hemisferio == 1:
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        print("invierno")
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        print("primavera")
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        print("Verano")
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        print("Otoño")
elif hemisferio == 2:
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        print("Verano")
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        print("Otoño")
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        print("Invierno")
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        print("Primavera")
else:
    print("Por favor, ingrese un hemisferio valido")