from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
import sys
from items import MySideBar

app = QApplication(sys.argv)

window = MySideBar()

window.show()
app.exec()