#!/usr/bin/python
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic
import pyfiglet

class Ui(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('figlet.ui', self)
        self.setFixedSize(510, 350)
        
    def pB_FigletClick(self):
        try:
            testo = self.lE_testo.text()
            result = pyfiglet.figlet_format(testo, font='colossal')
            self.pTE_Figlet.setPlainText(result)
        except:
            print("Testo non valido")   
    
    def lE_testoChange(self):
        self.pTE_Figlet.clear()



app = QApplication([])
window = Ui()
window.show()
app.exec()