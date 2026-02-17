#Elementos separados con comas y el conjunto en corchetes
#listaColores = ['rojo', 'verde', 'azul']
#print(listaColores)
#a = list('hola')
#type(a)
#print(a)
#colorB = listaColores[-1]
#print(colorB)
#list=[["a","b","c"],["d","e","f"],["g","h","i"],
#["j","k","l"]]
#list[0][0] = "a" ;list[0][1] = "b" ;list[0][2] = "c"
#list[1][0] = "d" ;list[1][1] = "e" ;list[1][2] = "f"
#list[2][0] = "g" ;list[2][1] = "h" ;list[2][2] = "i"
#list[3][0] = "j" ;list[3][1] = "k" ;list[3][2] = "l"
#print(list)

#hora de los ejercicios
import random
#variables
#lista = []
#funcionalidad
#for i in range(10):
#   lista.append(random.randint(1,500))
#lista.sort()
#print(lista)

#num = int(input("introduce un numero: "))
#if lista.count(num) >= 0:
#   print("el numero "+str(num)+" esta en la lista")
#   print("hay "+str(lista.index(num)) +" numeros antes de "+str(num))
    #else:
#   print("el numero "+str(num)+" no esta en la lista")

#salida
#print(lista)
#hora de los ejercicios PARTE2
lista =[]
num = 0
while num >=0:
    num = int(input("Introduce un numero: "))
    if num >= 0:
        lista.append(num)
        elif type(num) != int:
        print("No has introducido el numero")


lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
#variables
#funcionalidad
#Hay que corregir que el -1 sea la condicion y que no salga