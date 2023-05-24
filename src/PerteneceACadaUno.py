from typing import List

from Pertenece import pertenece

def pertenece_a_cada_uno(lista: List[List[int]], n: int) -> bool:
    pertenece_a_todos: bool = True
    i: int = 0

    while i < len(lista):
      sub_lista: List[int] = lista[i]
      pertenece_a_todos = pertenece_a_todos and pertenece(sub_lista, n)

      i += 1

    return pertenece_a_todos