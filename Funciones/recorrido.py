#Definición de funciones


"""Funciones para el recorrido del árbol"""

def preorden(arbol):
    if arbol:
        print(arbol[0], end=' ')
        preorden(arbol[1])
        preorden(arbol[2])


def inorden(arbol):
    if arbol:
        inorden(arbol[1])
        print(arbol[0], end=' ')
        inorden(arbol[2])


def postorden(arbol):
    if arbol:
        postorden(arbol[1])
        postorden(arbol[2])
        print(arbol[0], end=' ')

