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
def calculadora_textual_division(fraccion = ""):
    if fraccion.find("/") != 1:
        return 0.0
    """
    division = fraccion.split("/")
    numerador = division[0]
    denominador = division[1]
    """
    numerador, denominador = fraccion.split("/")
    if not numerador.isdecimal() or not denominador.isdecimal():
        return 0.0
    return int(numerador)/int(denominador)


def main():
    print(calculadora_textual_division("100000"))
    print(calculadora_textual_division("//10"))
    print(calculadora_textual_division("10/*"))
    print(calculadora_textual_division("a/10"))
    print(calculadora_textual_division("25/10"))
    print(calculadora_textual_division("4.5/5.3"))



if __name__ == "__main__":
    main()