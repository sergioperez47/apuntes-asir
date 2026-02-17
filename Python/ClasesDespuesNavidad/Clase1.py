#String secuencia. Inmutable y ordenada
 #cadena = "patata"
 #cadena[3] = "R"
 #cadena = "batata"
 #print(cadena[2])
 #print(type(cadena))
 #print(len(cadena))
from numpy.matrixlib.defmatrix import matrix

#Listas, Mutable, puede contener elementos repetidos,
#esta ordenada por orden de llegada
 #lista = [1,2,4,4,4,6,7]
 #print(lista)
 #lista[3] = 0
 #print(lista)
 #lista.sort()
 #print(lista)
 #lista.append(4)
 #print(lista)
 #print(lista.index(4))
 #print(lista.count(5))
 #print(len(lista))

#Matrices
 #matriz=[
     #["a1","b2","c3"],
     #["d1","e2","f3"],
     #["g1","patata","i3"],
     #["j1","k2","l3"],
 #]
 #print(matriz[2][1][4])

#Tupla, es inmutable
 #tuplaRGB = (12,10,105)
 #print(tuplaRGB)
  #tuplaRGB[0] = 125
 #tuplaRGB = (120,10,105)
 #print(tuplaRGB)

#Diccionario
#clave/key - no repetir, inmutable
#valor/value - se puede repetir, mutable
 #diccionario = {
     #"felix@email.es":1,
     #"emma@email.es":2,
     #"jorge@mail.com":0
 #}
 #print(diccionario)
 #print(diccionario.keys())
 #print(diccionario.values())
 #print(diccionario.items())
 #diccionario["miguela@hmail.es"] = 1
 #print(diccionario)
 #diccionario["jorge@mail.com"] = 1
 #print(diccionario)
 #diccionario.update({"lola@eilo.org":7})
 #print(diccionario)
 #diccionario.update({"jorge@mail.com":6})
 #print(diccionario)
 #for clave,valor in diccionario.items():
    #print(clave)
    #print(valor)
#sorted, ordena cosas inmutables e iterables
 #for clave in sorted(diccionario.keys()):
    #print(clave,diccionario[clave])
#print(diccionario.pop("felix@email.es"))
#print(diccionario)

