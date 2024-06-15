from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
import sys 
from main_pagestup import mainpgentry

#Calls the application class which creates an application instance. The window will display the information of mainpgentry class from main_pagestup file.
app = QApplication(sys.argv)
window = mainpgentry()
#Runs the window and executes the application.
window.show()
app.exec()