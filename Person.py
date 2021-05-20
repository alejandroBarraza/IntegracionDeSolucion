# from connection import *

# cursorOBj = sqlConn.cursor()
# cursorOBj.execute("Select * from persona")
# sqlConn.commit();


class Person:
    def __init__(self,nombre,apellido,telefono,id_unidad):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.id_unidad = id_unidad
    