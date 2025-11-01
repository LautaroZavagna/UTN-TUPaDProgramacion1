#Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

#Definimos la funcion
def saludar_usuario(nombre):
    return nombre

nombre = str(input("Por favor, ingrese su nombre: "))
print(f"Hola {(saludar_usuario(nombre))}!")