# Problema #2
# Version : 1.1
# Fecha : 12/05/2025
# Autores : Diego Urbina, Julio Delgadillo, Emmanuel Aguilar
"""
En una panadería tradicional en León, los panes recién horneados se apilan en una bandeja. El
primero que se vende es el último que se colocó. Simula el proceso de agregar panes a la bandeja
(push), vender uno (pop), y visualizar qué tipo de pan está listo para vender (peek).
"""

# Clase que representa un pan
class Pan:
    def __init__(self, tipo):
        self.tipo = tipo
        self.siguiente = None

# Clase que representa la pila de panes (la bandeja)
class BandejaPanes:
    def __init__(self):
        self.top = None  # Referencia al pan más reciente (último en llegar)

    def agregar_pan(self, tipo):
        nuevo = Pan(tipo)
        nuevo.siguiente = self.top  # El nuevo pan apunta al anterior
        self.top = nuevo            # El nuevo pan ahora es el tope
        print(f"Pan '{tipo}' agregado a la bandeja.")

    def vender_pan(self):
        if self.top is None:
            print("No hay panes para vender.")
            return None
        vendido = self.top
        self.top = self.top.siguiente  # El siguiente pan se convierte en el nuevo tope
        print(f"Pan '{vendido.tipo}' vendido.")
        return vendido.tipo

    def ver_proximo_pan(self):
        if self.top is None:
            print("No hay panes disponibles.")
            return None
        print(f"Pan listo para vender: '{self.top.tipo}'")
        return self.top.tipo

# Ejecución
if __name__ == "__main__":
    bandeja = BandejaPanes()

    while True:
        print("\n--- Menú de la panadería ---")
        print("1. Agregar pan")
        print("2. Vender pan")
        print("3. Ver pan disponible")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo = input("Ingrese el tipo de pan: ")
            bandeja.agregar_pan(tipo)
        elif opcion == "2":
            bandeja.vender_pan()
        elif opcion == "3":
            bandeja.ver_proximo_pan()
        elif opcion == "4":
            print("Cerrando")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
