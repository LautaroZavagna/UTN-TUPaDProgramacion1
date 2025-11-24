parcial_1 = {"Pedro", "Maria", "Marcos", "Julian", "Sofia"}
parcial_2 = {"Marcos", "Julian", "Sofia"}

ambos_parciales = parcial_1 & parcial_2

un_parcial = parcial_1 ^ parcial_2

print(f"Los alumnos que aprobaron ambos parciales fueron: {ambos_parciales}")
print(f"Los alumnos que aprobaron solo un parcial fueron: {un_parcial}")