#Creamos el archivo .txt y le agregamos tres productos iniciales.
with open("productos.txt", "w") as archivo:
    archivo.write("Lapiz,100,20\n")
    archivo.write("Borrador,50,15 \n")
    archivo.write("Pegamento,200,14 \n")

print("------------------")
print("------------------")

#Codigo para leer y mostrar productos
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip() #Borrar espacios y saltos de linea
        #Separamos datos con comas
        datos = linea.split(",")
        nombre = datos[0]
        precio = datos[1]
        cantidad = datos[2]

        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

print("------------------")
print("------------------")

#El usuario puede agregar productos
with open("productos.txt", "a") as archivo:
    for i in range(3):
        agregar_producto = str(input("Ingrese el producto que desea agregar: "))
        agregar_precio = float(input("Ingrese el precio del producto: "))
        agregar_cantidad = int(input("Ingrese el stock del producto: "))
        archivo.write(f"{agregar_producto},{agregar_precio},{agregar_cantidad}\n")

print("------------------")
print("------------------")

#Punto 4
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        if linea: 
            datos = linea.split(",")
            producto = {
                "nombre": datos[0],
                "precio": float(datos[1]),
                "cantidad": int(datos[2])
            }
            productos.append(producto)
for i in productos:
    print(i)

print("------------------")
print("------------------")

#Punto 5
buscar = str(input("Ingrese el nombre del producto: "))

encontrado = False
for producto in productos:
    if producto["nombre"].lower() == buscar.lower():
        print(f"Producto encontrado")
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: ${producto['precio']}")
        print(f"Stock: {producto['cantidad']}")
        encontrado = True
        break
if not encontrado:
    print("El producto no existe")

print("------------------")
print("------------------")

#punto 6
with open("productos.txt", "w") as archivo:
    for producto in productos:
        archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
