from typing import List

def preguntar_por_tipo_operacion() -> str:
    decision_usuario: str = input("Qué operacion deseas realizar? Cargar (C) / Descontar (D) / Finalizar (X) ")

    if decision_usuario != 'C' and decision_usuario != 'D' and decision_usuario != 'X':
        print("Respuesta incorrecta")
        return preguntar_por_tipo_operacion()
    
    return decision_usuario

def preguntar_por_monto_positivo() -> int:
    decision_usuario: str = input("Cuánto dinero deseas ingresar? ")

    return int(decision_usuario)

def preguntar_por_monto_negativo() -> int:
    decision_usuario: str = input("Cuánto dinero deseas descontar? ")

    return int(decision_usuario)

def calcular_monto_total(operaciones: List[tuple[str, int]]) -> int:
    i: int = 0
    monto: int = 0
    
    while i < len(operaciones):
        operacion: tuple[str, int] = operaciones[i]
        tipo_operacion: str = operacion[0]
        monto_operacion: int = operacion[1]

        if tipo_operacion == "C":
            monto += monto_operacion

        if tipo_operacion == "D":
            monto -= monto_operacion

        i += 1

    return monto

def sube() -> None:
    operaciones: List[tuple[str, int]] = []
    finalizado: bool = False

    while not finalizado:
        decision_usuario: str = preguntar_por_tipo_operacion()

        if decision_usuario == "X":
            finalizado = True
        
        elif decision_usuario == "C":
            cantidad: int = preguntar_por_monto_positivo()
            operaciones.append(("C", cantidad))
        
        elif decision_usuario == "D":
            cantidad: int = preguntar_por_monto_negativo()
            operaciones.append(("D", cantidad))

    print("\r")
    print("Tus operaciones fueron: " + str(operaciones))
    print("Tu monto total es: " + str(calcular_monto_total(operaciones)))

sube()