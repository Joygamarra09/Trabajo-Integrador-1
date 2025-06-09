#Definición de funciones
    def mostrar_inorden(self, nodo):
        if nodo:
            self.mostrar_inorden(nodo.izquierda) #hijo izquierdo
            print(nodo.valor)
            self.mostrar_inorden(nodo.derecha) #hijo derecho

    def mostrar_preorden(self, nodo):
        if nodo:
            print(nodo.valor)
            self.mostrar_preorden(nodo.izquierda) #hijo izquierdo
            self.mostrar_preorden(nodo.derecha) #hijo derecho

    def mostrar_postorden(self, nodo):
        if nodo:
            self.mostrar_postorden(nodo.izquierda) #hijo izquierdo
            self.mostrar_postorden(nodo.derecha) #hijo derecho
            print(nodo.valor)