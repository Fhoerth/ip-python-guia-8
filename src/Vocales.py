def es_vocal(letra: str) -> bool:
    letra_minuscula = letra.lower()

    return letra_minuscula == "a" or \
           letra_minuscula == "e" or \
           letra_minuscula == "i" or \
           letra_minuscula == "o" or \
           letra_minuscula == "u"

def eliminar_vocales(palabra: str) -> str:
    sin_vocales: str = ''
    i: int = 0

    while i < len(palabra):
        letra: str = palabra[i]

        if not es_vocal(letra):
            sin_vocales += letra
        
        i += 1

    return sin_vocales

def reemplaza_vocales(palabra: str) -> str:
    vocales_reemplazadas: str = ''
    i: int = 0

    while i < len(palabra):
        letra: str = palabra[i]

        if es_vocal(letra):
            vocales_reemplazadas += "_"
        else:
            vocales_reemplazadas += letra

        i += 1

    return vocales_reemplazadas
