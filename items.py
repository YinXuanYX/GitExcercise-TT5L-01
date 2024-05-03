from PySide6.QtCore import Qt
from ui_items import Ui_MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("MLBB ITEMS GUIDE")
        self.setWindowIcon(QIcon("images/mlbb.jpg"))
        

        self.icon_name_widget.setHidden(True)

        self.physicalicon.clicked.connect(self.switch_to_PhysicalPage)
        self.physicalname.clicked.connect(self.switch_to_PhysicalPage)

        self.magicicon.clicked.connect(self.switch_to_MagicPage)
        self.magicname.clicked.connect(self.switch_to_MagicPage)

        self.defenseicon.clicked.connect(self.switch_to_DefensePage)
        self.defensename.clicked.connect(self.switch_to_DefensePage)

        self.bootsicon.clicked.connect(self.switch_to_MovementPage)
        self.bootsname.clicked.connect(self.switch_to_MovementPage)



    def switch_to_PhysicalPage(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_MagicPage(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_DefensePage(self):
        self.stackedWidget.setCurrentIndex(2)
    
    def switch_to_MovementPage(self):
        self.stackedWidget.setCurrentIndex(3)