# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FyV.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FirmaVerifica(object):
    def setupUi(self, FirmaVerifica):
        FirmaVerifica.setObjectName("FirmaVerifica")
        FirmaVerifica.resize(791, 392)
        self.centralwidget = QtWidgets.QWidget(FirmaVerifica)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 30, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pathArchivo = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.pathArchivo.setGeometry(QtCore.QRect(240, 140, 521, 31))
        self.pathArchivo.setObjectName("pathArchivo")
        self.LlaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.LlaveButton.setGeometry(QtCore.QRect(70, 210, 161, 27))
        self.LlaveButton.setObjectName("LlaveButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 270, 79, 19))
        self.label_3.setObjectName("label_3")
        self.FirmaradioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.FirmaradioButton.setGeometry(QtCore.QRect(190, 80, 124, 25))
        self.FirmaradioButton.setObjectName("FirmaradioButton")
        self.LlavePath = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.LlavePath.setGeometry(QtCore.QRect(240, 210, 521, 31))
        self.LlavePath.setObjectName("LlavePath")
        self.VerifiradioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.VerifiradioButton.setGeometry(QtCore.QRect(470, 80, 161, 25))
        self.VerifiradioButton.setObjectName("VerifiradioButton")
        self.ArchivoButton = QtWidgets.QPushButton(self.centralwidget)
        self.ArchivoButton.setGeometry(QtCore.QRect(70, 140, 161, 27))
        self.ArchivoButton.setObjectName("ArchivoButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 110, 151, 19))
        self.label_2.setObjectName("label_2")
        self.EstatusN = QtWidgets.QLabel(self.centralwidget)
        self.EstatusN.setGeometry(QtCore.QRect(200, 270, 561, 19))
        self.EstatusN.setObjectName("EstatusN")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(280, 180, 191, 19))
        self.label_5.setObjectName("label_5")
        self.Ejecutar = QtWidgets.QPushButton(self.centralwidget)
        self.Ejecutar.setGeometry(QtCore.QRect(320, 310, 111, 41))
        self.Ejecutar.setObjectName("Ejecutar")
        FirmaVerifica.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FirmaVerifica)
        self.statusbar.setObjectName("statusbar")
        FirmaVerifica.setStatusBar(self.statusbar)

        self.retranslateUi(FirmaVerifica)
        QtCore.QMetaObject.connectSlotsByName(FirmaVerifica)

    def retranslateUi(self, FirmaVerifica):
        _translate = QtCore.QCoreApplication.translate
        FirmaVerifica.setWindowTitle(_translate("FirmaVerifica", "Firma / Verificacion"))
        self.label.setText(_translate("FirmaVerifica", "Firma / Verificación"))
        self.LlaveButton.setText(_translate("FirmaVerifica", "Seleccione llave"))
        self.label_3.setText(_translate("FirmaVerifica", "Estatus:"))
        self.FirmaradioButton.setText(_translate("FirmaVerifica", "Firma (A)"))
        self.VerifiradioButton.setText(_translate("FirmaVerifica", "Verificación (B)"))
        self.ArchivoButton.setText(_translate("FirmaVerifica", "Seleccione Archivo"))
        self.label_2.setText(_translate("FirmaVerifica", "Direccion Archivo:"))
        self.EstatusN.setText(_translate("FirmaVerifica", "Empecemos!!"))
        self.label_5.setText(_translate("FirmaVerifica", "Direccion de la llave:"))
        self.Ejecutar.setText(_translate("FirmaVerifica", "Ejecutar"))
