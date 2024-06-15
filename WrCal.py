from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
import sys

from sidebar import MySideBar# import code from sidebar.py

app = QApplication(sys.argv)

window = MySideBar()


window.show()
app.exec()