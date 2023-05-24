from typing import List

from Ordenados import ordenados
from EsMatriz import es_matriz

def filas_ordenadas(lista: List[List[int]]) -> List[bool]:
    if not es_matriz(lista):
        return None

    filas_ordenadas: List[bool] = []
    i: int = 0

    while i < len(lista):
        fila: lista[int] = lista[i]

        if ordenados(fila):
            filas_ordenadas.append(True)
        else:
            filas_ordenadas.append(False)

        i += 1
    
    return filas_ordenadas
