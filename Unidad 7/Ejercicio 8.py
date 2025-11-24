#Creamos la biblioteca
almacen = {"Lapices": 18, "Borradores": 12, "Biromes": 7, "Tijeras" : 3}
#Pasamos todo a minuscula para evitar errores
almacen = {k.lower(): v for k, v in almacen.items()}


while True:
    print("Seleccione la operacion que desea realizar")
    print("1. Consultar Stock")
    print("2. Agregar Unidades")
    print("3. Agregar un nuevo producto")
    print("4. Terminar operacion")
    opcion = int(input("Seleccione una de las tres opciones de arriba: "))

    if opcion == 1:
        consulta = str(input("Ingrese el producto que desea buscar: "))
        if consulta in almacen:
            print(f"El producto {consulta} existe y su stock es de {almacen[consulta]}")
        else:
            print("El producto no existe")
    elif opcion == 2:
        clave = str(input("Seleccione el nombre del producto al que desea agregar unidades: "))
        if clave in almacen:
            agregar = int(input("Ingrese la cantidad de productos a añadir: "))
            almacen[clave] += agregar
            print(f"El producto {clave} ahora tiene {almacen[clave]}")
        else:
            print("El producto que ingreso no esta en stock")
    elif opcion == 3:
        nuevo_producto = str(input("Ingrese el nombre del producto que desea agregar: "))
        if nuevo_producto not in almacen:
            valor = int(input("Ingrese el valor del producto: "))
            almacen[nuevo_producto] = valor
            print("Se ha agregado el nuevo producto")
            print(almacen)
        else:
            print("El producto ya existe")
    elif opcion == 4:
        print("Operacion terminada")
        break
    else:
        print("Opcion invalida")