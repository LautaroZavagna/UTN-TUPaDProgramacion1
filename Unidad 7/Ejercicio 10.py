paises = {
    "Argentina": "Buenos Aires",
    "Bolivia": "Sucre",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Colombia": "Bogota",
    "Ecuador": "Quito",
    "Paraguay": "Asunción",
    "Peru": "Lima",
    "Uruguay": "Montevideo",
    "Venezuela": "Caracas"
}

capitales_pais = {}

for pais, capital in paises.items():
    capitales_pais[capital] = pais


print("Diccionario invertido")
for capital, pais in capitales_pais.items():
    print(f"{capital}: {pais}")
