#num = int(input("introduce un numero: "))

#if num%2 == 0:
#    print("Es divisible por 2")
#elif num%3 == 0:
#    print("Es divisible por 3")
#elif num%5 == 0:
#    print("Es divisible por 5")
#else:
#    print("No es divisible por 2, 3 o 5")
#_________________________________________________________________

#continuar = True #Variable auxiliar iteradora

while continuar:
    equipofutbol = input("Dime el nombre de un equipo: ")

     if equipofutbol == "Oviedo":
         print("Buena eleccion")
         continuar = False
    elif equipofutbol == "Barça":
         print("Buena eleccion")
         continuar = False
     elif equipofutbol == "Atleti":
         print("Buena eleccion")
         continuar = False
    else:
        print("Introduce un equipo de futbol valido")
#_______________________________________________________________

#lista_colores = ["rojo", "verde", "azul"]

#for color in lista_colores:
#    print(color)

#Este es un ejemplo no valido
#indice_color = 0
#while indice_color < 3:
  #  print(lista_colores[indice_color])
   # indice_color+=1
#______________________________________________________________

#num = int(input("Introduce un numero: "))
#primo = True

#for i in range (2, num):
#    if num%i == 0:
#        primo = False
#if primo:
  #  print("El numero "+ str(num) + " es primo")
#else:
 #   print("El numero "+ str(num) + " no es primo")