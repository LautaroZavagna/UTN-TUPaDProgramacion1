#Crear una lista con los nombres de 8 estudiantes presentes en clase.
#Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#Mostrar la lista final actualizada

estudiantes = ["Diego", "Martin", "Laura", "Andrea", "Tomas", "Matias", "Ana", "Agostina"]

#Le presentamos la lista al usuario y le damos a elegir lo que desea hacer
print(f"Los siguientes alumnos se encuentran en clase: {estudiantes}")
print("Deseas agregar o eliminar a algun estudiante?")
print("1- Agregar un estudiante a la lista")
print("2- Eliminar un estudiante a la lista")
print("3- Dejar la lista como esta")
eleccion = int(input("Seleccione la operacion a realizar: "))

if eleccion == 1:
    modificacion = input("Ingrese el nombre del usuario: ")
    estudiantes.append(modificacion)
elif eleccion == 2:
    modificacion = input("Ingrese el nombre del estudiante a eliminar: ")
    estudiantes.remove(modificacion)
elif eleccion == 3:
    print("Operacion finalizada")
else:
    print("Error, por favor ingrese una opcion valida")

print(f"La lista de estudiantes ha quedado asi: {estudiantes}")