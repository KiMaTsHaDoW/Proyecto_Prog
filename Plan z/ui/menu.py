class Menu:
    def __init__(self):
        self._opcion:int = 0

    @staticmethod
    def mostrar_menu():
        while True:
            print("\n--- Menú Biblioteca ---")
            print("1. Mostrar alumnos")
            print("2. Mostrar libros")
            print("3. Prestar libro")
            print("4. Devolver libro")
            print("5. Salir")

    @property
    def opcion(self):
        return self._opcion

    @opcion.setter
    def opcion(self, opcion):
        self._opcion = opcion


        # if opcion == '1':
        #     self.mostrar_alumnos()
        # elif opcion == '2':
        #     self.mostrar_libros()
        # elif opcion == '3':
        #     self.prestar_libro()
        #     self.guardar_prestamos()
        #     self.guardar_libros()
        # elif opcion == '4':
        #     self.devolver_libro()
        #     self.guardar_prestamos()
        #     self.guardar_libros()
        # elif opcion == '5':
        #     print("¡Hasta luego!")
        #     break
        # else:
        #     print("Opción no válida. Intente de nuevo.")
