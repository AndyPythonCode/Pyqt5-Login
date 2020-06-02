# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 442)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_ventanaPrincipal = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ventanaPrincipal.setGeometry(QtCore.QRect(250, 160, 257, 42))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        font.setItalic(False)
        self.lbl_ventanaPrincipal.setFont(font)
        self.lbl_ventanaPrincipal.setObjectName("lbl_ventanaPrincipal")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuOpcion = QtWidgets.QMenu(self.menubar)
        self.menuOpcion.setObjectName("menuOpcion")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuOpcion.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tienda A. J."))
        self.lbl_ventanaPrincipal.setText(_translate("MainWindow", "Ventana Principal"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuOpcion.setTitle(_translate("MainWindow", "Opcion"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))