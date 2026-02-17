#Primero se declara las variables y se inicializan
enteros = 0
contador = 0
total = 0
#Seguir con el bucle mientras el usuario no introduzca la palabra exit
while enteros != "EXIT":
#Se tiene que quitar el int porque si no el programa explota
    #Ahora se vuelve a poner el int pero sigue saliendo error
    enteros= input("Introduce una nota: ")
#Hay que usar un if porque de la forma convencional el programa siempre va a explotar
    if enteros != "EXIT":
        # El calculo del total tiene que ir dentro del bucle,y ahora hay que hacer
        # la suma de todos los enteros
        total += int(enteros)
        # El contador sirve para ver cuantas veces has entrado al bucle
        contador += 1
# El valor exit tambien cuenta como uno pero eso no es correcto porque no deberia
# ser un valor visible de tu entrada al bucle

print("Se han introducido:", contador, "notas")
print("El total es:", total)
print("La nota media es:", total/contador)