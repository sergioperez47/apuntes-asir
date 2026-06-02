import json
import random

def cargar_preguntas(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

def ejecutar_test():
    # Ruta al archivo JSON
    ruta = "preguntas_informatica_54.json"
    
    try:
        preguntas = cargar_preguntas(ruta)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta}")
        return

    # Mezclar las preguntas para que salgan en orden aleatorio
    random.shuffle(preguntas)
    
    puntuacion = 0
    total_preguntas = len(preguntas)

    print("--- ¡BIENVENIDO AL TEST DE INFORMÁTICA! ---\n")

    for i, p in enumerate(preguntas, 1):
        print(f"Pregunta {i}: {p['pregunta']}")
        for opcion in p['opciones']:
            print(opcion)
        
        # Solicitar respuesta al usuario
        respuesta_usuario = input("Tu respuesta (A, B, C o D): ").strip().upper()
        
        # Validar
        if respuesta_usuario == p['respuesta_correcta']:
            print("¡Correcto! 🎉\n")
            puntuacion += 1
        else:
            print(f"Incorrecto ❌. La respuesta correcta era la {p['respuesta_correcta']}.\n")
    
    # Resultado final
    print("--- FIN DEL TEST ---")
    print(f"Tu puntuación final es: {puntuacion}/{total_preguntas}")

if __name__ == "__main__":
    ejecutar_test()
