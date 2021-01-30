# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CyD.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CifradoDescifrado(object):
    def setupUi(self, CifradoDescifrado):
        CifradoDescifrado.setObjectName("CifradoDescifrado")
        CifradoDescifrado.resize(775, 375)
        self.centralwidget = QtWidgets.QWidget(CifradoDescifrado)
        self.centralwidget.setObjectName("centralwidget")
        self.CifradoradioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.CifradoradioButton.setGeometry(QtCore.QRect(160, 70, 124, 25))
        self.CifradoradioButton.setObjectName("CifradoradioButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 20, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.DescifradoradioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.DescifradoradioButton.setGeometry(QtCore.QRect(440, 70, 161, 25))
        self.DescifradoradioButton.setObjectName("DescifradoradioButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 100, 151, 19))
        self.label_2.setObjectName("label_2")
        self.archivopath = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.archivopath.setGeometry(QtCore.QRect(250, 130, 491, 31))
        self.archivopath.setObjectName("archivopath")
        self.ArchivoButton = QtWidgets.QPushButton(self.centralwidget)
        self.ArchivoButton.setGeometry(QtCore.QRect(80, 130, 161, 27))
        self.ArchivoButton.setObjectName("ArchivoButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 260, 79, 19))
        self.label_3.setObjectName("label_3")
        self.Estatus = QtWidgets.QLabel(self.centralwidget)
        self.Estatus.setGeometry(QtCore.QRect(170, 260, 561, 19))
        self.Estatus.setObjectName("Estatus")
        self.llavePath = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.llavePath.setGeometry(QtCore.QRect(250, 200, 491, 31))
        self.llavePath.setObjectName("llavePath")
        self.LlaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.LlaveButton.setGeometry(QtCore.QRect(80, 200, 161, 27))
        self.LlaveButton.setObjectName("LlaveButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 170, 191, 19))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 300, 161, 41))
        self.pushButton.setObjectName("pushButton")
        CifradoDescifrado.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CifradoDescifrado)
        self.statusbar.setObjectName("statusbar")
        CifradoDescifrado.setStatusBar(self.statusbar)

        self.retranslateUi(CifradoDescifrado)
        QtCore.QMetaObject.connectSlotsByName(CifradoDescifrado)

    def retranslateUi(self, CifradoDescifrado):
        _translate = QtCore.QCoreApplication.translate
        CifradoDescifrado.setWindowTitle(_translate("CifradoDescifrado", "CifradoDescifrado"))
        self.CifradoradioButton.setText(_translate("CifradoDescifrado", "Cifrado (A)"))
        self.label.setText(_translate("CifradoDescifrado", "Cifrado / Descifrado"))
        self.DescifradoradioButton.setText(_translate("CifradoDescifrado", "Descifrado (B)"))
        self.label_2.setText(_translate("CifradoDescifrado", "Direccion Archivo:"))
        self.ArchivoButton.setText(_translate("CifradoDescifrado", "Seleccione Archivo"))
        self.label_3.setText(_translate("CifradoDescifrado", "Estatus:"))
        self.Estatus.setText(_translate("CifradoDescifrado", "Empecemos!!"))
        self.LlaveButton.setText(_translate("CifradoDescifrado", "Seleccione llave"))
        self.label_5.setText(_translate("CifradoDescifrado", "Direccion de la llave:"))
        self.pushButton.setText(_translate("CifradoDescifrado", "Ejecutar"))
