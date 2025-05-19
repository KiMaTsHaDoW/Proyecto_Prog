class Menu:

    def __init__(self):
        self._opcion:int = 0

    @staticmethod
    def mostrar_menu():
        print("\n--- Menú de Gestión de Biblioteca ---")
        print("1. Agregar alumno")
        print("2. Listar alumnos")
        print("3. Agregar libro")
        print("4. Listar libros")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Guardar datos y salir")

    @property
    def opcion(self):
        return self._opcion

    @opcion.setter
    def opcion(self, opcion):
        self._opcion = opcion
