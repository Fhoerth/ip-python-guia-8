from typing import List

def es_matriz(lista: List[List[int]]) -> bool:
    if not lista[0] or len(lista[0]) == 0:
        return False
    
    largo_fila = len(lista[0])
    es_matriz: bool = True
    i: int = 0

    while (i < len(lista)):
        fila = lista[i]
        es_matriz = es_matriz and len(fila) == largo_fila

        i += 1

    return es_matriz
