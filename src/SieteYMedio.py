from typing import List

import random

def generar_carta_aleatoria():
    n = random.randint(0, 12)

    while n == 8 or n == 9:
        n = random.randint(0, 12)

    return n

def puntaje_de_carta(carta: int) -> int:
    if carta < 10:
        return carta
    
    return 0.5

def input_deseas_seguir() -> str:
    return input("Deseas seguir? S/N ")

def preguntar_si_quiere_seguir() -> bool:
    decision_usuario: str = input_deseas_seguir()

    if decision_usuario != 'S' and decision_usuario != 'N':
        decision_usuario = input_deseas_seguir()
    
    if decision_usuario == 'S':
        return True

    return False

def siete_y_medio():
    puntaje: int = 0
    puntaje_limite: int = 7.5
    usuario_quiere_seguir: bool = True
    cartas_elegidas: List[int] = []

    while usuario_quiere_seguir and puntaje <= puntaje_limite:
        usuario_quiere_seguir: str = preguntar_si_quiere_seguir()

        if usuario_quiere_seguir:
            carta_aleatoria: int = generar_carta_aleatoria()
            cartas_elegidas.append(carta_aleatoria)

            puntaje += puntaje_de_carta(carta_aleatoria)

            print("\r")
            print("La carta aleatoria fue: " + str(carta_aleatoria))
            print("Tu nuevo puntaje es: " + str(puntaje))
            print("\r")

    print("\r")

    if not usuario_quiere_seguir and puntaje <= puntaje_limite:
        print("Ganaste!")
    else:
        print("Perdiste!")

    print("Tu puntaje final fue: " + str(puntaje))
    print("Tus cartas elegidas fueron: " + str(cartas_elegidas))


siete_y_medio()