from PySide6.QtCore import Qt
from newpage_ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PySide6.QtSql import *
import sqlite3



class heroinfo(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("MLBB HERO GUIDE")
        self.assa.clicked.connect(self.assasinpg)
        self.tank.clicked.connect(self.tenkpg)
        self.mage.clicked.connect(self.magpg)
        self.fighter.clicked.connect(self.fightpg)
        self.mm.clicked.connect(self.marskmpg)
        self.sup.clicked.connect(self.suppg)
        self.Saber.clicked.connect(self.saberpg)
      
    def assasinpg(self):
        self.stackedWidget.setCurrentIndex(0)

    def tenkpg(self):
        self.stackedWidget.setCurrentIndex(1)

    def magpg(self):
        self.stackedWidget.setCurrentIndex(2)

    def fightpg(self):
        self.stackedWidget.setCurrentIndex(3)

    def marskmpg(self):
        self.stackedWidget.setCurrentIndex(4)

    def suppg(self):
        self.stackedWidget.setCurrentIndex(5)

    def saberpg(self):
        self.stackedWidget.setCurrentIndex(6)
        conn = sqlite3.connect('heroes.db')
        cursor = conn.cursor()

        cursor.execute('SELECT Passive_name,Passive FROM heroes WHERE Id = 1')
        result = cursor.fetchone()

        if result:
            passive_name = result[0]
            passive = result[1]  
            self.Passive_name_label.setText(f"{passive_name}")
            self.passivedesc.setText(f"{passive}")
        else:
            self.Passive_name_label.setText("No passive name found.")

        conn.close()
        

