"""
def con_raise(numero):
    if numero %2 == 0:
        raise Exception("No queremos numeros pares")
    else:
        return numero
todo_ok =  False
while not todo_ok:
    try:
        numero = int(input("Dame un numero impar: "))
        print(con_raise(numero))
    except ValueError:
        print("Eso no es un numero")
    except Exception as excepcion:
        print(excepcion)
    else:
        todo_OK = True
"""
import datetime


def comprobar_fecha():
    dia, mes, año = fecha.split("/")
    dia = int(dia)
    mes = int(mes)
    año = int(año)
    if mes > 12 or mes < 1:
        return False
    if dia > 31 or dia < 1:
        return False
    # 1,3,5,7,8,10,12 -> 31
    # 4,6,9,11
    if mes == 2:
        if bisiesto(año) and dia <= 29:
            return True
        elif not bisiesto(año) and dia <= 28:
            return True
        else:
            return False
    if mes in (1, 3, 5, 7, 8, 10, 12):
        return True
    elif mes in (4, 6, 9, 11) and dia < 31:
        return True
    else:
        return False


def bisiesto(año):
    return año % 4 == 0 and año % 100 != 0 or año % 400 == 0


print(comprobar_fecha("31/04/1984"))

datetime.date(1984,2,29)

try:
    datetime.date(1984,2,28)
except:
    print("Fecha incorrecta")
else:
    print("Fecha correcta")