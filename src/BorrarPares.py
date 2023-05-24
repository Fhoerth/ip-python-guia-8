from typing import List

def es_par(n: int) -> bool:
    return n % 2 == 0

def borrar_pares_1(lista: List[int]) -> List[int]:
    i: int = 0

    while i < len(lista):
        n: int = lista[i]

        if es_par(n):
            lista[i] = 0
        else:
            lista[i] = n

        i += 1

    return lista

def borrar_pares_2(lista: List[int]) -> List[int]:
    i: int = 0
    nueva_lista: List[int] = []

    while i < len(lista):
        n: int = lista[i]

        if es_par(n):
            nueva_lista.append(0)
        else:
            nueva_lista.append(n)

        i += 1

    return nueva_lista
