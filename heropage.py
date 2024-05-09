from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
import sys 
from uisetup import heroinfo

app = QApplication(sys.argv)

window = heroinfo()

window.show()
app.exec()