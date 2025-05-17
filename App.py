import os
import sys

from Clases.Alumnos import Alumno
from Clases.Libros import Libro
from Clases.ACL import ACL

# Listas globales
alumnos = []
libros = []
prestamos = []


class App:
    # Función para guardar alumnos en alumnos.txt
    @staticmethod
    def guardar_alumnos():
        with open('alumnos.txt', 'w', encoding='utf-8') as f:
            for a in alumnos:
                line = f"{a.nombre},{a.apellidos},{a.tramo_concedido},{a.seccion}\n"
                f.write(line)

    @staticmethod
    def agregar_alumno():
        print("\n--- Agregar Alumno ---")
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        tramo = input("Tramo concedido: ")
        seccion = input("Sección: ")
        alumno = Alumno(nombre, apellidos, tramo, seccion)
        alumnos.append(alumno)
        print("Alumno añadido correctamente.\n")

    @staticmethod
    def listar_alumnos():
        print("\n--- Lista de Alumnos ---")
        if not alumnos:
            print("No hay alumnos registrados.")
        else:
            for idx, alumno in enumerate(alumnos, 1):
                print(f"{idx}. {alumno}")

    @staticmethod
    def agregar_libro():
        print("\n--- Agregar Libro ---")
        titulo = input("Título: ")
        autor = input("Autor: ")
        isbn = input("ISBN: ")
        while True:
            try:
                ejemplares = int(input("Número de ejemplares: "))
                if ejemplares < 0:
                    print("Por favor, ingresa un número positivo.")
                    continue
                break
            except ValueError:
                print("Por favor, ingresa un número válido.")
        libro = Libro(titulo, autor, isbn, ejemplares)
        libros.append(libro)
        print("Libro añadido correctamente.\n")

    @staticmethod
    def listar_libros():
        print("\n--- Lista de Libros ---")
        if not libros:
            print("No hay libros registrados.")
        else:
            for idx, libro in enumerate(libros, 1):
                print(f"{idx}. {libro}")

    @staticmethod
    def prestar_libro():
        if not alumnos:
            print("No hay alumnos registrados. Primero añade alumnos.")
            return
        if not libros:
            print("No hay libros registrados. Primero añade libros.")
            return
        print("\n--- Prestar Libro ---")
        App.listar_alumnos()
        try:
            alumno_idx = int(input("Selecciona alumno (número): ")) - 1
            if alumno_idx not in range(len(alumnos)):
                print("Número inválido.")
                return
        except ValueError:
            print("Entrada inválida.")
            return

        App.listar_libros()
        try:
            libro_idx = int(input("Selecciona libro (número): ")) - 1
            if libro_idx not in range(len(libros)):
                print("Número inválido.")
                return
        except ValueError:
            print("Entrada inválida.")
            return

        if libros[libro_idx].numero_ejemplares == 0:
            print("No hay ejemplares disponibles para ese libro.")
            return

        fecha_prestamo = input("Fecha de préstamo (YYYY-MM-DD): ")
        acl = ACL(fecha_prestamo)
        prestamos.append({
            "alumno": alumnos[alumno_idx],
            "libro": libros[libro_idx],
            "ACL": acl
        })
        libros[libro_idx].numero_ejemplares -= 1
        print(f"Préstamo realizado: {alumnos[alumno_idx].nombre} tomó '{libros[libro_idx].titulo}'.\n")

    @staticmethod
    def devolver_libro():
        print("\n--- Devolver Libro ---")
        prestamos_activos = [p for p in prestamos if p["ACL"].estado == 'entregado']
        if not prestamos_activos:
            print("No hay préstamos activos para devolver.")
            return
        for idx, p in enumerate(prestamos_activos, 1):
            alumno = p["alumno"]
            libro = p["libro"]
            acl = p["ACL"]
            print(f"{idx}. {alumno} - Libro: '{libro.titulo}' - Préstamo: {acl.fecha_prestamo}")
        try:
            seleccion = int(input("Selecciona el préstamo a devolver (número): ")) - 1
            if seleccion not in range(len(prestamos_activos)):
                print("Número inválido.")
                return
        except ValueError:
            print("Entrada inválida.")
            return

        prestamo = prestamos_activos[seleccion]
        fecha_devolucion = input("Fecha de devolución (YYYY-MM-DD): ")
        prestamo["ACL"].fecha_devolucion = fecha_devolucion
        prestamo["ACL"].estado = 'devuelto'

    # Función para cargar alumnos desde alumnos.txt
    @staticmethod
    def cargar_alumnos():
        if os.path.exists('alumnos.txt'):
            with open('alumnos.txt', 'r', encoding='utf-8') as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) == 4:
                        a = Alumno(parts[0], parts[1], parts[2], parts[3])
                        alumnos.append(a)

    # Función para guardar libros en libros.txt
    @staticmethod
    def guardar_libros():
        with open('libros.txt', 'w', encoding='utf-8') as f:
            for l in libros:
                line = f"{l.titulo},{l.autor},{l.isbn},{l.numero_ejemplares}\n"
                f.write(line)

    # Función para cargar libros desde libros.txt
    @staticmethod
    def cargar_libros():
        if os.path.exists('libros.txt'):
            with open('libros.txt', 'r', encoding='utf-8') as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) == 4:
                        l = Libro(parts[0], parts[1], parts[2], int(parts[3]))
                        libros.append(l)

    # Función para guardar préstamos en prestamos.txt
    @staticmethod
    def guardar_prestamos():
        with open('prestamos.txt', 'w', encoding='utf-8') as f:
            for p in prestamos:
                acl = p["ACL"]
                line = (
                    f"{p['alumno'].nombre},{p['alumno'].apellidos},{p['alumno'].tramo_concedido},{p['alumno'].seccion},"
                    f"{p['libro'].titulo},{p['libro'].autor},{p['libro'].isbn},"
                    f"{acl.fecha_prestamo},{acl.fecha_devolucion if acl.fecha_devolucion else ''},{acl.estado}\n"
                )
                f.write(line)

    # Función para cargar préstamos desde prestamos.txt
    @staticmethod
    def cargar_prestamos():
        if os.path.exists('prestamos.txt'):
            with open('prestamos.txt', 'r', encoding='utf-8') as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) == 10:
                        # Reconstruir alumno, libro, ACL
                        alumno = Alumno(parts[0], parts[1], parts[2], parts[3])
                        libro = Libro(parts[4], parts[5], parts[6], 0)  # número de ejemplares no se guarda aquí, se puede ajustar
                        acl = ACL(parts[7], parts[8] if parts[8] else None, parts[9])
                        prestamos.append({
                            "alumno": alumno,
                            "libro": libro,
                            "ACL": acl
                        })
    @staticmethod
    def main():
        # Cargar datos desde archivos
        App.cargar_alumnos()
        App.cargar_libros()
        App.cargar_prestamos()

        while True:
            print("\n--- Menú de Gestión de Biblioteca ---")
            print("1. Agregar alumno")
            print("2. Listar alumnos")
            print("3. Agregar libro")
            print("4. Listar libros")
            print("5. Prestar libro")
            print("6. Devolver libro")
            print("7. Guardar datos y salir")
            choice = input("Selecciona una opción: ")

            if choice == '1':
                App.agregar_alumno()
            elif choice == '2':
                App.listar_alumnos()
            elif choice == '3':
                App.agregar_libro()
            elif choice == '4':
                App.listar_libros()
            elif choice == '5':
                App.prestar_libro()
            elif choice == '6':
                App.devolver_libro()
            elif choice == '7':
                # Guardar todos los datos antes de salir
                App.guardar_alumnos()
                App.guardar_libros()
                App.guardar_prestamos()
                print("Datos guardados. ¡Hasta luego!")
                sys.exit()
            else:
                print("Opción no válida, intenta de nuevo.")