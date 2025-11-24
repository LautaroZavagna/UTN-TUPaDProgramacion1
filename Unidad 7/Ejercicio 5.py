frase = input("Ingrese una frase: ")

frase = frase.lower().strip()

separar_palabras = frase.split()

palabras_unicas = set(separar_palabras)

diccionario = {}

for palabra in separar_palabras:
    if palabra in diccionario:
        diccionario[palabra] += 1
    else:
        diccionario[palabra] = 1

print(f"Palabras unicas: {palabras_unicas}")
print(f"Cantidad de veces que aparece cada palabra: {diccionario}")
