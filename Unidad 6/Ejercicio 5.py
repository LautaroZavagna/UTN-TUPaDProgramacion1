#Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes.
#Solicitar al usuario los segundos y mostrar el resultado usando esta función.

#Definimos la funcion
def segundos_a_horas(segundos):
    return (segundos / 60) / 60

#Pedimos al usuario la cantidad de segundos
segundos = int(input("Ingrese la cantidad de segundos que desea convertir a horas: "))

print(f"la cantidad de segundos ingresadas son {segundos_a_horas(segundos)} horas")