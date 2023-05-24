from typing import List

def es_retiro(operacion: tuple[str, int]) -> bool:
    return operacion[0] == "R"

def es_ingreso(operacion: tuple[str, int]) -> bool:
    return operacion[0] == "I"

def monto_operacion(operacion: tuple[str, int]) -> int:
    return operacion[1]

def saldo(operaciones: List[tuple[str, int]]) -> int:
    monto_total: int = 0
    i: int = 0

    while i < len(operaciones):
        operacion: tuple[str, int] = operaciones[i]

        if es_retiro(operacion):
            monto_total -= monto_operacion(operacion)

        if es_ingreso(operacion):
            monto_total += monto_operacion(operacion)

        i += 1

    return monto_total
