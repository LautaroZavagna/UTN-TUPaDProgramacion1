#Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
#Mostrar el total vendido por cada producto.
#Mostrar el día con mayores ventas totales.
#Indicar cuál fue el producto más vendido en la semana.

#Definimos la matriz
ventas = [
    ["Ventas", "Queso", "Jamon Cocido", "Salame", "Jamon Crudo", " ", " ", " "],
    ["Dia 1", 10, 15, 5, 7, " ", " ", " "],
    ["Dia 2", 20, 10, 8, 12, " ", " ", " "],
    ["Dia 3", 5, 8, 6, 9, " ", " ", " "],
    ["Dia 4", 12, 17, 10, 11, " ", " ", " "],
    ["Dia 5", 8, 12, 7, 6, " ", " ", " "],
    ["Dia 6", 11, 9, 9, 13, " ", " ", " "],
    ["Dia 7", 15, 11, 12, 14, " ", " ", " "]
]
mayor_ventas = 0
mejor_dia = ""
total_maximo = 0
producto_mas_vendido = ""

cantidad_filas = len(ventas)
cantidad_columnas = len(ventas)

#Bucle for para mostrar la tabla de ventas
for fila in range(cantidad_filas):
    for columna in range(cantidad_columnas):
        print(str(ventas[fila][columna]).ljust(15), end=' ')
    print( )

#Bucle para ver la cantidad total de productos vendidos
print("Venta total de productos:")
for columna in range(1,5):
    productos_totales = 0
    for fila in range(1, cantidad_filas):
        cantidad = ventas[fila][columna]
        if cantidad != " ": #Evitamos los espacios
            productos_totales += cantidad
    print(ventas[0][columna], ":", productos_totales)

#Bucle para ver el dia con mas ventas
for fila in range(1,5):
    total_diario = 0
    for columna in range(1,cantidad_columnas):
        cantidad = ventas[fila][columna]
        if cantidad != " ":
            total_diario += cantidad
    if total_diario > mayor_ventas:
        mayor_ventas = total_diario
        mejor_dia = ventas[fila][0]
print(f"El dia con mayor ventas fue el {mejor_dia} con una cantidad de {mayor_ventas} productos totales vendidos")

#Bucle para saber cual fue el producto mas vendido de la semana
for columna in range(1,5):
    total_producto = 0
    for fila in range(1,cantidad_filas):
        cantidad = ventas[fila][columna]
        if cantidad != " ":
            total_producto += cantidad
    if total_producto > total_maximo:
        total_maximo = total_producto
        producto_mas_vendido = ventas[0][columna]
print(f"El producto mas ventido durante la semana es: {producto_mas_vendido} con un total de {total_maximo} ventas")