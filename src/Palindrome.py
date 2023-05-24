def es_palindrome(palabra: str) -> bool:
    i: int = 0
    j: int = len(palabra) - 1

    palabra_es_palindrome: bool = True

    while i <= j:
      palabra_es_palindrome: bool = palabra_es_palindrome and palabra[i] == palabra[j]

      if palabra_es_palindrome:
          j -= 1
          i += 1
      else:
          i = len(palabra)

    return palabra_es_palindrome