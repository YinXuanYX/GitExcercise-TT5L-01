from PySide6.QtCore import Qt
from newpage_ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget



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
