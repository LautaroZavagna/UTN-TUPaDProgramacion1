#Importamos los paquetes
from statistics import mode, median, mean
import random

#Desarrollamos el codigo
Numeros_Aleatorios = [random.randint(1, 100) for i in range(50)]
Num_Mode = mode(Numeros_Aleatorios)
Num_Median = median(Numeros_Aleatorios)
Num_Mean = mean(Numeros_Aleatorios)
print(Num_Mode)
print(Num_Median)
print(Num_Mean)