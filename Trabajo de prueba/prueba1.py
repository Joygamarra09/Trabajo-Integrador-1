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

# Creación de un árbol de búsqueda binario.
arbol = ArbolBusqueda()

# Inserción de estudiantes en el árbol.
print("Insertando estudiantes en el árbol de búsqueda...")
estudiantes = [
    Estudiante("Alicia", 85),
    Estudiante("Bastian", 75),
    Estudiante("Carlos", 90),
    Estudiante("David", 60),
    Estudiante("Emily", 95)
]

# print(raíz.hijos) #Sirve para verificar los hijos del nodo raíz.

#Ciclo iterador para mostrar los estudiantes que se agregaron en el árbol.
for estudiante in estudiantes:
    arbol.insertar(estudiante)
    print(f"Estudiante incorporado: {estudiante}")

# Menú de opciones para interactuar con el árbol.
# Definimos una función para mostrar el menú de opciones.
def menu():
    print("\nMenú de opciones:")
    print("1. Insertar estudiante")
    print("2. Mostrar árbol")
    print("3. Buscar estudiante")
    print("4. Eliminar estudiante")
    print("5. Actualizar calificación")
    print("6. Mostrar estudiantes ordenados por calificación")
    print("7. Mostrar estudiantes aprobados (calificación >= 60)")
    print("8. Mostrar estudiantes desaprobados")
    print("9. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

# Bucle principal para interactuar con el árbol.
while True:
    opcion = menu()
    
    if opcion == "1":
        nombre = input("Ingrese el nombre del estudiante: ")
        calificacion = float(input("Ingrese la calificación del estudiante: "))
        nuevo_estudiante = Estudiante(nombre, calificacion)
        arbol.insertar(nuevo_estudiante)
        print(f"Estudiante {nombre} con calificación {calificacion} insertado en el árbol.")
    

    elif opcion == "2":
        print("Árbol de búsqueda actual:")
        print(arbol)
    

    elif opcion == "3":
        nombre = input("Ingrese el nombre del estudiante a buscar: ")
        encontrado = False
        for nodo in arbol.raiz.hijos:
            if nodo.valor.nombre == nombre:
                print(f"Estudiante encontrado: {nodo.valor}")
                encontrado = True
                break
        if not encontrado:
            print(f"Estudiante {nombre} no encontrado en el árbol.")


    elif opcion == "4":
        nombre = input("Ingrese el nombre del estudiante a eliminar: ")
        encontrado = False
        for nodo in arbol.raiz.hijos:
            if nodo.valor.nombre == nombre:
                arbol.raiz.hijos.remove(nodo)
                print(f"Estudiante {nombre} eliminado del árbol.")
                encontrado = True
                break
        if not encontrado:
            print(f"Estudiante {nombre} no encontrado en el árbol.")


    elif opcion == "5":
        nombre = input("Ingrese el nombre del estudiante a actualizar: ")
        nueva_calificacion = float(input("Ingrese la nueva calificación: "))
        encontrado = False
        for nodo in arbol.raiz.hijos:
            if nodo.valor.nombre == nombre:
                nodo.valor.calificacion = nueva_calificacion
                print(f"Calificación de {nombre} actualizada a {nueva_calificacion}.")
                encontrado = True
                break
        if not encontrado:
            print(f"Estudiante {nombre} no encontrado en el árbol.")


    elif opcion == "6":
        print("Estudiantes ordenados por calificación:")
        estudiantes_ordenados = sorted(arbol.raiz.hijos, key=lambda x: x.valor.calificacion)
        for nodo in estudiantes_ordenados:
            print(nodo.valor)


    elif opcion == "7":
        print("Estudiantes con calificación de aprobación (mayor o igual a 60):")
        estudiantes_aprobados = [nodo.valor for nodo in arbol.raiz.hijos if nodo.valor.calificacion >= 60]
        if estudiantes_aprobados:
            for estudiante in estudiantes_aprobados:
                print(estudiante)
        else:
            print("No hay estudiantes aprobados.")

    elif opcion == "8":
        print("Estudiantes desaprobados (calificación menor a 60):")
        estudiantes_desaprobados = [nodo.valor for nodo in arbol.raiz.hijos if nodo.valor.calificacion < 60]
        if estudiantes_desaprobados:
            for estudiante in estudiantes_desaprobados:
                print(estudiante)
        else:
            print("No hay estudiantes desaprobados.")
    elif opcion == "9":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")
