# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CH.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CH(object):
    def setupUi(self, CH):
        CH.setObjectName("CH")
        CH.resize(800, 472)
        self.centralwidget = QtWidgets.QWidget(CH)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 110, 151, 19))
        self.label_2.setObjectName("label_2")
        self.Estatus = QtWidgets.QLabel(self.centralwidget)
        self.Estatus.setGeometry(QtCore.QRect(180, 350, 561, 19))
        self.Estatus.setObjectName("Estatus")
        self.LlaveEmisorButton = QtWidgets.QPushButton(self.centralwidget)
        self.LlaveEmisorButton.setGeometry(QtCore.QRect(30, 210, 161, 27))
        self.LlaveEmisorButton.setObjectName("LlaveEmisorButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 180, 261, 19))
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 30, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.EmisorRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.EmisorRadioButton.setGeometry(QtCore.QRect(190, 80, 124, 25))
        self.EmisorRadioButton.setObjectName("EmisorRadioButton")
        self.LlaveEmisorPath = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.LlaveEmisorPath.setGeometry(QtCore.QRect(200, 210, 561, 31))
        self.LlaveEmisorPath.setObjectName("LlaveEmisorPath")
        self.ReceptorRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.ReceptorRadioButton.setGeometry(QtCore.QRect(470, 80, 161, 25))
        self.ReceptorRadioButton.setObjectName("ReceptorRadioButton")
        self.ArchivoButton = QtWidgets.QPushButton(self.centralwidget)
        self.ArchivoButton.setGeometry(QtCore.QRect(30, 140, 161, 27))
        self.ArchivoButton.setObjectName("ArchivoButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 350, 79, 19))
        self.label_3.setObjectName("label_3")
        self.archivoPath = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.archivoPath.setGeometry(QtCore.QRect(200, 140, 560, 31))
        self.archivoPath.setObjectName("archivoPath")
        self.LlaveReceptorPath = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.LlaveReceptorPath.setGeometry(QtCore.QRect(200, 280, 561, 31))
        self.LlaveReceptorPath.setObjectName("LlaveReceptorPath")
        self.LlaveReceptorButton = QtWidgets.QPushButton(self.centralwidget)
        self.LlaveReceptorButton.setGeometry(QtCore.QRect(30, 280, 161, 27))
        self.LlaveReceptorButton.setObjectName("LlaveReceptorButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(200, 250, 281, 19))
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 400, 100, 31))
        self.pushButton.setObjectName("pushButton")
        self.llaveEmisorLabel = QtWidgets.QLabel(self.centralwidget)
        self.llaveEmisorLabel.setGeometry(QtCore.QRect(470, 180, 171, 19))
        self.llaveEmisorLabel.setText("")
        self.llaveEmisorLabel.setObjectName("llaveEmisorLabel")
        self.llaveReceptorLabel = QtWidgets.QLabel(self.centralwidget)
        self.llaveReceptorLabel.setGeometry(QtCore.QRect(480, 250, 161, 20))
        self.llaveReceptorLabel.setText("")
        self.llaveReceptorLabel.setObjectName("llaveReceptorLabel")
        CH.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CH)
        self.statusbar.setObjectName("statusbar")
        CH.setStatusBar(self.statusbar)

        self.retranslateUi(CH)
        QtCore.QMetaObject.connectSlotsByName(CH)

    def retranslateUi(self, CH):
        _translate = QtCore.QCoreApplication.translate
        CH.setWindowTitle(_translate("CH", "CH"))
        self.label_2.setText(_translate("CH", "Direccion Archivo:"))
        self.Estatus.setText(_translate("CH", "Empecemos!!"))
        self.LlaveEmisorButton.setText(_translate("CH", "Seleccione llave "))
        self.label_5.setText(_translate("CH", "Direccion de la llave del Emisor:"))
        self.label.setText(_translate("CH", "Criptografía Hibrida"))
        self.EmisorRadioButton.setText(_translate("CH", "Emisor"))
        self.ReceptorRadioButton.setText(_translate("CH", "Receptor"))
        self.ArchivoButton.setText(_translate("CH", "Seleccione Archivo"))
        self.label_3.setText(_translate("CH", "Estatus:"))
        self.LlaveReceptorButton.setText(_translate("CH", "Seleccione llave "))
        self.label_6.setText(_translate("CH", "Direccion de la llave del Receptor:"))
        self.pushButton.setText(_translate("CH", "Ejecutar"))
