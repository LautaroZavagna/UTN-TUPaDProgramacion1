#Ejercicio 1
print ("Hola Mundo!")

#Ejercicio 2
Nombre = input("Por favor, ingrese su nombre: ")
print (f"Hola", Nombre)

#Ejercicio 3
Nombre = input("Por favor, ingrese su nombre: ")
Apellido = input("Por favor ingrese su apellido: ")
Edad = input("Por favor ingrese su Edad: ")
Edad = int(Edad)
Residencia = input("Por favor ingrese su pais de residencia: ")
print (f"Soy", Nombre, Apellido,", tengo ",Edad, "años y vivo en", Residencia)

#Ejercicio 4
import math
Radio = float(input("Ingrese el radio del circulo: "))
Area = math.pi * (Radio ** 2)
Perimetro = 2 * math.pi * Radio
print (f"El Area es:", Area)
print (f"El perimetro es:", Perimetro)

#Ejercicio 5
Segundos = int(input("Ingrese la cantidad de segundos: "))
Horas = Segundos / 3600
print (f"Los segundos ingresados son equivalentes a ", Horas, "Horas")

#Ejercicio 6
numero = int(input("Ingrese un numero, a continuacion se mostrara la tabla de multiplicar del mismo: "))
for i in range(1, 11):
    Resultado = numero * i
    print(f"{numero} X {i} = {Resultado}")

#Ejercicio 7
PrimerNumero = float(input("Ingrese el primer numero: "))
SegundoNumero = float(input("Ingrese el segundo numero: "))

NumeroFinal = PrimerNumero + SegundoNumero
print(f"La suma de {PrimerNumero} y {SegundoNumero} es {NumeroFinal}")
NumeroFinal = PrimerNumero - SegundoNumero
print(f"La resta de {PrimerNumero} y {SegundoNumero} es {NumeroFinal}")
NumeroFinal = PrimerNumero * SegundoNumero
print(f"La multiplicacion de {PrimerNumero} y {SegundoNumero} es {NumeroFinal}")
NumeroFinal = PrimerNumero / SegundoNumero
print(f"La division de {PrimerNumero} y {SegundoNumero} es {NumeroFinal}")

#Ejercicio 8
Altura = float(input("Ingrese su altura en metros: "))
Peso = float(input("Ingrese su peso en Kilogramos: "))
IMC = Peso / (Altura)**2
IMC = round(IMC, 1)
print(f"Su indice de masa corporal es: {IMC}")

#Ejercicio 9
GradoF = float(input("Ingrese una temperatura en grados Fahrenheit para convertirla en Celsius: "))
GradoG = (GradoF - 32) * (5/9)
print(f"{GradoF} grados Fahrenheit son equivalentes a {GradoG} grados Celcius")

#Ejercicio 10
print("Ingrese tres numeros a continuacion para sacar su promedio")
PrimerNumero = int(input("Escriba el primer Numero: "))
SegundoNumero = int(input("Escriba el segundo Numero: "))
TerceroNumero = int(input("Escriba el tercer Numero: "))

Promedio = (PrimerNumero + SegundoNumero + TerceroNumero) / 3
print(f"El promedio de los tres numeros ingresados es {Promedio}")