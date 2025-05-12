# Problema #5
# Version : 1.1
# Fecha : 12/05/2025
# Autores : Diego Urbina, Julio Delgadillo, Emmanuel Aguilar
"""
En un mercado de Chinandega, los sacos con productos se cargan en camiones uno encima de otro.
Al llegar a destino, el primer saco que se descarga es el último que se cargó. Simula este proceso
con una pila que permita apilar sacos (push), descargar uno (pop) y visualizar el que está encima
(peek).
"""

# Clase que representa un saco
class Saco:
    def __init__(self, contenido):
        self.contenido = contenido
        self.siguiente = None

# Clase que representa la pila de sacos en el camión
class PilaSacos:
    def __init__(self):
        self.top = None

    def cargar_saco(self, contenido):
        nuevo = Saco(contenido)
        nuevo.siguiente = self.top
        self.top = nuevo
        print(f"Saco de '{contenido}' cargado al camión.")

    def descargar_saco(self):
        if self.top is None:
            print("No hay sacos para descargar.")
            return None
        descargado = self.top
        self.top = self.top.siguiente
        print(f"Saco de '{descargado.contenido}' descargado del camión.")
        return descargado.contenido

    def ver_saco_superior(self):
        if self.top is None:
            print("No hay sacos en el camión.")
            return None
        print(f"Saco en la cima: '{self.top.contenido}'")
        return self.top.contenido

# Ejecución
if __name__ == "__main__":
    camion = PilaSacos()

    while True:
        print("\n--- Menú de carga del camión ---")
        print("1. Cargar saco")
        print("2. Descargar saco")
        print("3. Ver saco en la cima")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            contenido = input("Ingrese el contenido del saco: ")
            camion.cargar_saco(contenido)
        elif opcion == "2":
            camion.descargar_saco()
        elif opcion == "3":
            camion.ver_saco_superior()
        elif opcion == "4":
            print("Cerrando")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
