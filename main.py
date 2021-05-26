
from Person import *
import sqlite3
from sqlite3 import Error

# connection method to database 
def create_connection(db_file):
   
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

# return all data from database person 
def select_all_tasks(conn):

    cur = conn.cursor()
    cur.execute("SELECT * FROM persona")
    rows = cur.fetchall()
    for row in rows:
        print(row)


# insert a person to Persona Table.
def insert_person(conn):
    
    nombre = input("ingrese su nombre:")
    apellido = input("ingrese su apellido:")
    telefono = input("ingrese su telefono:")
    unidad = input("ingrese su departamento:")
    p1= Person(nombre,apellido, telefono,unidad)

    cur = conn.cursor()
    cur.execute("""INSERT INTO persona(nombre,apellido,telefono,id_unidad) 
                   VALUES (?,?,?,?)""",(p1.nombre,p1.apellido,p1.telefono,p1.id_unidad))
    conn.commit()
    print("Record inserted successfully into persona table ", cur.rowcount)

    
def menu():
    print("[1]. Ingresar una persona")
    print("[2]. Mostrar lista person")
    print("[0]. Salir del Programa")


#main method.
def main():
    database = r"D:\ale\Clases\descargas educa\pr integracion soluciones\Directorio\Directorio\directorio.db"
    # create a database connection
    # menu()
    # option = int(input("ingresar opcion: "))
    # while option != 0:
    #     if option == 1:
    #         # do something
    #         pass
    #     elif option == 2:
    #         # do something
    #         pass
    #     else:
    #         print("selecion numero disponible en el menu")
    #     print()
    #     menu()
    #     option = int(input("ingresar opcion: "))
    # print("gracias por usar este programa")
    conn = create_connection(database)
    with conn: 
        print("1. Query all tasks")
        insert_person(conn) 
        select_all_tasks(conn)

    print("connection closed")



if __name__ == '__main__':
    main()


   