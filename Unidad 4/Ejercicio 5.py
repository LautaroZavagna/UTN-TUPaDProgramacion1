#Importamos el modulo random
import random
num = random.randint(0,9)
intentos_totales = 1 #Inicializamos esta variable en 1 porque el usuario tiene que intentar adivinar el numero 1 vez

#Le pedimos al usuario que intente adivinar el numero
intento = int(input("Intenta adivinar el numero: "))

#En caso de que el usuario no adivine el numero a la primera, cada intento sumara 1 a la cantidad de intentos totales
while intento != num:
    intentos_totales += 1
    intento = int(input("Numero incorrecto! intenta otra vez: "))

print(f"Felicidades! has adivinado el numero! La cantidad de intentos realizados es de {intentos_totales}")