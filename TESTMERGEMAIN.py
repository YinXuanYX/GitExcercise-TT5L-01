from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
import sys
from TESTMERGE import CentralMainWindow

app = QApplication(sys.argv)

window = CentralMainWindow()

window.show()
app.exec()