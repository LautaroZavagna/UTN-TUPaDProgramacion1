#Crear una matriz con las notas de 5 estudiantes en 3 materias.
#Mostrar el promedio de cada estudiante.
#Mostrar el promedio de cada materia.

#        nombre de la materia con sus estudiantes,                          primera materia con notas           segunda materia                    tercera materia
notas = [
    ["Materias", "", "Miguel", "Martin", "Cristina", "Diego", "Agostina"],
    ["Matematica", "", 7, 6.5, 9, 10, 9.5],
    ["Literatura", "", 8, 10, 6, 7, 6],
    ["Historia", "", 5, 7, 10, 9, 8],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "]
]

cantidad_filas = len(notas)
cantidad_columnas = len(notas)

for fila in range(cantidad_filas):
    for columna in range(cantidad_columnas):
        print(str(notas[fila][columna]).ljust(10), end=' ')
    print( )