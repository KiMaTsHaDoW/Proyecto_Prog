from alumno import Alumno
from libro import Libro
from prestamo import Prestamo
from clases.constantes import *

class Biblioteca:
    def __init__(self):
        self.alumnos_file = F_ALUMNOS
        self.libros_file = F_LIBROS
        self.prestamos_file = F_PRESTAMOS

        self.alumnos = []
        self.libros = []
        self.prestamos = []

    def cargar_alumnos(self):
        try:
            with open(self.alumnos_file, 'r') as f:
                for registro in f.readlines():
                    registro = registro.strip()
                    partes = registro.split(':')
                    self.alumnos.append(Alumno(partes[0], partes[1], partes[2]))
        except FileNotFoundError:
            print('No existe el archivo')

    def cargar_libros(self):
        datos = self.libros_file.cargar()
        return [Libro(**l) for l in datos]

    def cargar_prestamos(self):
        datos = self.prestamos_file.cargar()
        return [Prestamo(**p) for p in datos]

    def guardar_alumnos(self):
        datos = [a.__dict__ for a in self.alumnos]
        self.alumnos_file.guardar(datos)

    def guardar_libros(self):
        datos = [l.__dict__ for l in self.libros]
        self.libros_file.guardar(datos)

    def guardar_prestamos(self):
        datos = [p.__dict__ for p in self.prestamos]
        self.prestamos_file.guardar(datos)

    def mostrar_alumnos(self):
        print("Alumnos:")
        for a in self.alumnos:
            print(f"ID: {a.id}, Nombre: {a.nombre}, Curso: {a.curso}")

    def mostrar_libros(self):
        print("Libros:")
        for l in self.libros:
            print(f"ID: {l.id}, Título: {l.titulo}, Ejemplares disponibles: {l.ejemplares}")

    def prestar_libro(self):
        self.mostrar_alumnos()
        alumno_id = int(input("ID del alumno: "))
        alumno = next((a for a in self.alumnos if a.id == alumno_id), None)
        if not alumno:
            print("Alumno no encontrado.")
            return

        self.mostrar_libros()
        libro_id = int(input("ID del libro a prestar: "))
        libro = next((l for l in self.libros if l.id == libro_id), None)
        if not libro:
            print("Libro no encontrado.")
            return

        if libro.ejemplares > 0:
            nuevo_prestamo = Prestamo(alumno_id, libro_id)
            self.prestamos.append(nuevo_prestamo)
            libro.ejemplares -= 1
            print(f"Préstamo registrado: {alumno.nombre} tomó en préstamo '{libro.titulo}'.")
        else:
            print("No hay ejemplares disponibles para este libro.")

    def devolver_libro(self):
        alumno_id = int(input("ID del alumno: "))
        prestamos_activos = [p for p in self.prestamos if p.alumno_id == alumno_id and p.estado == 'prestado']
        if not prestamos_activos:
            print("El alumno no tiene préstamos activos.")
            return

        print("Préstamos activos del alumno:")
        for idx, p in enumerate(prestamos_activos, 1):
            libro = next((l for l in self.libros if l.id == p.libro_id), None)
            print(f"{idx}. {libro.titulo} (ID: {libro.id})")
        opcion = int(input("Número del préstamo a devolver: "))
        prestamo = prestamos_activos[opcion - 1]
        libro = next((l for l in self.libros if l.id == prestamo.libro_id), None)
        prestamo.estado = 'devuelto'
        libro.ejemplares += 1
        print(f"Libro '{libro.titulo}' devuelto correctamente.")
        self.guardar_prestamos()
        self.guardar_libros()