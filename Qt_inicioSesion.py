# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inicioSesion.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication
from Conexion import Conexion as BaseDeDatos
from App_Inicio import *

class Ui_inicioSesion(BaseDeDatos):
    def setupUi(self, inicioSesion):
        inicioSesion.setObjectName("inicioSesion")
        inicioSesion.resize(358, 271)

        self.gpb_usuario_password = QtWidgets.QGroupBox(inicioSesion)
        self.gpb_usuario_password.setGeometry(QtCore.QRect(10, 20, 331, 191))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)

        self.gpb_usuario_password.setFont(font)
        self.gpb_usuario_password.setObjectName("gpb_usuario_password")

        self.layoutWidget = QtWidgets.QWidget(self.gpb_usuario_password)
        self.layoutWidget.setGeometry(QtCore.QRect(24, 40, 81, 141))
        self.layoutWidget.setObjectName("layoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.lbl_usuario = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_usuario.setFont(font)
        self.lbl_usuario.setObjectName("lbl_usuario")
        self.verticalLayout.addWidget(self.lbl_usuario)

        self.lbl_password = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_password.setFont(font)
        self.lbl_password.setObjectName("lbl_password")
        self.verticalLayout.addWidget(self.lbl_password)

        self.lbl_nombre = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_nombre.setFont(font)
        self.lbl_nombre.setObjectName("lbl_nombre")
        self.verticalLayout.addWidget(self.lbl_nombre)

        self.lbl_role = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_role.setFont(font)
        self.lbl_role.setObjectName("lbl_role")
        self.verticalLayout.addWidget(self.lbl_role)

        self.layoutWidget1 = QtWidgets.QWidget(self.gpb_usuario_password)
        self.layoutWidget1.setGeometry(QtCore.QRect(100, 40, 211, 141))
        self.layoutWidget1.setObjectName("layoutWidget1")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.text_usuario = QtWidgets.QLineEdit(self.layoutWidget1)
        self.text_usuario.setFocus(True)
        self.text_usuario.setFont(font)
        self.text_usuario.setMaxLength(10)
        self.text_usuario.setCursorPosition(0)
        self.text_usuario.setObjectName("text_usuario")
        self.verticalLayout_2.addWidget(self.text_usuario)

        self.text_password = QtWidgets.QLineEdit(self.layoutWidget1)
        self.text_password.setFont(font)
        self.text_password.setMaxLength(10)
        self.text_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.text_password.setCursorPosition(0)
        self.text_password.setObjectName("text_password")
        self.verticalLayout_2.addWidget(self.text_password)

        self.text_nombre = QtWidgets.QLineEdit(self.layoutWidget1)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 17, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 17, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 17, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 17, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.text_nombre.setPalette(palette)

        self.text_nombre.setFont(font)
        self.text_nombre.setCursorPosition(0)
        self.text_nombre.setReadOnly(True)
        self.text_nombre.setObjectName("text_nombre")
        self.verticalLayout_2.addWidget(self.text_nombre)

        self.text_role = QtWidgets.QLineEdit(self.layoutWidget1)
        self.text_role.setPalette(palette)
        self.text_role.setFont(font)
        self.text_role.setCursorPosition(0)
        self.text_role.setReadOnly(True)
        self.text_role.setObjectName("text_role")
        self.verticalLayout_2.addWidget(self.text_role)

        self.btn_aceptar = QtWidgets.QPushButton(inicioSesion)
        self.btn_aceptar.setAutoDefault(False)
        self.btn_aceptar.setGeometry(QtCore.QRect(200, 220, 141, 41))
        self.btn_aceptar.setFont(font)
        self.btn_aceptar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.btn_cancelar = QtWidgets.QPushButton(inicioSesion)
        self.btn_cancelar.setAutoDefault(False)
        self.btn_cancelar.setGeometry(QtCore.QRect(20, 220, 141, 41))
        self.btn_cancelar.setFont(font)
        self.btn_cancelar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/cancelar.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancelar.setIcon(icon)
        self.btn_cancelar.setIconSize(QtCore.QSize(24, 24))
        self.btn_cancelar.setObjectName("btn_cancelar")

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/aceptar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_aceptar.setIcon(icon1)
        self.btn_aceptar.setIconSize(QtCore.QSize(24, 24))
        self.btn_aceptar.setObjectName("btn_aceptar")

        self.retranslateUi(inicioSesion)
        QtCore.QMetaObject.connectSlotsByName(inicioSesion)

        #EVENTOS
        self.btn_cancelar.clicked.connect(self.Cancelar)
        self.btn_aceptar.clicked.connect(self.validar)
        self.text_usuario.returnPressed.connect(self.focus)
        self.text_password.returnPressed.connect(self.focus)

    #Todos los metodos que usara login
    def Cancelar(self):
        sys.exit()

    #Ya que el pyqt5 no hace focus nosotros lo hacemos con funcione definidas del modulo
    def focus(self):
        if self.text_usuario.hasFocus() == True:
            self.text_password.setFocus()

        elif self.text_password.hasFocus() == True:
            self.btn_aceptar.setDefault(True)

    #cuando presionamos algunos de os botones nos informa que ha pasado
    def miniMensaje(self, titulo, mensaje, informativo):
        msg = QMessageBox()
        msg.setWindowTitle(titulo)
        msg.setIcon(QMessageBox.Information)
        msg.setText(mensaje)
        msg.setInformativeText(informativo)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def ver(self):
        print(BaseDeDatos.selecionarTabla(self,'Login','*'))

    #Si los datos que introduces en los entry
    def validar(self):
        mensaje = ''
        titulo = ''
        informativo = ''
        if self.btn_aceptar.text() == "Aceptar":
            #compara si se encuentra vacio los campos de texto
            if len(self.text_usuario.text()) == 0 or len(self.text_password.text()) == 0:
                mensaje = 'Usuario\n\nPassword'
                titulo = 'Usuario y Password incorrectos'
                informativo = 'No pueden quedar vacio'
                self.miniMensaje(titulo,mensaje,informativo)
            else:
                #si no se encuentran vacio verifica si se encuentra en la base de datos
                if self.buscar(self.text_usuario.text(), self.text_password.text()):
                    titulo = 'Iniciando Sesion'
                    mensaje = f'Bienvenido {self.text_usuario.text()}!!!'
                    informativo = 'Presiona ok y luego siguiente...'
                    self.miniMensaje(titulo,mensaje,informativo)
                    #si no se encuentra manda un mensaje de error
                else: 
                    titulo = 'Iniciando Sesion'
                    mensaje = 'Ha ocurrido un fallo'
                    informativo = 'No se ha encontrado'
                    self.miniMensaje(titulo,mensaje,informativo)
        else:
            print("Nueva Ventana!!")


    def rellenarCampos(self, usuarioNombre, usuarioRole):
        nombre = usuarioNombre
        role = usuarioRole
        self.text_nombre.setPlaceholderText(nombre)
        self.text_role.setPlaceholderText(role)
        self.btn_cancelar.setEnabled(False)
        self.text_usuario.setReadOnly(True)
        self.text_password.setReadOnly(True)
        self.btn_aceptar.setText("Siguiente")

    #se encarga de buscar en la base de datos        
    def buscar(self, palabra, password):
        for i in BaseDeDatos.selecionarTabla(self,'Login','*'):
            if i[1] == palabra and i[2] == password:
                self.rellenarCampos(i[3], i[4])
                return True
            else:
                return False

    #para agregarle los nombre que le he asignado en la applicacion gui
    def retranslateUi(self, inicioSesion):
        _translate = QtCore.QCoreApplication.translate
        inicioSesion.setWindowTitle(_translate("inicioSesion", "Inicio de Sesion"))
        self.gpb_usuario_password.setTitle(_translate("inicioSesion", "Usuario y Password"))
        self.lbl_usuario.setText(_translate("inicioSesion", "Usuario:"))
        self.lbl_password.setText(_translate("inicioSesion", "Password:"))
        self.lbl_nombre.setText(_translate("inicioSesion", "Nombre:"))
        self.lbl_role.setText(_translate("inicioSesion", "Role:"))
        self.text_usuario.setText(_translate("inicioSesion", "100470852"))
        self.text_password.setText(_translate("inicioSesion", "andy2000"))
        self.text_nombre.setPlaceholderText(_translate("inicioSesion", "UnKnow"))
        self.text_role.setPlaceholderText(_translate("inicioSesion", "UnKnow"))
        self.btn_cancelar.setText(_translate("inicioSesion", "Cancelar"))
        self.btn_aceptar.setText(_translate("inicioSesion", "Aceptar"))

        #crear un mensajito abajo donde pones el mouse
        self.btn_aceptar.setToolTip(_translate("inicioSesion","Presione para entrar."))
        self.btn_aceptar.setToolTip(_translate("inicioSesion","Presione para cancelar."))