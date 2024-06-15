from PySide6.QtCore import Qt
from main_page_ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PySide6.QtSql import *
from PySide6.QtGui import QPixmap, QIcon
import subprocess


class mainpgentry(QMainWindow,Ui_MainWindow):  #The class is the generated mainwindow and the compiling of the ui file data that will be runned on the window 
    def __init__(self): #intializes every code with the parameter self to integrate into the main window.
        super().__init__()
        self.setupUi(self) #Sets up the ui to function with the class
        self.setWindowTitle("MLBB ULTIMATE GUIDE") #Sets the name of the window
        self.Items_page.clicked.connect(self.run_Itemspage)
        self.Heroes_page.clicked.connect(self.run_heropage)
        self.Calculator_page.clicked.connect(self.run_Wrpage)

    #Uses the module subprocess to run a file outside of this file as a pop up screen.
    def run_heropage(self):
        subprocess.Popen(['python', 'heropage.py'])#runs the heroes guide page
    def run_Itemspage(self):
        subprocess.Popen(['python', 'main_items.py'])#runs the items guide page
    def run_Wrpage(self):
        subprocess.Popen(['python', 'WrCal.py'])#runs the Wr
