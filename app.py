from mysql.connector import errorcode
from clases.constantes import *
import mysql.connector


class App:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(
                user=USER,
                password=PASSWORD,
                host=HOST,
                database=DATABASE
            )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                print('No existe la base de datos')
            elif err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('Error de conexion')
            else:
                print(err)
        else:
            self.cnx.autocommit = True


    def cargar_datos(self):
        alumnos:list = []
        libros:list = []
        alumnos_cursos_libros: list = []
        cursos: list = []
        materias: list = []

    def cargar_alumnos(self, alumnos):
        cursor = self.cnx.cursor()
