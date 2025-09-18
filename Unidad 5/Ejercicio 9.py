ta_te_ti = [
    [" - ", " - ", " - "],
    [" - ", " - ", " - "],
    [" - ", " - ", " - "]
]

filas = len(ta_te_ti)
columnas = len(ta_te_ti)

print("Aqui podras jugar al Ta-Te-Ti ingresando el numero de columna y fila")

#Mostramos el tablero inicial
for f in range(filas):
    for c in range(columnas):
        print(ta_te_ti[f][c], end=' ')
    print()

turno = 0
ganador = ""

while ganador == "" and turno < 9:
    jugador = "X" if turno % 2 == 0 else "O"
    print(f"Turno del jugador {jugador}")
    f = int(input("Fila (0-2): "))
    c = int(input("Columna (0-2): "))
    #comprobamos si la casilla esta libre
    if ta_te_ti[f][c] == " - ":
        ta_te_ti[f][c] = " " + jugador + " "
        turno = turno + 1
        #mostramos el tablero despues de cada jugada
        for fila in range(filas):
            for col in range(columnas):
                print(ta_te_ti[fila][col], end=' ')
            print()
        #Comprobamos si hay algun ganador
        #filas
        for fila in range(3):
            if ta_te_ti[fila][0] == ta_te_ti[fila][1] == ta_te_ti[fila][2] != " - ":
                ganador = jugador
        #columnas
        for columna in range(3):
            if ta_te_ti[0][columna] == ta_te_ti[1][columna] == ta_te_ti[2][columna] != " - ":
                ganador = jugador
        #diagonales
        if ta_te_ti[0][0] == ta_te_ti[1][1] == ta_te_ti[2][2] != " - ":
            ganador = jugador
        if ta_te_ti[0][2] == ta_te_ti[1][1] == ta_te_ti[2][0] != " - ":
            ganador = jugador
    else:
        print("Esta casilla esta ocupada")

if ganador != "":
    print(f"¡El ganador es el jugador, {ganador}!")
else:
    print("Empate")
