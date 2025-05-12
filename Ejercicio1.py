# Problema #1
# Version : 1.1
# Fecha : 12/05/2025
# Autores : Diego Urbina, Julio Delgadillo, Emmanuel Aguilar
"""
Una oficina de atención ciudadana en una alcaldía municipal en Nicaragua recibe documentos para
revisión. Por cada solicitud, se apilan los documentos entregados en el orden en que llegan. El
personal debe revisar el último documento entregado primero. Se debe simular el proceso de
revisión, utilizando una pila, y permitir agregar nuevos documentos, eliminar el último revisado y
mostrar los pendientes.
"""

# Clase que representa un documento
class Documento:
    def __init__(self, codigo):
        self.codigo = codigo
        self.siguiente = None

# Clase que representa la pila de documentos
class PilaDocumentos:
    def __init__(self):
        self.top = None  # Inicio de la pila
        self.tamanio = 0

    def agregar_documento(self, codigo):
        nuevo = Documento(codigo)
        nuevo.siguiente = self.top
        self.top = nuevo
        self.tamanio += 1
        print(f"Documento '{codigo}' agregado.")

    def revisar_documento(self):
        if self.top is None:
            print("No hay documentos para revisar.")
            return None
        revisado = self.top
        self.top = self.top.siguiente
        self.tamanio -= 1
        print(f"Documento '{revisado.codigo}' revisado y eliminado.")
        return revisado.codigo

    def mostrar_pendientes(self):
        if self.top is None:
            print("No hay documentos pendientes.")
            return
        actual = self.top
        print("\nDocumentos pendientes (de más reciente a más antiguo):")
        while actual:
            print(f"- {actual.codigo}")
            actual = actual.siguiente

# Ejecución
if __name__ == "__main__":
    oficina = PilaDocumentos()

    while True:
        print("\n--- Menú de opciones ---")
        print("1. Agregar documento")
        print("2. Revisar documento (eliminar)")
        print("3. Mostrar documentos pendientes")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Ingrese el código del documento: ")
            oficina.agregar_documento(codigo)
        elif opcion == "2":
            oficina.revisar_documento()
        elif opcion == "3":
            oficina.mostrar_pendientes()
        elif opcion == "4":
            print("Fin del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
