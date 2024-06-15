from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
import sys 
from uisetup import heroinfo

#Calls the application class which creates an application instance. The window will display the information of heroinfo class from uisetup file.
app = QApplication(sys.argv)
window = heroinfo()
#Runs the window and executes the application.
window.show()
app.exec()