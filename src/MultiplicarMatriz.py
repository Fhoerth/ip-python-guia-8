from typing import List

import numpy

def matriz_aleatoria(d: int) -> List[List[int]]:
    i: int = 0
    j: int = 0

    matriz: List[List[int]] = []

    while i < d:
        matriz.append([])

        while j < d:
            matriz[i].append(numpy.random.randint(-100, 100))
            j += 1

        j = 0
        i += 1

    return matriz

def multiplicar_matriz_por_si_misma(matriz: List[List[int]]) -> List[List[int]]:
    i: int = 0
    j: int = 0
    
    while i < len(matriz):
        while j < len(matriz):
            matriz[i][j] *= matriz[j][i]
            j += 1
        
        j = 0
        i += 1

    return matriz

def multiplicar_matriz(d: int, p: int) -> List[List[int]]:
    i: int = 0
    matriz: List[List[int]] = matriz_aleatoria(d)

    while i < p:
        matriz = multiplicar_matriz_por_si_misma(matriz)
        i += 1
    
    return matriz
