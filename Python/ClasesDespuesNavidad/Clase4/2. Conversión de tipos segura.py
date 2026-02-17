"""
2. Conversión de tipos segura

Crea una función llamada convertir_a_entero(lista). Esta función debe recibir una lista de strings y devolver una nueva lista solo con los valores que pudieron convertirse exitosamente a int. Los que fallen deben ignorarse (pero el programa no debe detenerse).
• Ejemplo de entrada: ["10", "hola", "20", "3.5"]
• Resultado esperado: [10, 20]
"""

def convertir_a_entero(lista):
    resultado = []
    for valor in lista:
        try:
            valor = int(valor)
        except:
            pass
        else:
            resultado.append(valor)
        return resultado

lista_original = ["10", "hola", "20", "3.5"]
lista_numeros = convertir_a_entero(lista_original)
print(lista_original)
print(lista_numeros)