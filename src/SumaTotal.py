from typing import List

def suma_total(lista: List[int]) -> int:
    i: int = 0
    suma: int = 0

    while i < len(lista):
        elemento_de_la_lista: int = lista[i]
        suma += elemento_de_la_lista
        i += 1
    
    # for i in range(0, len(lista)):
    #     elemento_de_la_lista: int = lista[i]
    #     suma += elemento_de_la_lista

    # for elemento_de_la_lista in lista:
    #     suma += elemento_de_la_lista

    return suma
