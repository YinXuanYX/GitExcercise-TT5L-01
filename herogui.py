import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon    #importing the library

class MyApp(QWidget):
    def __init__(self):
        super().__init
        self.setWindowTitle('hello app')  #app name
        self.setWindowIcon(QIcon('map.ico'))  #icon for the app
        self.resize(500, 350) #width , height

        layout = QVBoxLayout()
        self.setLayout(layout)


#widgets
        self.inputField = QLineEdit()
        self.button = QPushButton()
        self.output = QTextEdit()


        layout.addWidget(self.inputField)
        layout.addWidget(self.button)
        layout.addWidget(self.output)
        




app = QApplication(sys.argv)

window = MyApp()
window.show()   #display the app


sys.exit(app.exec_())