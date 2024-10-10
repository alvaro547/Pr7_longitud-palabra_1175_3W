print(" ")
print("Alvaro Campechano 3W")
print(" ")
def longitud_ultima_palabra(frase):
    """
    Devuelve la longitud de la última palabra en una cadena.
    
    Args:
    frase (str): La cadena de texto a analizar.
    
    Returns:
    int: La longitud de la última palabra.
    """
    # Eliminar espacios al principio y al final y dividir la frase en palabras
    palabras = frase.strip().split()
    
    # Verificar si hay palabras
    if palabras:
        # Retornar la longitud de la última palabra
        return len(palabras[-1])
    else:
        return 0  # Retornar 0 si no hay palabras

# Ejemplo de uso
texto = "   Hola mundo  "
longitud = longitud_ultima_palabra(texto)
print(f"La longitud de la última palabra es: {longitud}")
