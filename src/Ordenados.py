from typing import List

def ordenados(lista: List[int]) -> bool:
    i: int = 0
    anteriores_estan_ordenados: bool = True

    while i < len(lista) - 1:
        elemento_de_la_lista: int = lista[i]
        siguiente_elemento_de_la_lista: int = lista[i + 1]
        anteriores_estan_ordenados = anteriores_estan_ordenados and elemento_de_la_lista < siguiente_elemento_de_la_lista
        i += 1

    todos_ordenados: bool = anteriores_estan_ordenados

    return todos_ordenados