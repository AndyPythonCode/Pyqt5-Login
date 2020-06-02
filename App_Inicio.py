from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from Qt_inicioSesion import *
from Qt_Tienda import *

class App_inicioSesion(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon("img/usuario.png"))
        self.ui = Ui_inicioSesion()
        self.ui.setupUi(self)

    def mostrarLogin(self):
        self.show()
        self.exec_()

class App_tienda(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon("img/usuario.png"))
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def mostrarTienda(self):
        self.show()

class Menu:
    def __init__(self):
        self.condicion = False

    def mostrar(self):
        if self.condicion:
            print(f"En mostrar:")
            self.tienda = App_tienda()
            self.tienda.mostrarTienda()      
        else:
            self.Login = App_inicioSesion()
            self.Login.mostrarLogin()  
    def mensaje(self):
        print(f"ventana Principal: {self.condicion}")    

if __name__ == "__main__":
    App = QApplication(sys.argv)   
    menu = Menu()
    menu.mostrar()
    sys.exit(App.exec_())  
