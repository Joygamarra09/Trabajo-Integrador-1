 if opcion == "1":

        nombre = input("Nombre del estudiante: ")

        if not nombre.isalpha() and not nombre.replace(" ", "").isalpha():  # Verificamos que el nombre contenga solo letras o espacios.






        if nombre.isalpha(): # Verificamos que el nombre contenga solo letras.
            nombre = nombre.lower()  # Hacemos el nombre en minúsculas para evitar duplicados por mayúsculas/minúsculas.
            # Verificamos si el nombre ya existe en el árbol.
            if arbol.buscar(nombre):
                print("El estudiante ingresado ya existe.")
                continue
        else:
            print("Nombre inválido. Debe contener solo letras.")
            continue
