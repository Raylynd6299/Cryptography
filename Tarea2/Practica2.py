import affineCipher as AFC
import vigenere as VGC
import os,sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QDialog,QPushButton,QInputDialog,QListWidgetItem,QFileDialog
from PyQt5.QtCore import pyqtSignal, QTimer, Qt,QDir
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, \
    QApplication, QStyle, QListWidget, QStyleOptionButton, QListWidgetItem
import VigeAffineCipherUI

def cifrarVigenereProceso(clave,pathh,anillo):
    plainText = ""
    with open(pathh,"r+") as file:
        plainText = file.read()

    cipherText = VGC.vigenereCipher(plainText,clave,anillo)
    
    arch = pathh.split("/")[-1]
    arch = arch.split(".")
    arch = f"{arch[0]}.vig"
    with open(arch,"w+") as filee:
        filee.write(cipherText)

def decifrarVigenereProceso(clave,pathh,anillo):
    plainText = ""
    with open(pathh,"r+") as file:
        plainText = file.read()

    cipherText = VGC.vigenereDecipher(plainText,clave,anillo)
    
    arch = pathh.split("/")[-1]
    arch = arch.split(".")
    arch = f"{arch[0]}_vig.txt"
    with open(arch,"w+") as filee:
        filee.write(cipherText)
        
        
def cifrarAffineProceso(alfa,beta,anillo,pathh):
    plainText = ""
    with open(pathh,"r+") as file:
        plainText = file.read()

    cipherText = AFC.AffineCipher(alfa,beta,anillo,plainText)
    
    arch = pathh.split("/")[-1]
    arch = arch.split(".")
    arch = f"{arch[0]}.aff"
    with open(arch,"w+") as filee:
        filee.write(cipherText)

def decifrarAffineProceso(alfa,beta,anillo,pathh):
    plainText = ""
    with open(pathh,"r+") as file:
        plainText = file.read()

    cipherText = AFC.AffineDecipher(alfa,beta,anillo,plainText)
    
    arch = pathh.split("/")[-1]
    arch = arch.split(".")
    arch = f"{arch[0]}_aff.txt"
    with open(arch,"w+") as filee:
        filee.write(cipherText)
         

class Pra2(QtWidgets.QMainWindow, VigeAffineCipherUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Pra2, self).__init__(parent)
        self.ui = VigeAffineCipherUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.vigeCifraPush.clicked.connect(self.CifrarVigenere)
        self.ui.vigeDecifraPush.clicked.connect(self.DecifrarVigenerre)
        self.ui.AffineCifraPush.clicked.connect(self.CifrarAffine)
        self.ui.AffineDecifraPush.clicked.connect(self.DecifrarAffine)
        
    def CifrarVigenere(self):
        FileToDecript,_ = QFileDialog.getOpenFileName(self,"Seleccione un archivo","./","All Files (*);;Text Files (*.txt)") 
        if (FileToDecript != ""):
            if (self.ui.ClaveCifrar.text() != "" and self.ui.anillovige.text() != ""):
                if(int(self.ui.anillovige.text())<257):
                    cifrarVigenereProceso(self.ui.ClaveCifrar.text(),FileToDecript,int(self.ui.anillovige.text()))
                    self.ui.VigeLabel.setText("Archivo Cifrado!")
                else:
                    self.ui.VigeLabel.setText("Anillo invalido!")
            else:
                self.ui.VigeLabel.setText("Clave necesaria!")
        else:
            self.ui.VigeLabel.setText("Debe seleccionar un archivo")
    
    def DecifrarVigenerre(self):
        FileToDecript,_ = QFileDialog.getOpenFileName(self,"Seleccione un archivo","./","All Files (*);;Text Files (*.txt)") 
        if (FileToDecript != ""):
            if (self.ui.ClaveDecifrar.text() != "" and self.ui.anillovige.text() != ""):
                if(int(self.ui.anillovige.text())<257):
                    decifrarVigenereProceso(self.ui.ClaveDecifrar.text(),FileToDecript,int(self.ui.anillovige.text()))
                    self.ui.VigeLabel.setText("Archivo Decifrado!")
                else:
                    self.ui.VigeLabel.setText("Anillo invalido!")
            else:
                self.ui.VigeLabel.setText("Clave necesaria!")
        else:
            self.ui.VigeLabel.setText("Debe seleccionar un archivo")
            
    def CifrarAffine(self):
        FileToDecript,_ = QFileDialog.getOpenFileName(self,"Seleccione un archivo","./","All Files (*);;Text Files (*.txt)") 
        if (FileToDecript != ""):
            if (self.ui.AlfaText.text() != "" and self.ui.BetaText.text() != "" and self.ui.anilloAffine.text() != "" ):
                if(int(self.ui.anilloAffine.text()) < 257):
                    if(AFC.verifyKey(int(self.ui.AlfaText.text()),int(self.ui.anilloAffine.text()) ) == (True,1)):
                        cifrarAffineProceso(int(self.ui.AlfaText.text()),int(self.ui.BetaText.text()),int(self.ui.anilloAffine.text()),FileToDecript)
                        self.ui.AffineLabel.setText("Archivo Cifrado!")
                    else:
                        self.ui.AffineLabel.setText("Alfa Invalida o falta anillo!")
                else:
                    self.ui.AffineLabel.setText("anillo Invalido!")
            else:
                if (self.ui.anilloAffine.text() != "" ):
                    if(int(self.ui.anilloAffine.text()) < 257):
                        a,b = AFC.GenKey(int(self.ui.anilloAffine.text()))
                        self.ui.AffineLabel.setText("Archivo Cifrado!")
                        self.ui.AlfaText.setText(f"{a}")
                        self.ui.BetaText.setText(f"{b}")
                        self.ui.BetaText.setText(f"{b}")
                        cifrarAffineProceso(a,b,int(self.ui.anilloAffine.text()),FileToDecript)
                    else:
                        self.ui.AffineLabel.setText("anillo Invalido!")        
                else:
                    self.ui.AffineLabel.setText("Ingresa el anillo N")
        else:
            self.ui.AffineLabel.setText("Debe seleccionar un archivo")
    
    def DecifrarAffine(self):
        FileToDecript,_ = QFileDialog.getOpenFileName(self,"Seleccione un archivo","./","All Files (*);;Text Files (*.txt)") 
        if (FileToDecript != ""):
            if (self.ui.AlfaText.text() != "" and self.ui.BetaText.text() != "" and self.ui.anilloAffine.text() != "" and int(self.ui.anilloAffine.text()) < 257):
                if(AFC.verifyKey(int(self.ui.AlfaText.text()),int(self.ui.anilloAffine.text())  ) == (True,1)):
                    decifrarAffineProceso(int(self.ui.AlfaText.text()),int(self.ui.BetaText.text()),int(self.ui.anilloAffine.text()) ,FileToDecript)
                    self.ui.AffineLabel.setText("Archivo Descifrado!")
                else:
                    self.ui.AffineLabel.setText("Alfa Invalida!" + self.ui.AlfaText.text())
            else:
                self.ui.AffineLabel.setText("Es necesari alfa y beta!")
        else:
            self.ui.AffineLabel.setText("Debe seleccionar un archivo")
            
app = QApplication(sys.argv)
gui = Pra2()

if __name__ == '__main__':
    gui.show()
    sys.exit(app.exec_())
