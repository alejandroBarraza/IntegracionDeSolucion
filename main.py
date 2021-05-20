from Person import Person
from Person import *
import sys
import sqlite3
if __name__ == "__main__":

    nombre = input("ingrese su nombre:")
    apellido = input("ingrese su apellido:")
    telefono = input("ingrese su telefono:")
    unidad = input("ingrese su departamento:")
    p1= Person(nombre,apellido, telefono,unidad)

    try:
        sqlConn = sqlite3.connect('test1.db')
        cursor = sqlConn.cursor()
        print("Database created and Successfully Connected to SQLite")
        cursor.execute("INSERT INTO persona VALUES (?,?,?,?,?)",(p1.nombre,p1.apellido,p1.telefono,p1.id_unidad))
        cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if sqlConn:
            sqlConn.close()
            print("The SQLite connection is closed")
    

   