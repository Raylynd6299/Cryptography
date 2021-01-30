# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MenuInicial(object):
    def setupUi(self, MenuInicial):
        MenuInicial.setObjectName("MenuInicial")
        MenuInicial.resize(626, 240)
        self.centralwidget = QtWidgets.QWidget(MenuInicial)
        self.centralwidget.setObjectName("centralwidget")
        self.CDcheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.CDcheckBox.setGeometry(QtCore.QRect(120, 140, 211, 25))
        self.CDcheckBox.setObjectName("CDcheckBox")
        self.FVcheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.FVcheckBox.setGeometry(QtCore.QRect(340, 140, 171, 25))
        self.FVcheckBox.setObjectName("FVcheckBox")
        self.AMButton = QtWidgets.QPushButton(self.centralwidget)
        self.AMButton.setGeometry(QtCore.QRect(260, 180, 100, 27))
        self.AMButton.setObjectName("AMButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 110, 271, 19))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 30, 441, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MenuInicial.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MenuInicial)
        self.statusbar.setObjectName("statusbar")
        MenuInicial.setStatusBar(self.statusbar)

        self.retranslateUi(MenuInicial)
        QtCore.QMetaObject.connectSlotsByName(MenuInicial)

    def retranslateUi(self, MenuInicial):
        _translate = QtCore.QCoreApplication.translate
        MenuInicial.setWindowTitle(_translate("MenuInicial", "Practica C H"))
        self.CDcheckBox.setText(_translate("MenuInicial", "Cifrado/Descifrado"))
        self.FVcheckBox.setText(_translate("MenuInicial", "Firma/Verificación"))
        self.AMButton.setText(_translate("MenuInicial", "Abrir Menu"))
        self.label.setText(_translate("MenuInicial", "Seleccione la opcion que desea"))
        self.label_2.setText(_translate("MenuInicial", "Práctica: Criptografía Híbrida"))
