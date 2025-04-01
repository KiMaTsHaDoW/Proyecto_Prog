from mysql.connector import errorcode
from clases.constantes import *
import mysql.connector

try:
    cnx = mysql.connector.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        database=DATABASE
    )
    cursor = cnx.cursor()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print('No existe la base de datos')
    elif err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Error de conexion')
    else:
        print(err)
else:
    cnx.autocommit = True


alumnos = []

alumnos.append(cursor.execute('SELECT * FROM alumnos'))
print(alumnos)