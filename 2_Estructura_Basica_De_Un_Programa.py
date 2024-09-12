# Importación de librerías
import datetime

# Declaración de variables
nombre = "Juan"
edad = 25


# Declaración de funciones
def saludar(nombre):
    """Imprime un mensaje de saludo"""
    print(f"Hola, {nombre}!")


def calcular_edad(edad):
    """Calcula la edad en años"""
    return edad


# Programa principal
def main():
    # Comentarios
    # Este es un comentario de una línea
    """
    Este es un comentario de varias líneas
    """

    # Estructuras de control
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")

    # Entrada y salida
    print("¿Cuál es tu nombre?")
    nombre_usuario = input()
    print(f"Hola, {nombre_usuario}!")

    # Llamada a funciones
    saludar(nombre)
    edad_calculada = calcular_edad(edad)
    print(f"Tu edad es: {edad_calculada}")

    # Terminación del programa
    print("¡Hasta luego!")

main()