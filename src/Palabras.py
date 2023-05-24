from typing import List

def palabras(lista: List[str]) -> bool:
    i: int = 0
    tiene_una_palabra_largo_7: bool = True

    while i < len(lista):
        elemento_de_la_lista: str = lista[i]
        tiene_una_palabra_largo_7 = tiene_una_palabra_largo_7 and len(elemento_de_la_lista) > 7
        
        if tiene_una_palabra_largo_7:
            i = len(lista)
        else:
            i += 1
    
    return tiene_una_palabra_largo_7