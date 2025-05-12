# Problema #4
# Version : 1.1
# Fecha : 12/05/2025
# Autores : Diego Urbina, Julio Delgadillo, Emmanuel Aguilar
"""
Una docente de informática en una secundaria revisa tareas impresas que sus estudiantes colocan
sobre su escritorio. Siempre revisa primero la última tarea entregada. Implementa un sistema que
permita agregar tareas (push), revisar una (pop), y mostrar cuál es la siguiente en revisar (peek),
todo usando una pila.
"""

# Clase que representa una tarea
class Tarea:
    def __init__(self, estudiante, descripcion):
        self.estudiante = estudiante
        self.descripcion = descripcion
        self.siguiente = None

# Clase que representa la pila de tareas sobre el escritorio
class PilaTareas:
    def __init__(self):
        self.top = None

    def agregar_tarea(self, estudiante, descripcion):
        nueva = Tarea(estudiante, descripcion)
        nueva.siguiente = self.top
        self.top = nueva
        print(f"Tarea de '{estudiante}' agregada: {descripcion}")

    def revisar_tarea(self):
        if self.top is None:
            print("No hay tareas para revisar.")
            return None
        tarea = self.top
        self.top = self.top.siguiente
        print(f"Tarea revisada: '{tarea.descripcion}' de {tarea.estudiante}")
        return tarea

    def tarea_en_proceso(self):
        if self.top is None:
            print("No hay tareas pendientes.")
            return None
        print(f"Siguiente tarea a revisar: '{self.top.descripcion}' de {self.top.estudiante}")
        return self.top

# Ejecución
if __name__ == "__main__":
    escritorio = PilaTareas()

    while True:
        print("\n--- Menú de revisión de tareas ---")
        print("1. Agregar tarea")
        print("2. Revisar tarea")
        print("3. Ver siguiente tarea en proceso")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            estudiante = input("Nombre del estudiante: ")
            descripcion = input("Descripción de la tarea: ")
            escritorio.agregar_tarea(estudiante, descripcion)
        elif opcion == "2":
            escritorio.revisar_tarea()
        elif opcion == "3":
            escritorio.tarea_en_proceso()
        elif opcion == "4":
            print("Cerrando")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
