# Definición de funciones


"""Función para mostrar un contacto"""

class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):         #sirve para mostrar el contacto como texto legible cuando haces print(contacto)
        return print(f"{self.nombre} - Tel: {self.telefono}")
    

