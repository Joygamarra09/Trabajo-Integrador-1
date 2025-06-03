#Definición de funciones

"""Función para mostrar el árbol por pantalla"""

def mostrar_arbol_n_ario(nodo, nivel=0):
    indentacion = "  " * nivel
    print(f"{indentacion}- {nodo.nombre}")
    for contacto in nodo.contactos:
        print(f"{indentacion}  📇 {contacto}")
    for hijo in nodo.hijos:
        mostrar_arbol_n_ario(hijo, nivel + 1)



