from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
import sys
from items import ItemsGuide

app = QApplication(sys.argv)

window = ItemsGuide()

window.show()
app.exec()