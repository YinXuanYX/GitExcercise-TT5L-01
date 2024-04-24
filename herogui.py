import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton #application (settings initializing and event loop) main window (add widgets), Qlable allow to show text/img for our widgets
from PyQt6.QtGui import QIcon, QPixmap   #importing the library
from PyQt6.QtGui import QIcon  #import icons
from PyQt6.QtCore import Qt  #for widget location

app = QApplication([]) 

window = QMainWindow()
#setting up window
window.setMinimumSize(400, 500) #set minimum size and let user resize if needed
 #can do individually also window.setMinimumHeight #window.setFixedSize #dont allow user to resize
window.setWindowTitle("a new application")
window.setWindowIcon(QIcon('mlbb.jpg'))

#adding widgets
#label = QLabel("Text goes here", alignment=Qt.AlignmentFlag.AlignHCenter)
#font.setPointSize(17)
#font.setBold(True)
#label.setFont(font)

button = QPushButton("Click Me")
button.setFixedSize(50,50)
window.setCentralWidget(button)

#display a img
#label = QLabel()
#label.setPixmap(QPixmap("mlbb.jpg").scaled(250,250))
#window.setCentralWidget(label)
