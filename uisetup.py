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
        self.allhero.clicked.connect(self.allpg)
        self.assa.clicked.connect(self.assasinpg)
        self.tank.clicked.connect(self.tenkpg)
        self.mage.clicked.connect(self.magpg)
        self.fighter.clicked.connect(self.fightpg)
        self.mm.clicked.connect(self.marskmpg)
        self.sup.clicked.connect(self.suppg)
        self.Saber.clicked.connect(self.saberpg)
        self.Saber_2.clicked.connect(self.saberpg)
      
    def allpg(self):
        self.stackedWidget.setCurrentIndex(0)
        
    
    def assasinpg(self):
        self.stackedWidget.setCurrentIndex(1)

    def tenkpg(self):
        self.stackedWidget.setCurrentIndex(2)

    def magpg(self):
        self.stackedWidget.setCurrentIndex(3)

    def fightpg(self):
        self.stackedWidget.setCurrentIndex(4)

    def marskmpg(self):
        self.stackedWidget.setCurrentIndex(5)

    def suppg(self):
        self.stackedWidget.setCurrentIndex(6)

    def saberpg(self):
        self.stackedWidget.setCurrentIndex(7)
        conn = sqlite3.connect('heroes.db')
        cursor = conn.cursor()

        cursor.execute('SELECT Passive_name, Passive, Skill_1_name, Skill_1, Skill_2_name, Skill_2, Skill_3_name, Skill_3, Ultimate_name, Ultimate FROM heroes WHERE Id = 1')
        result = cursor.fetchone()

        if result:
            passive_name, passive, \
            skill_1_name, skill_1, \
            skill_2_name, skill_2, \
            skill_3_name, skill_3, \
            ultimate_name, ultimate = result
            
            self.Passive_name_label.setText(f"{passive_name}")
            self.passivedesc.setText(f" {passive}")
            self.skill1_name.setText(f" {skill_1_name}")
            self.skill1desc.setText(f" {skill_1}")
            self.skill2_name.setText(f" {skill_2_name}")
            self.skill2desc.setText(f" {skill_2}")
            self.Specialskillname.setText(f" {skill_3_name}")
            self.specialskilldesc.setText(f" {skill_3}")
            self.Ultimatename.setText(f" {ultimate_name}")
            self.ultimatedesc.setText(f" {ultimate}")
        else:
            self.Passive_name_label.setText("No passive name found.")

        conn.close()
        

