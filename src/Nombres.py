from typing import List

def nombres() -> None:
    palabra_finalizar: str = "listo"

    finalizado: bool = False
    nombres: List[str] = []

    while (not finalizado):
        palabra: str = input("Ingresar nombre: ")
        
        if palabra != palabra_finalizar:
            nombres.append(palabra)
        else:
            finalizado = True

    print("Los nombres elegidos fueron: " + str(nombres))
