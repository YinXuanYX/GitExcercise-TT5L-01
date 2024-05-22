from PySide6.QtCore import Qt
from items_ui import Ui_MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

class MySideBar(QMainWindow, Ui_MainWindow):
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
        self.BOD_button.clicked.connect(self.switch_to_ItemInfoPage)
        self.melefic_button.clicked.connect(self.switch_to_ItemInfoPage)
        self.GreatDragon_button.clicked.connect(self.switch_to_ItemInfoPage)
        self.SeaHalbert_button.clicked.connect(self.switch_to_ItemInfoPage)
        self.RoseGold_button.clicked.connect(self.switch_to_ItemInfoPage)
        self.Bloodlust_button.clicked.connect(self.switch_to_ItemInfoPage)
        self.Hunter_button.clicked.connect(self.switch_to_ItemInfoPage)
        self.Heptaseas_button.clicked.connect(self.switch_to_ItemInfoPage)
        self.Windtalker_button.clicked.connect(self.switch_to_ItemInfoPage)
        self.Endless_button.clicked.connect(self.switch_to_ItemInfoPage)
        self.Berserker_button.clicked.connect(self.switch_to_ItemInfoPage)
        self.Haas_button.clicked.connect(self.switch_to_ItemInfoPage)
        self.WarX_button.clicked.connect(self.switch_to_ItemInfoPage)
        self.WON_button.clicked.connect(self.switch_to_ItemInfoPage)
        self.Golden_button.clicked.connect(self.switch_to_ItemInfoPage)
        self.Corrosion_button.clicked.connect(self.switch_to_ItemInfoPage)
        self.DHS_button.clicked.connect(self.switch_to_ItemInfoPage)
        


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

    def switch_to_ItemInfoPage(self):
        self.stackedWidget.setCurrentIndex(5)