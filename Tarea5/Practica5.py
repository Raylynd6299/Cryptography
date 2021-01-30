#! /usr/bin/python

import MenuPrincipal,CyD,Procesos,FyV,CH
import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class MenuPrincipalC(QMainWindow,MenuPrincipal.Ui_MenuInicial):
    def __init__(self, parent=None):
        super(MenuPrincipalC,self).__init__(parent)
        self.ui = MenuPrincipal.Ui_MenuInicial()
        self.ui.setupUi(self)
        self.ui.AMButton.clicked.connect(self.AbrirMenu)
    
    def AbrirMenu(self):
        if (self.ui.FVcheckBox.isChecked() and not self.ui.CDcheckBox.isChecked()):
            print("Menu de Firma y verificacion")
            MenuFirmaVerificacion(self).show()
        if (not self.ui.FVcheckBox.isChecked() and self.ui.CDcheckBox.isChecked()):
            print("Menu de cifrado y descifrado")
            MenuCifradoDescifrado(self).show()
            
        if (self.ui.FVcheckBox.isChecked() and self.ui.CDcheckBox.isChecked()):
            print("Menu de cifrado hibrido")
            CifradoHibrido(self).show()
        
class MenuCifradoDescifrado(QMainWindow,CyD.Ui_CifradoDescifrado):
    def __init__(self,parent=None):
        super(MenuCifradoDescifrado,self).__init__(parent)
        self.ui = CyD.Ui_CifradoDescifrado()
        self.ui.setupUi(self)
        self.pathArchivo = ""
        self.pathLlave = "" 
        self.ui.pushButton.clicked.connect(self.Ejecutar)
        self.ui.ArchivoButton.clicked.connect(self.SelArchvi)
        self.ui.LlaveButton.clicked.connect(self.SelLlave)
    def SelArchvi(self):
        FileToDecript,_ = QtWidgets.QFileDialog.getOpenFileName(self,"Seleccione un archivo","./","All Files (*);;Text Files (*.txt)") 
        self.ui.archivopath.clear()
        self.ui.archivopath.insertPlainText(FileToDecript)
        self.pathArchivo = FileToDecript
    def SelLlave(self):
        FileToDecript,_ = QtWidgets.QFileDialog.getOpenFileName(self,"Seleccione un archivo","./","All Files (*);;Text Files (*.txt)") 
        self.ui.llavePath.clear()
        self.ui.llavePath.insertPlainText(FileToDecript)
        self.pathLlave = FileToDecript
    def Ejecutar(self):
        if (self.ui.CifradoradioButton.isChecked()):
            if(self.pathArchivo != "" and self.pathLlave != ""):
                flag = Procesos.Cifrar(self.pathArchivo,self.pathLlave)
                if  flag :
                    self.ui.Estatus.setText("Archivo Cifrado Correctamente")
                else:
                    self.ui.Estatus.setText("Error al cifrar, ingrese la llave Correcta")
            else:
                self.ui.Estatus.setText("Seleccione los archivos necesarios")
        elif (self.ui.DescifradoradioButton.isChecked()):
            if(self.pathArchivo != "" and self.pathLlave != ""):
                flag = Procesos.DesCifrar(self.pathArchivo,self.pathLlave)
                if  flag :
                    self.ui.Estatus.setText("Archivo Descifrado Correctamente")
                else:
                    self.ui.Estatus.setText("Error al descifrar, ingrese la llave Correcta")
            else:
                self.ui.Estatus.setText("Seleccione los archivos necesarios")
        else:
            self.ui.Estatus.setText("Seleccione una Opcion")


class MenuFirmaVerificacion(QMainWindow,FyV.Ui_FirmaVerifica):
    def __init__(self,parent=None):
        super(MenuFirmaVerificacion,self).__init__(parent)
        self.ui = FyV.Ui_FirmaVerifica()
        self.ui.setupUi(self)
        self.pathArchivo = ""
        self.pathLlave = "" 
        self.ui.Ejecutar.clicked.connect(self.EjecutarF)
        self.ui.ArchivoButton.clicked.connect(self.SelArchvi)
        self.ui.LlaveButton.clicked.connect(self.SelLlave)
    def SelArchvi(self):
        FileToDecript,_ = QtWidgets.QFileDialog.getOpenFileName(self,"Seleccione un archivo","./","All Files (*);;Text Files (*.txt)") 
        self.ui.pathArchivo.clear()
        self.ui.pathArchivo.insertPlainText(FileToDecript)
        self.pathArchivo = FileToDecript
    def SelLlave(self):
        FileToDecript,_ = QtWidgets.QFileDialog.getOpenFileName(self,"Seleccione un archivo","./","All Files (*);;Text Files (*.txt)") 
        self.ui.LlavePath.clear()
        self.ui.LlavePath.insertPlainText(FileToDecript)
        self.pathLlave = FileToDecript
    def EjecutarF(self):
        if (self.ui.FirmaradioButton.isChecked()):
            if(self.pathArchivo != "" and self.pathLlave != ""):
                flag = Procesos.FirmaDigital(self.pathArchivo,self.pathLlave)
                if  flag :
                    self.ui.EstatusN.setText("Archivo Firmado Correctamente")
                else:
                    self.ui.EstatusN.setText("Error al firmar el archivo, ingrese la llave Correcta")
            else:
                self.ui.EstatusN.setText("Seleccione los archivos necesarios")
                
        elif (self.ui.VerifiradioButton.isChecked()):
            if(self.pathArchivo != "" and self.pathLlave != ""):
                flag = Procesos.Verificacion(self.pathArchivo,self.pathLlave)
                if  flag :
                    self.ui.EstatusN.setText("Archivo Verificado")
                else:
                    self.ui.EstatusN.setText("Error al Verificar, ingrese la llave Correcta")
            else:
                self.ui.EstatusN.setText("Seleccione los archivos necesarios")
        else:
            self.ui.EstatusN.setText("Seleccione una Opcion")
 
 
class CifradoHibrido(QMainWindow,CH.Ui_CH):
    def __init__(self,parent=None):
        super(CifradoHibrido,self).__init__(parent)
        self.ui = CH.Ui_CH()
        self.ui.setupUi(self)
        self.pathArchivo = ""
        self.LlaveEmisorPath = ""
        self.LlaveReceptorPath = ""
        self.ui.EmisorRadioButton.clicked.connect(self.ClickEmisor)
        self.ui.ReceptorRadioButton.clicked.connect(self.ClickReceptor)
        self.ui.pushButton.clicked.connect(self.Ejecutar)
        self.ui.ArchivoButton.clicked.connect(self.SelArchvi)
        self.ui.LlaveEmisorButton.clicked.connect(self.SelLlaveEmisor)
        self.ui.LlaveReceptorButton.clicked.connect(self.SelLlaveReceptor)
    def SelArchvi(self):
        FileToDecript,_ = QtWidgets.QFileDialog.getOpenFileName(self,"Seleccione un archivo","./","All Files (*);;Text Files (*.txt)") 
        self.ui.archivoPath.clear()
        self.ui.archivoPath.insertPlainText(FileToDecript)
        self.pathArchivo = FileToDecript
    def SelLlaveEmisor(self):
        FileToDecript,_ = QtWidgets.QFileDialog.getOpenFileName(self,"Seleccione un archivo","./","All Files (*);;Text Files (*.txt)") 
        self.ui.LlaveEmisorPath.clear()
        self.ui.LlaveEmisorPath.insertPlainText(FileToDecript)
        self.LlaveEmisorPath = FileToDecript
    def SelLlaveReceptor(self):
        FileToDecript,_ = QtWidgets.QFileDialog.getOpenFileName(self,"Seleccione un archivo","./","All Files (*);;Text Files (*.txt)") 
        self.ui.LlaveReceptorPath.clear()
        self.ui.LlaveReceptorPath.insertPlainText(FileToDecript)
        self.LlaveReceptorPath = FileToDecript
    def ClickEmisor(self):
        self.ui.llaveReceptorLabel.setText("(Publica)")
        self.ui.llaveEmisorLabel.setText("(Privada)")
    def ClickReceptor(self):
        self.ui.llaveReceptorLabel.setText("(Privada)")
        self.ui.llaveEmisorLabel.setText("(Publica)")
    def Ejecutar(self):
        if (self.ui.EmisorRadioButton.isChecked()):
            if(self.pathArchivo != "" and self.LlaveEmisorPath != "" and self.LlaveReceptorPath != ""):
                flag,num = Procesos.Emisor(self.pathArchivo,self.LlaveEmisorPath,self.LlaveReceptorPath)
                if  flag :
                    self.ui.Estatus.setText("Archivo Procesado Correctamente")
                else:
                    if num == 1:
                        self.ui.Estatus.setText("Error en la llave del Receptor")
                    elif num == 2:
                        self.ui.Estatus.setText("Error en la llave del Emisor")
                    elif num == 3:
                        self.ui.Estatus.setText("Error al procesar el archivo")           
            else:
                self.ui.Estatus.setText("Seleccione los archivos necesarios")
                
        elif (self.ui.ReceptorRadioButton.isChecked()):
            if(self.pathArchivo != "" and self.LlaveEmisorPath != "" and self.LlaveReceptorPath != ""):
                flag,num = Procesos.Receptor(self.pathArchivo,self.LlaveEmisorPath,self.LlaveReceptorPath)
                if  flag :
                    self.ui.Estatus.setText("Archivo Correcto")
                else:
                    if num == 1:
                        self.ui.Estatus.setText("Error en la llave del Receptor")
                    elif num == 2:
                        self.ui.Estatus.setText("Error en la llave del Emisor")
                    elif num == 3:
                        self.ui.Estatus.setText("Error al verificar el archivo, Error de Autenticacion") 
            else:
                self.ui.Estatus.setText("Seleccione los archivos necesarios")
        else:
            self.ui.Estatus.setText("Seleccione una Opcion")
        
app = QtWidgets.QApplication(sys.argv)
gui = MenuPrincipalC()

if __name__ == '__main__':
    gui.show()
    sys.exit(app.exec_())