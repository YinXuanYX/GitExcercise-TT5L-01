from PySide6.QtCore import Qt
from newpage_ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PySide6.QtSql import *
from PySide6.QtGui import QPixmap, QIcon
import sqlite3
from functools import partial



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
        self.Saber.clicked.connect(partial(self.saberpg, 1))
        self.saber.clicked.connect(partial(self.saberpg, 1))
        self.Karina.clicked.connect(partial(self.saberpg, 2))
        self.Alucard.clicked.connect(partial(self.saberpg, 3))
        self.Fanny.clicked.connect(partial(self.saberpg, 4))
        self.Hayabusa.clicked.connect(partial(self.saberpg, 5))
        self.Natalia.clicked.connect(partial(self.saberpg, 6))
      
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

    def saberpg(self, item_id, *args):
        self.stackedWidget.setCurrentIndex(7)
        conn = sqlite3.connect('heroes.db')
        cursor = conn.cursor()
        cursor.execute('SELECT Passive_name, Passive, Skill_1_name, Skill_1, Skill_2_name, Skill_2, Skill_3_name, Skill_3, Ultimate_name, Ultimate, Heroimage, passive_image, skill1_image, skill2_image, ultimate_image FROM heroes WHERE Id = ?', (item_id,))
        result = cursor.fetchone()

        if result:
            (passive_name, passive, 
             skill_1_name, skill_1, 
             skill_2_name, skill_2, 
             skill_3_name, skill_3, 
             ultimate_name, ultimate, 
             Heroimage, passive_image, 
             skill1_image, skill2_image, ultimate_image) = result
            
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
            self.heropic.setPixmap(QPixmap(f":/{Heroimage}"))
            self.passivepic.setPixmap(QPixmap(f":/{passive_image}"))
            self.skill1pic.setPixmap(QPixmap(f":/{skill1_image}"))
            self.skill2pic.setPixmap(QPixmap(f":/{skill2_image}"))
            self.ultipic.setPixmap(QPixmap(f":/{ultimate_image}"))
        else:
            self.Passive_name_label.setText("No passive name found.")

        conn.close()
        
 