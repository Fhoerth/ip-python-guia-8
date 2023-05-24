from typing import List

def pertenece_1(lista: List[int], elemento: int) -> bool:
    # range
    for i in range(0, len(lista)):
        elemento_de_la_lista: int = lista[i]

        if elemento == elemento_de_la_lista:
            return True
    
    return False

def pertenece_2(lista: List[int], elemento: int) -> bool:
    # while
    i: int = 0

    while i < len(lista):
        elemento_de_la_lista: int = lista[i]
        
        if elemento_de_la_lista == elemento:
            return True

        i += 1

    return False

def pertenece_3(lista: List[int], elemento: int) -> bool:
    # for in
    for elemento_de_la_lista in lista:
        if elemento_de_la_lista == elemento:
            return True

    return False

pertenece = pertenece_1