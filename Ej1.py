# Hola Mundo 
print("Hola Mundo")

# Crea un programa para saber si un numer es par o impar 

def es_par_o_impar():
    """
    Solicita un número al usuario y determina si es par o impar.
    Maneja entradas no numéricas.
    """
    try:
        # Solicitamos al usuario que introduzca un número
        numero_str = input("Introduce un número entero: ")
        # Convertimos la entrada a un número entero
        numero = int(numero_str)

        # Usamos el operador módulo (%) para saber el resto de la división por 2
        if numero % 2 == 0:
            print(f"El número {numero} es par.")
        else:
            print(f"El número {numero} es impar.")
    except ValueError:
        print("Error: Por favor, introduce un número entero válido.")

# Llamamos a la función para que se ejecute el programa
es_par_o_impar()
