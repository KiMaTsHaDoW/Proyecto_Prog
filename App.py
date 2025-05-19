import re

from Clases.Alumnos import Alumno
from Clases.Libros import Libro
from Clases.ACL import ACL
from Clases.constantes import *
from Clases.menu import Menu
from Clases.Login import Login

alumnos:[Alumno] = []
libros:[Libro] = []
prestamos:[ACL] = []


class App:
    @staticmethod
    def agregar_alumno():
        print("\n--- Agregar Alumno ---")
        nombre:str = input("Nombre: ")
        apellidos:str = input("Apellidos: ")
        tramo:str = input("Tramo concedido: ")
        seccion:str = input("Sección: ")
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
        titulo:str = input("Título: ")
        autor:str = input("Autor: ")
        isbn:str = input("ISBN: ")
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
        fecha_prestamo: str = ''
        if not alumnos:
            print("No hay alumnos registrados. Primero añade alumnos.")
            return
        if not libros:
            print("No hay libros registrados. Primero añade libros.")
            return
        print("\n--- Prestar Libro ---")
        App.listar_alumnos()
        try:
            alumno_idx:int = int(input("Selecciona alumno (número): ")) - 1
            if alumno_idx not in range(len(alumnos)):
                print("Número inválido.")
                return
        except ValueError:
            print("Entrada inválida.")
            return

        App.listar_libros()
        try:
            libro_idx:int = int(input("Selecciona libro (número): ")) - 1
            if libro_idx not in range(len(libros)):
                print("Número inválido.")
                return
        except ValueError:
            print("Entrada inválida.")
            return

        if libros[libro_idx].numero_ejemplares == 0:
            print("No hay ejemplares disponibles para ese libro.")
            return
        while not App.validar_fecha(fecha_prestamo):
            fecha_prestamo = input("Fecha de préstamo (YYYY-MM-DD): ")
            if App.validar_fecha(fecha_prestamo):
                acl = ACL(fecha_prestamo)
                prestamos.append({
                    "alumno": alumnos[alumno_idx],
                    "libro": libros[libro_idx],
                    "ACL": acl
                })
                libros[libro_idx].numero_ejemplares -= 1
            else:
                print("Fecha invalida.")
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
        fecha_devolucion:str = input("Fecha de devolución (YYYY-MM-DD): ")
        prestamo["ACL"].fecha_devolucion = fecha_devolucion
        prestamo["ACL"].estado = 'devuelto'

    @staticmethod
    def guardar_alumnos():
        with open(ARCHIVO_ALUMNOS, 'w', encoding='utf-8') as f:
            for a in alumnos:
                line = f"{a.nombre},{a.apellidos},{a.tramo_concedido},{a.seccion}\n"
                f.write(line)

    @staticmethod
    def cargar_alumnos():
        try:
            with open(ARCHIVO_ALUMNOS, 'r', encoding='utf-8') as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) == 4:
                        a = Alumno(parts[0], parts[1], parts[2], parts[3])
                        alumnos.append(a)
        except FileNotFoundError:
            print(f'El archivo {ARCHIVO_ALUMNOS} no existe')

    @staticmethod
    def guardar_libros():
        with open(ARCHIVO_LIBROS, 'w', encoding='utf-8') as f:
            for l in libros:
                line = f"{l.titulo},{l.autor},{l.isbn},{l.numero_ejemplares}\n"
                f.write(line)

    @staticmethod
    def cargar_libros():
        try:
            with open(ARCHIVO_LIBROS, 'r', encoding='utf-8') as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) == 4:
                        l = Libro(parts[0], parts[1], parts[2], int(parts[3]))
                        libros.append(l)
        except FileNotFoundError:
            print(f'El archivo {ARCHIVO_LIBROS} no existe')

    @staticmethod
    def guardar_prestamos():
        with open(ARCHIVO_PRESTAMOS, 'w', encoding='utf-8') as f:
            for p in prestamos:
                acl = p["ACL"]
                line = (
                    f"{p['alumno'].nombre},{p['alumno'].apellidos},{p['alumno'].tramo_concedido},{p['alumno'].seccion},"
                    f"{p['libro'].titulo},{p['libro'].autor},{p['libro'].isbn},"
                    f"{acl.fecha_prestamo},{acl.fecha_devolucion if acl.fecha_devolucion else ''},{acl.estado}\n"
                )
                f.write(line)

    @staticmethod
    def cargar_prestamos():
        try:
            with open(ARCHIVO_PRESTAMOS, 'r', encoding='utf-8') as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) == 10:
                        alumno = Alumno(parts[0], parts[1], parts[2], parts[3])
                        libro = Libro(parts[4], parts[5], parts[6], 0)  # número de ejemplares no se guarda aquí, se puede ajustar
                        acl = ACL(parts[7], parts[8] if parts[8] else None, parts[9])
                        prestamos.append({
                            "alumno": alumno,
                            "libro": libro,
                            "ACL": acl
                        })
        except FileNotFoundError:
            print(f'El archivo {ARCHIVO_PRESTAMOS} no existe')

    @staticmethod
    def validar_fecha(fecha:str):
        patron = r'^(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$'
        return re.match(patron, fecha) is not None

    @staticmethod
    def main():
        sesion_iniciada: bool = False
        App.cargar_alumnos()
        App.cargar_libros()
        App.cargar_prestamos()
        while True:
            if sesion_iniciada is False:
                sesion_iniciada = Login.iniciar_sesion()
            if sesion_iniciada:
                Menu.mostrar_menu()
                Menu.opcion = input("Selecciona una opción: ")

                if Menu.opcion == OPCION_1:
                    App.agregar_alumno()
                elif Menu.opcion == OPCION_2:
                    App.listar_alumnos()
                elif Menu.opcion == OPCION_3:
                    App.agregar_libro()
                elif Menu.opcion == OPCION_4:
                    App.listar_libros()
                elif Menu.opcion == OPCION_5:
                    App.prestar_libro()
                elif Menu.opcion == OPCION_6:
                    App.devolver_libro()
                elif Menu.opcion == OPCION_7:
                    App.guardar_alumnos()
                    App.guardar_libros()
                    App.guardar_prestamos()
                    print("Datos guardados correctamente.")
                    break
                else:
                    print("Opción no válida, intenta de nuevo.\n")
            else:
                print('Credenciales Incorrectas\n')


if __name__ == '__main__':
    App.main()
