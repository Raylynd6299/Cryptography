# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_P3.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(686, 301)
        MainWindow.setWindowTitle("Practica 3 - Modos OP")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pathDir = QtWidgets.QLabel(self.centralwidget)
        self.pathDir.setGeometry(QtCore.QRect(190, 40, 481, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.pathDir.setFont(font)
        self.pathDir.setObjectName("pathDir")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 10, 191, 19))
        self.label_2.setObjectName("label_2")
        self.Sel_Img = QtWidgets.QPushButton(self.centralwidget)
        self.Sel_Img.setGeometry(QtCore.QRect(70, 40, 100, 27))
        self.Sel_Img.setObjectName("Sel_Img")
        self.Modo = QtWidgets.QComboBox(self.centralwidget)
        self.Modo.setGeometry(QtCore.QRect(70, 110, 171, 27))
        self.Modo.setObjectName("Modo")
        self.Modo.addItem("")
        self.Modo.addItem("")
        self.Modo.addItem("")
        self.Modo.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 80, 281, 19))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 80, 261, 19))
        self.label_4.setObjectName("label_4")
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(390, 110, 261, 27))
        self.Password.setObjectName("Password")
        self.Encry = QtWidgets.QRadioButton(self.centralwidget)
        self.Encry.setGeometry(QtCore.QRect(220, 160, 124, 25))
        self.Encry.setObjectName("Encry")
        self.Descry = QtWidgets.QRadioButton(self.centralwidget)
        self.Descry.setGeometry(QtCore.QRect(370, 160, 124, 25))
        self.Descry.setObjectName("Descry")
        self.ejecutar = QtWidgets.QPushButton(self.centralwidget)
        self.ejecutar.setGeometry(QtCore.QRect(290, 200, 100, 27))
        self.ejecutar.setObjectName("ejecutar")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(180, 230, 79, 19))
        self.label_5.setObjectName("label_5")
        self.Estado_L = QtWidgets.QLabel(self.centralwidget)
        self.Estado_L.setGeometry(QtCore.QRect(270, 230, 391, 19))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.Estado_L.setFont(font)
        self.Estado_L.setText("")
        self.Estado_L.setObjectName("Estado_L")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.pathDir.setText(_translate("MainWindow", "/"))
        self.label_2.setText(_translate("MainWindow", "Seleccione la imagen"))
        self.Sel_Img.setText(_translate("MainWindow", "Imagen"))
        self.Modo.setItemText(0, _translate("MainWindow", "Modo_ECB"))
        self.Modo.setItemText(1, _translate("MainWindow", "Modo_CBC"))
        self.Modo.setItemText(2, _translate("MainWindow", "Modo_CFB"))
        self.Modo.setItemText(3, _translate("MainWindow", "Modo_OFB"))
        self.label_3.setText(_translate("MainWindow", "Seleccione en Modo de Operacion"))
        self.label_4.setText(_translate("MainWindow", "Ingrese la contraseña (8 Digitos)"))
        self.Encry.setText(_translate("MainWindow", "Cifrar"))
        self.Descry.setText(_translate("MainWindow", "Descifrar"))
        self.ejecutar.setText(_translate("MainWindow", "Ejecutar"))
        self.label_5.setText(_translate("MainWindow", "Estado:"))
