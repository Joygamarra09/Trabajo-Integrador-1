# Definición de funciones


"""Función para mostrar un contacto"""

class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):         #sirve para mostrar el contacto como texto legible cuando haces print(contacto)
        return print(f"{self.nombre} - Tel: {self.telefono}")
    


"""Función para representar categorías"""

class NodoArbol:
    def __init__(self, nombre_categoria):
        self.nombre_categoria = nombre_categoria
        self.contactos = []
        self.subcategorias = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def es_contacto(self):
        return isinstance(self, NodoContacto)

    def mostrar(self, nivel=0):
        indentacion = "  " * nivel
        if self.es_contacto():
            print(indentacion + str(self.contacto))
        else:
            print(indentacion + f"[{self.nombre_categoria}]")
            for hijo in self.hijos:
                hijo.mostrar(nivel + 1)


class NodoContacto(NodoArbol):
    def __init__(self, contacto):
        super().__init__(contacto.nombre)
        self.contacto = contacto




"""
Si este nodo es la categoría buscada (nombre_categoria), 
agrega el contacto y devuelve True para indicar éxito.

"""

def agregar_contacto_a_categoria(raiz, categoria_nombre, contacto):
    if raiz.nombre_categoria == categoria_nombre:
        raiz.agregar_hijo(NodoContacto(contacto))
        return True
    for hijo in raiz.hijos:
        if not hijo.es_contacto():
            if agregar_contacto_a_categoria(hijo, categoria_nombre, contacto):
                return True
    return False

