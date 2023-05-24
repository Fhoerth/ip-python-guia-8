def da_vuelta_str(palabra: str) -> str:
    palabra_invertida: str = ''
    j: int = len(palabra) - 1
    
    while j >= 0:
      letra: str = palabra[j]
      palabra_invertida += letra
      j -= 1

    return palabra_invertida