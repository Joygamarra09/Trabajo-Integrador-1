# Método para insertar un estudiante en el árbol.
    def insertar(self, estudiante):
        self.raiz = self._insertar_recursivo(self.raiz, estudiante)

# Método recursivo para insertar un estudiante en el árbol de búsqueda.
    def _insertar_recursivo(self, nodo, estudiante):
        if nodo is None:
            return Nodo(estudiante)
        if estudiante.calificacion < nodo.valor.calificacion:
            nodo.izquierda = self._insertar_recursivo(nodo.izquierda, estudiante)
        else:
            nodo.derecha = self._insertar_recursivo(nodo.derecha, estudiante)
        return nodo

#Método para buscar un estudiante por nombre en el árbol.
    def buscar(self, nombre):
        return self._buscar_recursivo(self.raiz, nombre)

#Función recursiva para buscar un estudiante por nombre en el árbol.
    def _buscar_recursivo(self, nodo, nombre):
        if nodo is None:
            return None
        if nodo.valor.nombre.lower() == nombre.lower():
            return nodo.valor
        encontrado = self._buscar_recursivo(nodo.izquierda, nombre)
        if encontrado is None:
            encontrado = self._buscar_recursivo(nodo.derecha, nombre)
        return encontrado