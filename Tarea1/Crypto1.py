import GUI,os,sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QDialog,QPushButton,QInputDialog,QListWidgetItem,QFileDialog
from PyQt5.QtCore import pyqtSignal, QTimer, Qt,QDir
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, \
    QApplication, QStyle, QListWidget, QStyleOptionButton, QListWidgetItem
from cryptography.fernet import Fernet    
    
ClavePrincipal = ""    

def GenerarClave():
    clave = Fernet.generate_key()
    with open("clave.key","wb") as ArchClave :
        ArchClave.write(clave)

def CargarClave():
    return open("clave.key","rb").read()

def Encriptar(mensaje):
    global ClavePrincipal

    mess = mensaje.encode()
    aes = Fernet(ClavePrincipal)
    
    return aes.encrypt(mess)

def DesEncriptar(mensjae):
    global ClavePrincipal
    
    mess = mensjae.encode()
    aes = Fernet(ClavePrincipal)
    
    return aes.decrypt(mess)
    
def EncriptarArchivo(archivo):
    global ClavePrincipal
    if ClavePrincipal == "":
        claveEsta = os.popen('ls').read()
        if "clave.key" in claveEsta : 
            ClavePrincipal =  CargarClave()
        else:
            GenerarClave()
            ClavePrincipal = CargarClave()
            
    aes = Fernet(ClavePrincipal)
    with open(archivo,"rb") as file :
        archivo_info = file.read()
        
    encrypted_data = aes.encrypt(archivo_info)
    
    nombre = archivo.strip().split("/")
    nombree = nombre[len(nombre)-1].split(".")
    nombree = nombree[0]+"_C."+nombree[1]
    
    with open(nombree,"wb") as file:
        file.write(encrypted_data)
def DesEncriptarArchivo(archivo):
    global ClavePrincipal
    if ClavePrincipal == "":
        claveEsta = os.popen('ls').read()
        if "clave.key" in claveEsta : 
            ClavePrincipal =  CargarClave()
        else:
            GenerarClave()
            ClavePrincipal = CargarClave()
    aes = Fernet(ClavePrincipal)
    with open(archivo,"rb") as file :
        archivo_info = file.read()
    desencrypted_data = aes.decrypt(archivo_info)
    
    nombre = archivo.strip().split("/")
    nombree = nombre[len(nombre)-1].split(".")
    nombree = nombree[0]+"_D."+nombree[1]
    
    with open(nombree,"wb") as file:
        file.write(desencrypted_data)

class Pra1_Crypto(QtWidgets.QMainWindow, GUI.Ui_MainWindow) :
    def __init__(self, parent=None):
        super(Pra1_Crypto, self).__init__(parent)
        self.ui = GUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.SeleccioneArchivoEncriptart)
        self.ui.pushButton_4.clicked.connect(self.SeleccioneArchivoDesEncriptart)
        self.ui.pushButton.clicked.connect(self.PorPalabra)
        
    def SeleccioneArchivoDesEncriptart(self):
        FileToDecript,_ = QFileDialog.getOpenFileName(self,"Seleccione un archivo",QDir.homePath(),"All Files (*);;Text Files (*.txt)") 
        if (FileToDecript != ""):
            DesEncriptarArchivo(FileToDecript)
            self.ui.label_5.setText("DesEncriptado")
    def SeleccioneArchivoEncriptart(self):
        FileToEncript,_ = QFileDialog.getOpenFileName(self,"Seleccione un archivo",QDir.homePath(),"All Files (*);;Text Files (*.txt)") 
        if (FileToEncript != ""):
            EncriptarArchivo(FileToEncript)
            self.ui.label_5.setText("Encriptado")
            
    def PorPalabra(self):
        global ClavePrincipal
        if ClavePrincipal == "":
            claveEsta = os.popen('ls').read()
            if "clave.key" in claveEsta : 
                ClavePrincipal =  CargarClave()
            else:
                GenerarClave()
                ClavePrincipal = CargarClave()
        if (self.ui.lineEdit.text() != "" and self.ui.lineEdit_2.text() == "") : 
            #Encriptar
            mesencrip = Encriptar(self.ui.lineEdit.text())
            self.ui.lineEdit_2.setText(str(mesencrip.decode()))
            
            self.ui.label_6.setText("Encriptado")
            
        elif  (self.ui.lineEdit.text() == "" and self.ui.lineEdit_2.text() != "") : 
            #Desencriptar
            mensajeDes = DesEncriptar(self.ui.lineEdit_2.text())
            self.ui.lineEdit_2.setText(str(mensajeDes.decode()))
            
            self.ui.label_6.setText("Desencriptado")
            
        else:
            self.ui.label_6.setText("Escriba en algun Campo")
        

app = QApplication(sys.argv)
gui = Pra1_Crypto()

if __name__ == '__main__':
    gui.show()
    sys.exit(app.exec_())
    