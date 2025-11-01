#Crear dos funciones:
#calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.
#calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo.
#Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

#Importamos el modulo math para poder usar el Pi
import math

#Definimos funciones
def calcular_area_circulo(radio):
    return (radio**2) * math.pi

def calcular_perimetro_circulo(radio):
    return (radio * 2) * math.pi

#Le pedimos el radio al usuario
radio = int(input("Ingrese el radio de un circulo para calcular su area y perimetro: "))

print(f"El area del circulo es {calcular_area_circulo(radio)} y su perimetro es {calcular_perimetro_circulo(radio)}")