#Inicializamos variables
suma = 0

#Pedimos al usuario ambos valores
primer_valor = int(input("Por favor ingrese el primer valor: "))
segundo_valor = int(input("Por favor ingrese el segundo valor: "))

#Aplicamos bucle for porque conocemos la cantidad de veces que se va a ejecutar
for i in range(primer_valor + 1, segundo_valor): #Le sumamos 1 al primer valor para que no lo tenga en cuenta en la suma
    suma += i
print(f"La suma de todos los valores entre {primer_valor} y {segundo_valor} es {suma}")