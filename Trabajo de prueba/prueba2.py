
# Definimos una clase ArbolBusqueda que contendrá la raíz del árbol y 
# métodos para insertar estudiantes.
class ArbolBusqueda:
     # Inicializamos el árbol de búsqueda con una raíz vacía.
    def __init__(self):
        self.raiz = None

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
    
    def _buscar_recursivo(self, nodo, nombre):
        if nodo is None:
            return None
        if nodo.valor.nombre == nombre:
            return nodo.valor
        encontrado = self._buscar_recursivo(nodo.izquierda, nombre)
        if encontrado is None:
            encontrado = self._buscar_recursivo(nodo.derecha, nombre)
        return encontrado

    def mostrar_inorden(self, nodo):
        if nodo:
            self.mostrar_inorden(nodo.izquierda) #hijo izquierdo
            print(nodo.valor)
            self.mostrar_inorden(nodo.derecha) #hijo derecho

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
    
    # Definimos una clase Estudiante que contendrá el nombre y la calificación del estudiante.
class Estudiante:
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion

    def __repr__(self):
        return f"{self.nombre} - {self.calificacion}"

# Para la creación de un árbol debemos definir una clase Nodo que contenga un valor y referencias a sus hijos
class Nodo:
    def __init__(self, estudiante):
        self.valor = estudiante
        self.izquierda = None
        self.derecha = None


   


# -------------------- Menú --------------------

def menu():
    print("--- Menú Gestor de Calificaciones ---")
    print("1. Insertar estudiante")
    print("2. Buscar estudiante")
    print("3. Mostrar todos (inorden)")
    print("4. Mostrar aprobados (>= 60)")
    print("5. Mostrar desaprobados (< 60)")
    print("6. Salir")
    return input("Seleccione una opción: ")


# -------------------- Programa Principal --------------------

arbol = ArbolBusqueda()

# Insertamos algunos estudiantes iniciales
for nombre, nota in [("Alicia", 85), ("Bastian", 75), ("Carlos", 90), ("David", 55), ("Emily", 95)]:
    arbol.insertar(Estudiante(nombre, nota))

while True:
    opcion = menu()

    if opcion == "1":
        nombre = input("Nombre del estudiante: ")
        try:
            nota = float(input("Calificación (1 a 100): "))
            if 0 <= nota <= 100:
                arbol.insertar(Estudiante(nombre, nota))
                print("Estudiante insertado.")
            else:
                print(" Calificación inválida.")
        except ValueError:
            print(" Entrada no válida.")

    elif opcion == "2":
        nombre = input("Nombre a buscar: ")
        resultado = arbol.buscar(nombre)
        if resultado:
            print(f"Encontrado: {resultado}")
        else:
            print("Estudiante no encontrado.")

    elif opcion == "3":
        print("--- Estudiantes (inorden) ---")
        arbol.mostrar_inorden(arbol.raiz)

    elif opcion == "4":
        print("\n--- Aprobados (>= 60) ---")
        arbol.mostrar_aprobados(arbol.raiz)

    elif opcion == "5":
        print("\n--- Desaprobados (< 60) ---")
        arbol.mostrar_desaprobados(arbol.raiz)

    elif opcion == "6":
        print("Saliendo...")
        break

    else:
        print("Opción inválida.")
