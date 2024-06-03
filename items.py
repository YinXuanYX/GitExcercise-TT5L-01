from PySide6.QtCore import Qt
from items_ui import Ui_MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PySide6.QtSql import *
import sqlite3
from functools import partial

class ItemsGuide(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("MLBB ITEMS GUIDE")
        self.setWindowIcon(QIcon("images/mlbb.jpg"))

        #set landing page to open first
        self.stackedWidget.setCurrentIndex(0)
        
        #hide the menu when app is first open
        self.icon_name_widget.setHidden(True)

        #buttons function
        self.Homeicon.clicked.connect(self.switch_to_LandingPage)
        self.Homename.clicked.connect(self.switch_to_LandingPage)

        self.physicalicon.clicked.connect(self.switch_to_PhysicalPage)
        self.physicalname.clicked.connect(self.switch_to_PhysicalPage)

        self.magicicon.clicked.connect(self.switch_to_MagicPage)
        self.magicname.clicked.connect(self.switch_to_MagicPage)

        self.defenseicon.clicked.connect(self.switch_to_DefensePage)
        self.defensename.clicked.connect(self.switch_to_DefensePage)

        self.bootsicon.clicked.connect(self.switch_to_MovementPage)
        self.bootsname.clicked.connect(self.switch_to_MovementPage)
         
        #physical items buttons 
        #use partial to avoid the extra argument problem so each button correctly passes item ID to the switch_to_ItemInfoPage function
        self.BOD_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 1))
        self.melefic_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 2))
        self.GreatDragon_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 3))
        self.SeaHalbert_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 4))
        self.RoseGold_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 5))
        self.Bloodlust_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 6))
        self.Hunter_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 7))
        self.Heptaseas_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 8))
        self.Windtalker_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 9))
        self.Endless_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 10))
        self.Berserker_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 11))
        self.Haas_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 12))
        self.WarX_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 13))
        self.WON_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 14))
        self.Golden_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 15))
        self.Corrosion_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 16))
        self.DHS_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 17))

        #Magic Items Buttons
        self.Flask_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 18))
        self.Genius_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 19))
        self.lightning_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 20))
        self.fleeting_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 21))
        self.BloodWings_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 22))
        self.COD_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 23))
        self.Starlium_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 24))
        self.Glowing_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 25))
        self.IceQueenWand_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 26))
        self.Concentrated_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 27))
        self.Holy_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 28))
        self.Divine_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 29))
        self.NOD_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 30))
        self.Feather_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 31))
        self.Winter_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 32))
        self.Enchanted_button.clicked.connect(partial(self.switch_to_ItemInfoPage, 33))
        


    def switch_to_LandingPage(self):
        self.stackedWidget.setCurrentIndex(0)
    def switch_to_PhysicalPage(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_MagicPage(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_DefensePage(self):
        self.stackedWidget.setCurrentIndex(3)
    
    def switch_to_MovementPage(self):
        self.stackedWidget.setCurrentIndex(4)


    #*args allows the thing to accept any number of additional arguments, solve the issue of receiving more arguments than expected from the clicked signal. Basically for the double digit.

    def switch_to_ItemInfoPage(self, item_id, *args):
        self.stackedWidget.setCurrentIndex(5)
        conn = sqlite3.connect('ITEAMREAL.db')
        cursor = conn.cursor()

        # Ensure the item_id is passed as a tuple
        cursor.execute('SELECT name, attributes, passive, type FROM items WHERE Id = ?', (item_id,))
        result = cursor.fetchone()

        if result:
            name, \
            attributes, \
            passive, \
            type = result
            
            self.ItemName.setText(f"{name}")
            self.ItemName_2.setText(f" {name}")
            self.ItemAttributes.setText(f" {attributes}")
            self.ItemType.setText(f" {type}")
            self.ItemPassive.setText(f" {passive}")
        else:
            self.ItemName.setText("No Item Found")

        conn.close()