alumnos = {}

#Ciclo for para cargar 3 alumnos y sus notas
for i in range(3):
    nombre = str(input("Ingrese el nombre del alumno: "))
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))
    alumnos[nombre] = (nota1, nota2, nota3)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / 3
    print(f"El promedio de {nombre} es {promedio}")