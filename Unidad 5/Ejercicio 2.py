#Pedir al usuario que cargue 5 productos en una lista.
#Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#Preguntar al usuario qué producto desea eliminar y actualizar la lista.

#Definimos las variables
lista_productos = []

#Bucle for para que el usuario agregue productos a la lista
for i in range(1,6):
    productos = input("Por favor ingrese los nombres de los productos: ")
    lista_productos.append(productos)

#Ordenamos alfabeticamente los productos
lista_productos = sorted(lista_productos)

#Le preguntamos al usuario que producto desea eliminar
print("Deseas eliminar o actualizar algun producto de la lista?")
print("1- Dejar la lista como esta")
print("2- Actualizar un producto")
print("3- Eliminar un producto")
operacion = int(input("Seleccione una opcion: "))

if operacion == 2:
    modificacion = input("Escriba el nombre del producto a actualizar: ")
    if modificacion == lista_productos[0]:
        lista_productos[0] = input("Escriba el nombre del nuevo producto: ")
    elif modificacion == lista_productos[1]:
        lista_productos[1] = input("Escriba el nombre del nuevo producto: ")
    elif modificacion == lista_productos[2]:
        lista_productos[2] = input("Escriba el nombre del nuevo producto: ")
    elif modificacion == lista_productos[3]:
        lista_productos[3] = input("Escriba el nombre del nuevo producto: ")
    elif modificacion == lista_productos[4]:
        lista_productos[4] = input("Escriba el nombre del nuevo producto: ")
    else:
        print("Error, ese producto no esta en la lista")
elif operacion == 3:
    modificacion = input("Escriba el nombre del producto a eliminar: ")
    if modificacion == lista_productos[0]:
        lista_productos.remove(modificacion)
    elif modificacion == lista_productos[1]:
        lista_productos.remove(modificacion)
    elif modificacion == lista_productos[2]:
        lista_productos.remove(modificacion)
    elif modificacion == lista_productos[3]:
        lista_productos.remove(modificacion)
    elif modificacion == lista_productos[4]:
        lista_productos.remove(modificacion)
    else:
        print("Error, ese producto no esta en la lista")
elif operacion == 1:
    print("Lista de productos terminada")
else:
    print("Por favor, seleccione una operacion valida")

print(f"la lista de productos es {lista_productos}")