#Definición de funciones

#Métodos para mostrar los estudiantes aprobados y desaprobados.
    def mostrar_aprobados(self, nodo):
        if nodo:
            self.mostrar_aprobados(nodo.izquierda)
            if nodo.valor.calificacion >= 60:
                print(nodo.valor)
            self.mostrar_aprobados(nodo.derecha)

    def mostrar_desaprobados(self, nodo):
        if nodo:
            self.mostrar_desaprobados(nodo.izquierda)
            if nodo.valor.calificacion < 60:
                print(nodo.valor)
            self.mostrar_desaprobados(nodo.derecha)
