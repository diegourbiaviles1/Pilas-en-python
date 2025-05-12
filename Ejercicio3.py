# Problema #3
# Version : 1.1
# Fecha : 12/05/2025
# Autores : Diego Urbina, Julio Delgadillo, Emmanuel Aguilar
"""
En una campaña de donación de sangre en un hospital de Estelí, los datos de los donantes se
almacenan en una pila según el orden en que se procesan. Si ocurre un problema técnico, se debe
revertir el último registro. Implementa un sistema para registrar donantes (push), eliminar el último
(pop), y mostrar el donante actual en proceso.
"""

# Clase que representa a un donante
class Donante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

# Clase que representa la pila de registros de donantes
class RegistroDonantes:
    def __init__(self):
        self.top = None

    def registrar_donante(self, nombre):
        nuevo = Donante(nombre)
        nuevo.siguiente = self.top
        self.top = nuevo
        print(f"Donante '{nombre}' registrado exitosamente.")

    def revertir_registro(self):
        if self.top is None:
            print("No hay registros para revertir.")
            return None
        eliminado = self.top
        self.top = self.top.siguiente
        print(f"Registro del donante '{eliminado.nombre}' ha sido revertido.")
        return eliminado.nombre

    def donante_actual(self):
        if self.top is None:
            print("No hay donantes en proceso.")
            return None
        print(f"Donante en proceso: '{self.top.nombre}'")
        return self.top.nombre

# Ejecución
if __name__ == "__main__":
    registro = RegistroDonantes()

    while True:
        print("\n--- Menú de la campaña de donación ---")
        print("1. Registrar nuevo donante")
        print("2. Revertir último registro")
        print("3. Mostrar donante en proceso")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del donante: ")
            registro.registrar_donante(nombre)
        elif opcion == "2":
            registro.revertir_registro()
        elif opcion == "3":
            registro.donante_actual()
        elif opcion == "4":
            print("Cerrando")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
