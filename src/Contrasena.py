from typing import List

def fortaleza_contrasena(contrasena: str) -> str:
    puede_ser_verde: bool = len(contrasena) > 8

    mayusculas: str = ""
    minusculas: str  = ""
    numeros: str = ""

    i: int = 0

    while puede_ser_verde and i < len(contrasena):
        letra: str = contrasena[i]

        es_letra_minuscula: bool = "a" <= letra <= "z"
        es_letra_mayuscula: bool = "A" <= letra <= "Z"
        letra_es_numero: bool = "0" <= letra <= "9"

        if es_letra_minuscula:
            minusculas = minusculas + letra

        if es_letra_mayuscula:
            mayusculas = mayusculas + letra

        if letra_es_numero:
            numeros = numeros + letra

        i += 1

    if len(mayusculas) and len(minusculas) and len(numeros):
        return "VERDE"
    
    if len(contrasena) < 5:
        return "ROJO"
    
    return "AMARILLO"

# def fortaleza_contrasena_con_listas(contrasena: str) -> str:
#     puede_ser_verde: bool = len(contrasena) > 8

#     mayusculas: List[str] = []
#     minusculas: List[str] = []
#     numeros: List[str] = []

#     i: int = 0

#     while puede_ser_verde and i < len(contrasena):
#         letra = contrasena[i]

#         es_letra_minuscula = "a" <= letra <= "z"
#         es_letra_mayuscula = "A" <= letra <= "Z"
#         letra_es_numero = "0" <= letra <= "9"

#         if es_letra_minuscula:
#             minusculas.append(letra)

#         if es_letra_mayuscula:
#             mayusculas.append(letra)

#         if letra_es_numero:
#             numeros.append(letra)

#         i += 1

#     if len(mayusculas) and len(minusculas) and len(numeros):
#         return "VERDE"
    
#     if len(contrasena) < 5:
#         return "ROJO"
    
#     return "AMARILLO"
