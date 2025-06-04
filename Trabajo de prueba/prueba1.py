# Definición de clases para el árbol, estudiantes y nodos.
# Este código implementa un árbol de búsqueda binario para almacenar estudiantes y sus calificaciones.

# Desarrollaremos un código que implemente una estructura de árbol de búsqueda en Python, donde se enlistarán estudiantes de una clase y sus respectivas calificaciones.
# Cada estudiante tendrá un nombre y una calificación, y el árbol permitirá insertar estudiantes de manera ordenada según sus calificaciones.

# Definimos una clase ArbolBusqueda que contendrá la raíz del árbol y métodos para insertar estudiantes.
class ArbolBusqueda:


    # Inicializamos el árbol de búsqueda con una raíz vacía.
    def __init__(self):
        self.raiz = None


    # Método para insertar un estudiante en el árbol.    
    def insertar(self, estudiante):
        if self.raiz is None:
            self.raiz = Nodo(estudiante)
        else:
            self._insertar_recursivo(self.raiz, estudiante)

    # Método recursivo para insertar un estudiante en el árbol de búsqueda.
    def _insertar_recursivo(self, nodo, estudiante):
        if estudiante.calificacion < nodo.valor.calificacion:
            if nodo.hijos and nodo.hijos[0]:
                self._insertar_recursivo(nodo.hijos[0], estudiante)
            else:
                nodo.agregar_hijo(Nodo(estudiante))
        else:
            if len(nodo.hijos) > 1 and nodo.hijos[1]:
                self._insertar_recursivo(nodo.hijos[1], estudiante)
            else:
                nodo.agregar_hijo(Nodo(estudiante))

    # Método para buscar un estudiante por nombre en el árbol.
    def __repr__(self):
        return f"ArbolBusqueda(raiz={self.raiz})"
    

# Definimos una clase Estudiante que contendrá el nombre y la calificación del estudiante.
class Estudiante:
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion

    def __repr__(self):
        return f"Estudiante(nombre={self.nombre}, calificacion={self.calificacion})"


# Para la creación de un árbol debemos definir una clase Nodo que contenga un valor y referencias a sus hijos (hijo izquiero, hijo derecho) que serán las posiciones que ocuparan los valores a medida 
# incorporen al árbol.
# Cada nodo contendrá un valor (en este caso, un objeto Estudiante) y una lista de hijos.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

    def agregar_hijo(self, nodo):
        self.hijos.append(nodo)

    def __repr__(self):
        return f"Nodo({self.valor})"
