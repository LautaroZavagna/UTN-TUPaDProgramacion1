#Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima:
#“Soy[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

#Definimos la funcion
def informacion_personal(nombre, apellido, edad, residencia):
    return nombre, apellido, edad, residencia


#Pedimos al usuario sus datos
nombre = str(input("Por favor ingrese su nombre: "))
apellido = str(input("Por favor ingrese su apellido: "))
edad = int(input("Por favor ingrese su edad: "))

#Verificamos que la edad sea valida
while edad < 0:
    print("Ingrese una edad valida")
    edad = int(input("Ingrese su edad: "))

residencia = str(input("Por favor ingrese su lugar de residencia: "))

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")