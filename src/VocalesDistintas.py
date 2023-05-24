from typing import List

from Pertenece import pertenece

def es_vocal(letra: str) -> bool:
    return letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"

def tiene_3_vocales_distintas(palabra: str) -> bool:
    vocales_distintas_en_palabra: List[str] = []
    letras: List[str] = list(palabra)

    i: int = 0

    while len(letras):
        letra: str = letras.pop()

        if es_vocal(letra) and not pertenece(letras, letra):
            vocales_distintas_en_palabra.append(letra)

    return len(vocales_distintas_en_palabra) >= 3
