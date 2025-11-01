#Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro e imprima la tabla de multiplicar de ese número del 1 al 10.
#Pedir al usuario el número y llamar a la función.

#Definimos la funcion
def tabla_multiplicar(numero):
    return numero * multiplicador

#Le pedimos al usuario que ingrese el numero
numero = int(input("Ingrese un numero para hacer su tabla de multiplicacion: "))

temp_numero = numero #Creamos una variable temporal para guardar el numero que ingreso el usuario

for i in range (1, 11, 1):
    multiplicador = i
    print(f"{temp_numero} X {multiplicador} = {tabla_multiplicar(numero)}")