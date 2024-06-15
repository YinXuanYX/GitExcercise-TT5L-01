from PySide6.QtCore import Qt
from newpage_ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PySide6.QtSql import *
from PySide6.QtGui import QPixmap, QIcon
import sqlite3
from functools import partial



class heroinfo(QMainWindow,Ui_MainWindow): #The class is the generated mainwindow and the compiling of the ui file data that will be runned on the window 
    def __init__(self): #intializes every code with the parameter self to integrate into the main window.
        super().__init__()
        self.setupUi(self) #Sets up the ui to function with the class
        self.setWindowTitle("MLBB ULTIMATE GUIDE") #Sets the name of the window

        #set landing page to open first
        self.stackedWidget.setCurrentIndex(0)

        #Signals and slots for all the buttons to respond according to the functions defined below.
        #Addtional note, partial allows the developer to make the signals and slot more dynamic by allowing the number of Id in database to be selected when the saberpg function is called.
        #use partial to avoid the extra argument problem so each button correctly passes item ID to each buttons of heroes.
        self.allhero.clicked.connect(self.allpg)
        self.assa.clicked.connect(self.assasinpg)
        self.tank.clicked.connect(self.tenkpg)
        self.mage.clicked.connect(self.magpg)
        self.fighter.clicked.connect(self.fightpg)
        self.mm.clicked.connect(self.marskmpg)
        self.sup.clicked.connect(self.suppg)
        self.Saber.clicked.connect(partial(self.saberpg, 1))
        self.Saber_3.clicked.connect(partial(self.saberpg, 1))
        self.Karina.clicked.connect(partial(self.saberpg, 2))
        self.Karina_3.clicked.connect(partial(self.saberpg, 2))
        self.Alucard.clicked.connect(partial(self.saberpg, 3))
        self.Alucard_3.clicked.connect(partial(self.saberpg, 3))
        self.Fanny.clicked.connect(partial(self.saberpg, 4))
        self.Fanny_3.clicked.connect(partial(self.saberpg, 4))
        self.Hayabusa.clicked.connect(partial(self.saberpg, 5))
        self.Hayabusa_3.clicked.connect(partial(self.saberpg, 5))
        self.Natalia.clicked.connect(partial(self.saberpg, 6))
        self.Natalia_6.clicked.connect(partial(self.saberpg, 6))
        self.Lancelot.clicked.connect(partial(self.saberpg, 7))
        self.Lancelot_3.clicked.connect(partial(self.saberpg, 7))
        self.Helcurt.clicked.connect(partial(self.saberpg, 8))
        self.Helcurt_3.clicked.connect(partial(self.saberpg, 8))
        self.Gusion.clicked.connect(partial(self.saberpg, 9))
        self.Gusion_3.clicked.connect(partial(self.saberpg, 9))
        self.Hanzo.clicked.connect(partial(self.saberpg, 10))
        self.Hanzo_3.clicked.connect(partial(self.saberpg, 10))
        self.Ling.clicked.connect(partial(self.saberpg, 11))
        self.Ling_3.clicked.connect(partial(self.saberpg, 11))
        self.Zilong.clicked.connect(partial(self.saberpg, 12))
        self.Zilong_3.clicked.connect(partial(self.saberpg, 12))
        self.Tig.clicked.connect(partial(self.saberpg, 13))
        self.Tig_3.clicked.connect(partial(self.saberpg, 13))
        self.Kai.clicked.connect(partial(self.saberpg, 14))
        self.Kai_3.clicked.connect(partial(self.saberpg, 14))
        self.Bane.clicked.connect(partial(self.saberpg, 15))
        self.Bane_2.clicked.connect(partial(self.saberpg, 15))
        self.Rafa.clicked.connect(partial(self.saberpg, 16))
        self.Rafa_3.clicked.connect(partial(self.saberpg, 16))
        self.Eud.clicked.connect(partial(self.saberpg, 17))
        self.Eud_3.clicked.connect(partial(self.saberpg, 17))
        self.Layla.clicked.connect(partial(self.saberpg, 18))
        self.Layla_2.clicked.connect(partial(self.saberpg, 18))
        self.Moskov.clicked.connect(partial(self.saberpg, 19))
        self.Moskov_2.clicked.connect(partial(self.saberpg, 19))
        self.Roger.clicked.connect(partial(self.saberpg, 20))
        self.Roger_2.clicked.connect(partial(self.saberpg, 20))
        self.Karrie.clicked.connect(partial(self.saberpg, 21))
        self.Karrie_2.clicked.connect(partial(self.saberpg, 21))
        self.Bruno.clicked.connect(partial(self.saberpg, 22))
        self.Bruno_2.clicked.connect(partial(self.saberpg, 22))
        self.Franco.clicked.connect(partial(self.saberpg, 23))
        self.Franco_3.clicked.connect(partial(self.saberpg, 23))
        self.Atlas.clicked.connect(partial(self.saberpg, 24))
        self.Atlas_2.clicked.connect(partial(self.saberpg, 24))
        self.Estes.clicked.connect(partial(self.saberpg, 25))
        self.Estes_3.clicked.connect(partial(self.saberpg, 25))
        self.Angela.clicked.connect(partial(self.saberpg, 26))
        self.Angela_3.clicked.connect(partial(self.saberpg, 26))
        self.Floryn.clicked.connect(partial(self.saberpg, 27))
        self.Floryn_3.clicked.connect(partial(self.saberpg, 27))
        self.Valir.clicked.connect(partial(self.saberpg, 28))
        self.Valir_2.clicked.connect(partial(self.saberpg, 28))
        self.Vex.clicked.connect(partial(self.saberpg, 29))
        self.Vex_2.clicked.connect(partial(self.saberpg, 29))
        self.Nana.clicked.connect(partial(self.saberpg, 30))
        self.Nana_2.clicked.connect(partial(self.saberpg, 30))
      
    def allpg(self):
        self.stackedWidget.setCurrentIndex(0) #Change the page index number to reflect the page created for buttons for all heroes
        
    def assasinpg(self):
        self.stackedWidget.setCurrentIndex(1) #Change the page index number to reflect the page created for buttons for assasin heroes

    def tenkpg(self):
        self.stackedWidget.setCurrentIndex(2) #Change the page index number to reflect the page created for buttons for tank heroes heroes

    def magpg(self):
        self.stackedWidget.setCurrentIndex(4) #Change the page index number to reflect the page created for buttons for mage heroes

    def fightpg(self):
        self.stackedWidget.setCurrentIndex(3) #Change the page index number to reflect the page created for buttons for fighter heroes

    def marskmpg(self):
        self.stackedWidget.setCurrentIndex(5) #Change the page index number to reflect the page created for buttons for marskman heroes

    def suppg(self):
        self.stackedWidget.setCurrentIndex(6) #Change the page index number to reflect the page created for buttons for support heroes
    
    #*args allows the thing to accept any number of additional arguments, solve the issue of receiving more arguments than expected from the clicked signal. Basically for the double digit.
    def saberpg(self, item_id, *args):
        self.stackedWidget.setCurrentIndex(7) #Change the page index number to reflect the page created for the data of heroes to be displayed
        conn = sqlite3.connect('heroes.db') #creates a connection to the database file
        cursor = conn.cursor() #creates a curson object that will help select things from the database
        # Ensure the item_id is passed as a tuple
        cursor.execute('SELECT Passive_name, Passive, Skill_1_name, Skill_1, Skill_2_name, Skill_2, Skill_3_name, Skill_3, Ultimate_name, Ultimate, Heroimage, passive_image, skill1_image, skill2_image, ultimate_image FROM heroes WHERE Id = ?', (item_id,))
        #The code above will query the data from database.
        result = cursor.fetchone() #The draw the data from the database to be used as a variable

        if result:
            (passive_name, passive, 
             skill_1_name, skill_1, 
             skill_2_name, skill_2, 
             skill_3_name, skill_3, 
             ultimate_name, ultimate, 
             Heroimage, passive_image, 
             skill1_image, skill2_image, ultimate_image) = result #This turns the variable into multiple variables that contains the data according to the selection 
            
            #The list of code down here is all the labels that will undergo modification which is to reflect the text in the label to the one in the database
            #There is also modification of images which are done using the class Qpixmap which allows the developer to set images in the place of the label according to the prefix of the resource file.
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

        conn.close() #This will close the connection