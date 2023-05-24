from typing import List

def divide_a_todos(lista: List[int], e: int) -> bool:
    if e == 0:
        return False

    i: int = 0
    anteriores_son_divisibles: bool = True

    while i < len(lista):
        elemento_de_la_lista: int = lista[i]
        es_divisible_por_elemento_de_la_lista: bool = elemento_de_la_lista % e == 0
        anteriores_son_divisibles = anteriores_son_divisibles and es_divisible_por_elemento_de_la_lista

        if anteriores_son_divisibles:
            i += 1
        else:
            i = len(lista)

    todos_divisibles: bool = anteriores_son_divisibles

    return todos_divisibles