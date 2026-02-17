#Una funcion que nos permita cargar estos datos: nombre del pais y poblacion desde el teclado
def lector_teclado():
    pais = input("Inserte el nombre del pais: ")
    #La entrada de datos finaliza cuando se introduzca un -1 como nombre de un país
    if pais == "-1":
        return "fin",0
    poblacion = int(input(f"Inserte la poblacion de {pais} :"))
    return pais, poblacion

#Los países y los datos de población son un par clave/valor en un diccionario.
paises = {}
ejecucion = True
while ejecucion:
    nombre_pais, poblacion = lector_teclado()
    if nombre_pais == "fin":
        ejecucion = False
    else:
        paises.update({nombre_pais: poblacion})

        paises_ordenados_poblacion = sorted(paises.items(), key=lambda items:items[1], reverse=True)

        print(paises_ordenados_poblacion)

for nombre_pais, poblacion in paises_ordenados_poblacion:
    print(f"{nombre_pais} -> {poblacion}")