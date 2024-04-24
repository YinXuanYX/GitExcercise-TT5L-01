import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget #application (settings initializing and event loop) main window (add widgets), Qlable allow to show text/img for our widgets
from PyQt6.QtGui import QIcon, QPixmap   #importing the library
from PyQt6.QtGui import QIcon  #import icons
from PyQt6.QtCore import Qt  #for widget location

app = QApplication([]) 
window = QMainWindow()
#setting up window
window.setMinimumSize(400, 500) #set minimum size and let user resize if needed

layout = QVBoxLayout

button1 = QPushButton("Click Me")
button2 = QPushButton("button2")

layout.addWidget(button1)
layout.addWidget(button2)

centerwidget= QWidget()
centerwidget.setLayout(layout)

window.setCentralWidget(centerwidget)


window.show()  #draw window
app.exec()  #start event loop, eg react to input such as click
