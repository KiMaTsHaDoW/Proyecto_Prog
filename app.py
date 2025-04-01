from clases.constantes import *

import mysql.connector


class App:
    def __init__(self):
        cnx = mysql.connector.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            database=DATABASE
        )

    def cargar_datos(self):
