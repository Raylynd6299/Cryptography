from PyQt5 import QtCore, QtGui, QtWidgets
from Crypto.Cipher import DES
import GUI_P3
import Procesos as Pro
import sys

    
class Pra3(QtWidgets.QMainWindow,GUI_P3.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Pra3,self).__init__(parent)
        self.ui = GUI_P3.Ui_MainWindow()
        self.pathh = ""
        self.ui.setupUi(self)
        self.ui.Sel_Img.clicked.connect(self.Sel_PATH)
        self.ui.ejecutar.clicked.connect(self.Ejecut)
    def Sel_PATH(self):
        FileToDecript,_ = QtWidgets.QFileDialog.getOpenFileName(self,"Seleccione una image","./","All Files (*);;Text Files (*.bmp)") 
        self.ui.pathDir.setText(FileToDecript)
        self.pathh = FileToDecript
    def Ejecut(self):
        if self.pathh == "":
            self.ui.Estado_L.setText("Seleccione una Imagen")
            return
        selMOD = self.ui.Modo.currentText()
        if self.ui.Password.text() == "":
            self.ui.Estado_L.setText("Ingrese una contraseña")
            return
        Password_text = self.ui.Password.text()
        if len(Password_text) != 8:
            self.ui.Estado_L.setText("La contraseña debe ter 8 digitos")
            return
        if selMOD == "Modo_ECB":
            selMOD = DES.MODE_ECB
        elif selMOD == "Modo_CBC":
            selMOD = DES.MODE_CBC
        elif selMOD == "Modo_CFB":
            selMOD = DES.MODE_CFB
        elif selMOD == "Modo_OFB":
            selMOD = DES.MODE_OFB
        if self.ui.Encry.isChecked():
            flag = Pro.Cifrar(Password_text,selMOD,self.pathh)
            if flag :
                self.ui.Estado_L.setText("Cifrado")
            else :
                self.ui.Estado_L.setText("Error al Cifrar")
        elif self.ui.Descry.isChecked():
            flag = Pro.DesCifrar(Password_text,selMOD,self.pathh)
            if flag :
                self.ui.Estado_L.setText("DesCifrado")
            else :
                self.ui.Estado_L.setText("Error al DesCifrar")
        else:
            self.ui.Estado_L.setText("Seleccione una accion")
            return

app = QtWidgets.QApplication(sys.argv)
gui = Pra3()

if __name__ == '__main__':
    gui.show()
    sys.exit(app.exec_())