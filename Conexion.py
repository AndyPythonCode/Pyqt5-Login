import sqlite3
from sqlite3 import Error

class Conexion:
    def __init__(self):
        #nombre de la base de datos
        self.nameFile = 'C:/Users/Andy Juan/Desktop/Python/pyqt5/Inicio de Sesion/DataBase/Tienda.db'
        #esto funciona para abrir nuestra base de datos
        self.conection = None
        #esto funciona para poner mandar comandos SQL a nuestra base de datos
        self.cursor = None

    #abrimos la base de datos
    def abrirConexion(self):
        try:
            #le decimos el archivo que necesita abrir
            self.conection = sqlite3.connect(self.nameFile)
            self.cursor = self.conection.cursor()
            print("Abriendo...")
        except Error as e:
            print(e)
    
    #cerramos la base de datos
    def cerrarConexion(self):
        try:
            #si nuestra base de datos no se encuentra abrierta cerramos
            if not self.conection == None:
                self.cursor.close()
                self.conection.close()
                print("Cerrando...")
            else:
                print("No esta abrierta la base de datos")
        except Error as e:
            print(e)

    #este en un decorador para no tener que mi codigo lleno de exceptiones
    def __exceptiones(f):
        def contenedor(self, *args):
            try:
                f(self, *args)
            except Error as e:
                print(f"No se puede {e}")
            finally:
                self.cerrarConexion()
        return contenedor

    #seleccionar todo a una tabla especifica
    def selecionarTabla(self, tabla, comando):
        self.abrirConexion()
        SQL = f"SELECT {comando} FROM {tabla}"
        self.cursor.execute(SQL)
        registros = self.cursor.fetchall()
        self.cerrarConexion()
        return registros
    
    #agregar datos en nuestra db, utilizando un decorador para agregar mas funcionalidad
    @__exceptiones
    def agregarTabla(self, tabla, comando, *argv):
        Usuarios = []
        Usuarios.append(argv)
        self.abrirConexion()
        SQL = f"INSERT INTO {tabla} {comando} VALUES (NULL,?,?)"
        self.cursor.executemany(SQL, Usuarios)
        self.conection.commit()

            