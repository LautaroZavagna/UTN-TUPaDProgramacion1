#Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
#Calcular el promedio de las mínimas y el de las máximas.
#Mostrar en qué día se registró la mayor amplitud térmica

clima = [[24, 13], [26, 17], [23, 17], [27, 18], [24, 14], [16, 9], [17, 8]]
temp_max = 0
temp_min = 0
promedio_max = 0
promedio_min = 0
dia_mas_alta = 1
temp_mas_alta = 0

#Sumamos las temperaturas maximas y minimas de todos los dias
for i in clima:
    max = i[0]
    min = i[1]
    temp_max += max
    temp_min += min
    if max > temp_mas_alta: #aplicamos if para saber cuanto es la temperatura mas alta y cuando se regitro
        temp_mas_alta = max
        dia_mas_alta += 1

#Calculamos el promedio y redondeamos el resultado a un numero despues de la coma
promedio_max = round((temp_max / 7),1)
promedio_min = round((temp_min / 7),1)

print(f"El promedio de las temperaturas maximas de la semana es {promedio_max}º")
print(f"El promedio de las temperaturas minimas de la semana es {promedio_min}º")
print(f"La temperatura mas alta registrada en la semana es {temp_mas_alta}º, registrada en el {dia_mas_alta} dia de la semana")