"""
4. Escribir una función en python que reciba una cadena de texto que representa una fracción y
nos devuelva su valor en decimal. La fracción tiene que ser introducida con el formato:
numerador/denominador, siendo numerador y denominador dos números enteros. Si
introducimos algo que no corresponda con esto debería de devolver un cero
EJEMPLOS DE EJECUCIÓN:
INVOCACIÓN DE LA FUNCIÓN              RESULTADO EN LA CONSOLA
print(fraccion(“25/10”))                       2.5
print(fracción(“a/10”))                         0
print(fracción(“//10”))                         0
print(fracción(“10”))                           0
"""
from mako.compat import exception_as


def calculadora_textual_division(fraccion = ""):
    resultado = 0
    try:
        numerador, denominador = fraccion.split("/")
        numerador = int(numerador)
        denominador= int(denominador)
    except Exception as e:
        print(e)
    else:
         resultado = numerador/denominador
    finally:
        return resultado
"""
#Esto es un ejemplo :)
def calculadora_textual_division(fraccion = ""):
    try:
        division = fraccion.split("/")
        error = division[2]
        return int(division[0])/int(division[1])
    except ValueError as e:
        print(e)
        return 0
    except IndexError as e:
        print(e)
        return 0
    except Exception as e:
"""
def main():
    print(calculadora_textual_division("100000"))
    print(calculadora_textual_division("//10"))
    print(calculadora_textual_division("10/*"))
    print(calculadora_textual_division("a/10"))
    print(calculadora_textual_division("25/10"))
    print(calculadora_textual_division("4.5/5.3"))



if __name__ == "__main__":
    main()