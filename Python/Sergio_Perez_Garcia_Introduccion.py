paises = {
    "China": 1441,
    "India": 1408,
    "Estados Unidos": 331,
    "Brasil": 214,
    "España": 48
}

pais = input("País (-1 para terminar): ")

while pais != "-1":
    poblacion = int(input("Población: "))
    paises[pais] = poblacion
    pais = input("País (-1 para terminar): ")

print("\nPaíses ordenados por población:")
for pais in sorted(paises, key=paises.get):
    print(pais, paises[pais])
