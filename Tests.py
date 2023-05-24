import pytest
import sys

sys.path.insert(0, './src')

from typing import List
from io import StringIO
from unittest import mock

from src.Pertenece import pertenece_1, pertenece_2, pertenece_3
from src.DivideATodos import divide_a_todos
from src.SumaTotal import suma_total
from src.Ordenados import ordenados
from src.Palabras import palabras
from src.Palindrome import es_palindrome
from src.Contrasena import fortaleza_contrasena
from src.Saldo import saldo
from src.VocalesDistintas import tiene_3_vocales_distintas
from src.BorrarPares import borrar_pares_1, borrar_pares_2
from src.Vocales import eliminar_vocales, reemplaza_vocales
from src.DaVueltaStr import da_vuelta_str
from src.PerteneceACadaUno import pertenece_a_cada_uno
from src.EsMatriz import es_matriz
from src.FilasOrdenadas import filas_ordenadas
from src.Nombres import nombres

def simular_respuestas(monkeypatch: pytest.MonkeyPatch, respuestas: List[str]) -> None:
    monkeypatch.setattr('sys.stdin', StringIO('\n'.join(respuestas)))

def obtener_salida(capsys: pytest.LogCaptureFixture, preguntas: List[str]) -> str:
    salida: str = str(capsys.readouterr().out)
    for pregunta in preguntas:
        salida = salida.replace(pregunta, "", 1)
    
    return salida

def test_pertenece_1():
    assert pertenece_1([1], 2) == False, "El elemento 2 no deberia pertenecer a la lista [1]"
    assert pertenece_1([1], -2) == False, "El elemento -2 no deberia pertenecer a la lista [1]"
    assert pertenece_1([-1], 2) == False, "El elemento 2 no deberia pertenecer a la lista [-1]"
    assert pertenece_1([-1], -2) == False, "El elemento -2 no deberia pertenecer a la lista [-1]"
    
    assert pertenece_1([1], 1) == True, "El elemento 1 si deberia pertenecer a lista [1]"
    assert pertenece_1([-1], -1) == True, "El elemento -1 si deberia pertenecer a lista [-1]"
    assert pertenece_1([-1, 0, 1], -1) == True, "El elemento -1 si deberia pertenecer a lista [-1, 0, 1]"
    assert pertenece_1([-1, 0, 1], 1) == True, "El elemento 1 si deberia pertenecer a lista [-1, 0, 1]"

def test_pertenece_2():
    assert pertenece_2([1], 2) == False, "El elemento 2 no deberia pertenecer a la lista [1]"
    assert pertenece_2([1], -2) == False, "El elemento -2 no deberia pertenecer a la lista [1]"
    assert pertenece_2([-1], 2) == False, "El elemento 2 no deberia pertenecer a la lista [-1]"
    assert pertenece_2([-1], -2) == False, "El elemento -2 no deberia pertenecer a la lista [-1]"
    
    assert pertenece_2([1], 1) == True, "El elemento 1 si deberia pertenecer a lista [1]"
    assert pertenece_2([-1], -1) == True, "El elemento -1 si deberia pertenecer a lista [-1]"
    assert pertenece_2([-1, 0, 1], -1) == True, "El elemento -1 si deberia pertenecer a lista [-1, 0, 1]"
    assert pertenece_2([-1, 0, 1], 1) == True, "El elemento 1 si deberia pertenecer a lista [-1, 0, 1]"

def test_pertenece_3():
    assert pertenece_3([1], 2) == False, "El elemento 2 no deberia pertenecer a la lista [1]"
    assert pertenece_3([1], -2) == False, "El elemento -2 no deberia pertenecer a la lista [1]"
    assert pertenece_3([-1], 2) == False, "El elemento 2 no deberia pertenecer a la lista [-1]"
    assert pertenece_3([-1], -2) == False, "El elemento -2 no deberia pertenecer a la lista [-1]"
    
    assert pertenece_3([1], 1) == True, "El elemento 1 si deberia pertenecer a lista [1]"
    assert pertenece_3([-1], -1) == True, "El elemento -1 si deberia pertenecer a lista [-1]"
    assert pertenece_3([-1, 0, 1], -1) == True, "El elemento -1 si deberia pertenecer a lista [-1, 0, 1]"
    assert pertenece_3([-1, 0, 1], 1) == True, "El elemento 1 si deberia pertenecer a lista [-1, 0, 1]"

def test_divide_a_todos():
    lista: List[int] = [-5, -3, -2, -1, 0, 1, 2, 3, 5]

    assert divide_a_todos(lista, 0) == False, "No se deberia poder dividir por 0"
    assert divide_a_todos(lista, -2) == False, "-2 no deberia dividir a todos los numeros de la lista"
    assert divide_a_todos(lista, 2) == False, "2 no deberia dividir a todos los numeros de la lista"
    assert divide_a_todos(lista, 1) == True, "1 deberia poder dividir a todos"
    assert divide_a_todos(lista, -1) == True, "-1 no deberia poder dividir a todos"
    assert divide_a_todos([], -1) == True, "-1 deberia poder dividir a todos en una lista vacia"
    assert divide_a_todos([], 1) == True, "1 deberia poder dividir a todos en una lista vacia"

    assert divide_a_todos([-6, -4, -2, 4, 6, 8, 10], 2) == True, "2 deberia poder dividir a todos"

def test_suma_total():
    assert suma_total([]) == 0, "Deberia devolver 0 para una lista vacia"
    assert suma_total([1, 2, 3, 4, 5]) == 15, "Deberia sumar numeros positivos"
    assert suma_total([-1, -2, -3, -4, -5]) == -15, "Deberia sumar numeros negativos"
    assert suma_total([-1, -2, -3, -4, -5, 1, 2, 3, 4, 5]) == 0, "Deberia sumar numeros positivos y negativos"

def test_ordenados():
    # lista desordenada cualquiera (negativos + 0 + positivos)
    # lista desordenada de positivos
    # lista desordenada de negativos
    # lista desordenada de dos elementos

    # lista ordenada cualquiera (negativos + 0 + positivos)
    # lista ordenada de positivos
    # lista ordenada de negativos

    # lista de un elemento
    # lista de dos elementos ordenados
    # lista vacia
    
    assert ordenados([2, 1, 0, -3, -5]) == False, "Deberia devolver False para una lista desordenada cualquiera (positivos y negativos)"
    assert ordenados([2, 1, 0]) == False, "Deberia devolver False para una lista desordenada de positivos"
    assert ordenados([0, -1, -2]) == False, "Deberia devolver False para una lista desordenada de negativos"
    assert ordenados([1, -1]) == False, "Deberia devolver False para una lista desordenada de dos elementos"
    assert ordenados([0, 1, 2, 3, -1]) == False, "Deberia devolver False para una lista desordenada que tiene elementos ordenados al principio"
    assert ordenados([-1, -2, 0, 1, 2]) == False, "Deberia devolver False para una lista desordenada que tiene elementos ordenados al final"

    assert ordenados([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == True, "Deberia devolver True para una lista ordenada de numeros positivos y negativos"
    assert ordenados([1, 2, 3, 4, 5]) == True, "Deberia devolver True para una lista ordenada de positivos"
    assert ordenados([-5, -4, -3, -2, -1]) == True, "Deberia devolver True para una lista ordenada de negativos"

def test_palabras():
    assert palabras(["12345678", "123", "456", "7"]) == True, "Deberia devolver True para una lista que contiene un elemento de 8 letras"
    assert palabras(["0", "123", "456", "7"]) == False, "Deberia devolver False para una lista que no contiene un elemento de 7 palabras"

def test_es_palindrome():
    assert es_palindrome("menem") == True, "Deberia devolver True para una palabra palindrome de numero de letras impares"
    assert es_palindrome("foooof") == True, "Deberia devolver True para una palabra palindrome de numero de letras pares"
    assert es_palindrome("sabado") == False, "Deberia devolver False para una palabra no palindrome"

def test_fortaleza_contrasena():
    # VERDE:
        # Mas de 8 caracteres (estricto)
        # Tiene al menos una letra minuscula
        # Tiene al menos una letra mayuscula
        # Tiene al menos un digito
    # AMARILLO: entre 8 y 5 caracteres (no estricto)
    # ROJO: menos de 5 caracteres (estricto)

    assert fortaleza_contrasena("a2B45678j") == "VERDE", "Deberia devolver `verde` para una contraseña fuerte"
    assert fortaleza_contrasena("2aB45678j") == "VERDE", "Deberia devolver `verde` para una contraseña que tiene un numero al principio"
    assert fortaleza_contrasena("a2B4567j8") == "VERDE", "Deberia devolver `verde` para una contraseña que tiene un numero al final"
    assert fortaleza_contrasena("B2a45678j") == "VERDE", "Deberia devolver `verde` para una contraseña que tiene una mayuscula al principio"
    assert fortaleza_contrasena("a2j45678B") == "VERDE", "Deberia devolver `verde` para una contraseña que tiene una mayuscula al final"

    assert fortaleza_contrasena("a2B4568e") == "AMARILLO", "Deberia devolver `amarillo` aunque cumpla con las condiciones fuertes pero tiene 8 caracteres"
    assert fortaleza_contrasena("abcdefgh") == "AMARILLO", "Deberia devolver `amarillo` aunque no cumpla con las condiciones fuertes pero tiene 8 caracteres"
    assert fortaleza_contrasena("12345") == "AMARILLO", "Deberia devolver `amarillo` si la palabra tiene 5 caracteres"

    assert fortaleza_contrasena("1234") == "ROJO", "Deberia `rojo` si tiene menos de 5 caracteres"


def test_saldo():
    assert saldo([("R", 1), ("R", 10), ("R", 1000)]) == -1011, "Deberia devolver saldo negativo si las operaciones son solo de retiro"
    assert saldo([("R", 1), ("I", 1000), ("R", 10), ("R", 1000)]) == -11, "Deberia devolver saldo negativo si hay operaciones mixtas"

    assert saldo([("I", 1), ("I", 10), ("I", 1000)]) == 1011, "Deberia devolver saldo positivo si las operaciones son solo de ingreso"
    assert saldo([("R", 1), ("R", 10), ("R", 1000), ("I", 1000000)]) == 998989, "Deberia devolver saldo positivo si hay operaciones mixtas"


def test_tiene_3_vocales_distintas():
    assert tiene_3_vocales_distintas("aei") == True, "Deberia devolver verdadero si tiene 3 vocales distintas"
    assert tiene_3_vocales_distintas("aooa") == False, "Deberia devolver falso si no tiene 3 vocales distintas"


def test_borrar_pares():
    lista1: List[int] = [1, 2, 3, 4, 5, 6]
    lista2: List[int] = [-1, -2, -3, -4, -5, -6]
    lista3: List[int] = [-1, -2, -3, -4, -5, -6, 0, 1, 2, 3, 4, 5]

    assert borrar_pares_1(list(lista1)) == [1, 0, 3, 0, 5, 0], "Deberia borrar los pares de una lista sin negativos"
    assert borrar_pares_1(list(lista2)) == [-1, 0, -3, 0, -5, 0], "Deberia borrar los pares de una lista con negativos"
    assert borrar_pares_1(list(lista3)) == [-1, 0, -3, 0, -5, 0, 0, 1, 0, 3, 0, 5], "Deberia borrar los pares de una lista mixta"

    assert borrar_pares_2(lista1) == [1, 0, 3, 0, 5, 0], "Deberia borrar los pares de una lista sin negativos"
    assert borrar_pares_2(lista2) == [-1, 0, -3, 0, -5, 0], "Deberia borrar los pares de una lista con negativos"
    assert borrar_pares_2(lista3) == [-1, 0, -3, 0, -5, 0, 0, 1, 0, 3, 0, 5], "Deberia borrar los pares de una lista mixta"

    # Asegura que no se haynan mutado las listas originales
    assert lista1 == [1, 2, 3, 4, 5, 6]
    assert lista2 == [-1, -2, -3, -4, -5, -6]
    assert lista3 == [-1, -2, -3, -4, -5, -6, 0, 1, 2, 3, 4, 5]

def test_eliminar_vocales():
    assert eliminar_vocales('abcdeghi') == 'bcdgh', "Deberia borrar las vocales de una palabra"

def test_reemplaza_vocales():
    assert reemplaza_vocales('abcdeghi') == '_bcd_gh_', "Deberia reemplazar las vocales por guiones bajos"

def test_da_vuelta_str():
    assert da_vuelta_str("menem") == "menem", "No da vuelta una palabra palindrome"
    assert da_vuelta_str("abcdef") == "fedcba", "Da vuelta una palabra"

def test_pertenece_a_cada_uno():
    sub_lista_1: List[int] = [-2, -1, 0, 1, 2]
    sub_lista_2: List[int] = [2, 2, 2, 2, 2]
    sub_lista_3: List[int] = [3, 3, 3, 3, 3]
    sub_lista_4: List[int] = [1, 2, 3, 4, 5]

    assert pertenece_a_cada_uno([sub_lista_2, sub_lista_3], 0) == False, "0 no debería pertenece a ninguna de las listas"
    assert pertenece_a_cada_uno([sub_lista_2, sub_lista_3], 2) == False, "2 debería pertenecer a la primera lista, pero no a la segunda"
    assert pertenece_a_cada_uno([sub_lista_2, sub_lista_3], 3) == False, "3 debería pertenecer a la segunda lista, pero no a la primera"

    assert pertenece_a_cada_uno([sub_lista_4, sub_lista_4, sub_lista_4], 1) == True, "1 debería pertenecer a todas las listas"
    assert pertenece_a_cada_uno([sub_lista_4, sub_lista_4, sub_lista_4], 3) == True, "3 debería pertenecer a todas las listas"
    assert pertenece_a_cada_uno([sub_lista_4, sub_lista_4, sub_lista_4], 4) == True, "4 debería pertenecer a todas las listas"

    assert pertenece_a_cada_uno([sub_lista_4, sub_lista_4, sub_lista_2], 2) == True, "2 debería pertenecer a todas las listas"
    assert pertenece_a_cada_uno([sub_lista_4, sub_lista_4, sub_lista_3], 3) == True, "3 debería pertenecer a todas las listas"

def esMatriz():
    sub_lista_1: List[int] = [1, 2, 3, 4, 5]
    sub_lista_2: List[int] = [6, 7, 8, 9]

    assert es_matriz([sub_lista_1, sub_lista_2]) == False, "Debería devolver falso si el largo de alguna de las filas no coincide con el resto"
    assert es_matriz([sub_lista_1, sub_lista_1]) == False, "Debería devolver verdadero si el largo de todas las filas no coinciden"

def test_filas_ordenadas():
    sub_lista_ordenada: List[int] = [-2, -1, 0, 1, 2]
    sub_lista_desordenada: List[int] = [-2, -1, 0, 2, 1]

    assert filas_ordenadas([sub_lista_desordenada, sub_lista_desordenada]) == [False, False], "Debería devolver una lista de valores Falso para listas desordenadas"
    assert filas_ordenadas([sub_lista_ordenada, sub_lista_desordenada]) == [True, False], "Debería devolver una lista de valores Verdadero y Falso para una lista ordenada y una desordenada"
    assert filas_ordenadas([sub_lista_desordenada, sub_lista_ordenada]) == [False, True], "Debería devolver una lista de valores falso y verdadero para una lista desordenada y una ordenada"
    assert filas_ordenadas([sub_lista_ordenada, sub_lista_ordenada]) == [True, True], "Debería devolver una lista de valores verdaderos para listas ordenadas"

def test_nombres(monkeypatch, capsys):
    # 1. Respetar bien los espacios de las preguntas. Deben coincidir con los strings utilizados en la función `input`.
    preguntas: List[str] = ['Ingresar nombre: ', 'Ingresar nombre: ', 'Ingresar nombre: ']
    respuestas: str = ['John', 'Doe', 'listo']

    # 2. Verificar que la cantidad de respuestas coincida con la cantidad de preguntas
    assert len(respuestas) == len(preguntas), "El número de preguntas coincide con el número de respuestas"
    
    # 3. Patch unput
    simular_respuestas(monkeypatch, respuestas)
    
    # 4. Ejecuto funcion
    nombres()

    #5. Capturar salida
    salida: str = obtener_salida(capsys, preguntas)

    # 8. Testear la salida
    assert salida == "Los nombres elegidos fueron: ['John', 'Doe']\n"
