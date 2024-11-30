# #Recientemente Candy Crush Saga le pide una variación del juego a U.T.N para 
# su juego de consola con los siguientes requerimientos:
#Dada la siguiente lista de diccionarios
#● lista = [
#● {"piezas":[]},
#● {"piezas":[]},
#● {"piezas":[]},
#● {"piezas":[]}
#● ]
#
#Desarrollar una función que genere números al azar entre 1 y 3, y completar las 
# listas para que queden de la siguiente forma:
# Ej:
# ● [2, 3, 3, 3, 3, 3, 1]
# ● [1, 1, 1, 1, 1, 1, 3]
# ● [3, 1, 2, 3, 1, 1, 1]
# ● [1, 1, 3, 2, 3, 2, 2]
# (los número son generados al azar)
#
#
#Solicitar al usuario una posición (fila y una columna)
#Verificar si, de forma vertical, existen desde esa posición elegida, 
#hacia arriba o hacia abajo 3 números iguales, es decir 3 unos, 3 dos o 3 tres.
#Si existen mostra el mensaje "HA GANADO 10 PUNTOS", sino "SEGUI PARTICIPANDO"
# Utilizar funciones, validar el ingreso de datos

from random import *

def generar_tablero(filas, columnas, clave, inicio_random:int, fin_random:int)->list:
    
    matriz = []
    for i in range(filas):
        diccionario_filas = {clave:[]}
        matriz.append(diccionario_filas) 
        for j in range(columnas):
            numero = randint(inicio_random,fin_random)
            matriz[i][clave].append(numero)
    return matriz

def validar_rango(numero, desde, hasta)->float | int:
    """Valida el numero en un rango, y lo pide indefinidamente hasta que este validado
    Una vez validado, lo retorna"""
    while numero< desde or numero > hasta:
        numero = int(input(f"Ingreso, no valido. Ingrese un numero ({desde+1}-{hasta+1}): "))
    return numero


def ingresar_validar_fila(desde=0, hasta=9)->int:
    """Solicita y valida una posicion(fila) al usuario"""
    
    fila = int(input(f"¿En que fila se encuentra? ({desde+1}/{hasta+1})"))
    fila = validar_rango(fila-1, desde, hasta)   
    return fila 

def ingresar_validar_columna(desde=0, hasta=9)->int:
    """Solicita y valida una posicion(columna) al usuario"""
    columna = int(input(f"¿En que columna se encuentra? ({desde+1}/{hasta+1})"))
    columna = validar_rango(columna-1, desde, hasta)
    return columna

def mostrar_lista(lista:list):
    """Ingresa una lista por parametro y la muestra con un for"""
    for e_lista in lista:
        print(e_lista)


def numero_en_posicion (lista, fila, clave, columna)->int:
    """Ingresa por parametro una lista, una fila, una clave y una columna.
    y retorna el numero que se encuentra en esa posicion"""
    numero = lista[fila][clave][columna]
    return numero


def revisar_fila_anterior (tablero, fila, clave, columna, numero)->bool:
    """Ingresa el tablero, la posicion (fila y columna)
    y el numero con el que compara
    Devuelve True si lo encuentra en la misma columna pero la fila anterior"""
    if tablero[fila - 1][clave][columna] == numero:
        return True
    
def revisar_fila_siguiente (tablero, fila, clave, columna, numero)->bool:
    """Ingresa el tablero, la posicion (fila y columna)
    y el numero con el que compara
    Devuelve True si lo encuentra en la misma columna pero la fila siguiente"""
    if tablero[fila + 1][clave][columna] == numero:
        return True
    
def revisar_filas(tablero, fila, clave, columna, numero)->bool:
    """ Ingresa por parametro el tablero, la fila por la cual ingresar, 
    la clave del diccionario, la columna elegida, y el numero a comprar.
    Retorna True si acerto el juego"""

    bandera_ganador = False
    if fila == 0:
        if revisar_fila_siguiente(tablero, fila, clave, columna, numero):
            fila += 1  #Para usar la funcion y que revise la fila siguiente de la siguiente
            if revisar_fila_siguiente(tablero, fila, clave, columna, numero):
                bandera_ganador = True

    elif fila == 1: 
        if revisar_fila_anterior(tablero, fila, clave, columna, numero):
            if revisar_fila_siguiente(tablero, fila, clave, columna, numero):
                bandera_ganador = True
        elif revisar_fila_siguiente(tablero, fila, clave, columna, numero):
            fila += 1  #Para usar la funcion y que revise la fila siguiente de la siguiente
            if revisar_fila_siguiente(tablero, fila, clave, columna, numero):
                bandera_ganador = True
    elif fila == 2:
        if revisar_fila_siguiente(tablero, fila, clave, columna, numero):
            if revisar_fila_anterior(tablero, fila, clave, columna, numero):
                bandera_ganador = True
        elif revisar_fila_anterior(tablero, fila, clave, columna, numero):
            fila -=1
            if revisar_fila_anterior(tablero, fila, clave, columna, numero):
                bandera_ganador = True
    else:
        if revisar_fila_anterior(tablero, fila, clave, columna, numero):
            fila -= 1   #Para usar la funcion y que revise la fila ANTERIOR de la anterior
            if revisar_fila_anterior(tablero, fila, clave, columna, numero):
                bandera_ganador = True
    
    return bandera_ganador

def ganador(bandera_ganador:bool):
    if bandera_ganador:
        print("HA GANADO 10 PUNTOS")
    else:
        print("SEGUI PARTICIPANDO")




filas = 4
columnas = 7
clave = "Piezas"
inicio_piezas = 1
fin_piezas = 3
bandera_ganador = False

'''
tablero = generar_tablero(filas, columnas, clave, inicio_piezas, fin_piezas)
mostrar_lista(tablero)
print("Usted ingresara una posicion")
fila = ingresar_validar_fila(0,3)
columna = ingresar_validar_columna(0,6)
numero =  numero_en_posicion(tablero, fila, clave, columna)  #Guarda el numero en la posicion ingresada por el usuario
print(f"La fila elegida es {fila}")         #Chequeo
print(f"La columna elegida es {columna}")   #Chequeo
print(numero)                               #Chequeo

#------------------------------------------------------------

'''

