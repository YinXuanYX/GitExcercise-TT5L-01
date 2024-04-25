from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(720,580)
        self.setWindowTitle("Mobile Legends Item Guide")
        self.setWindowIcon(QIcon("mlbb.jpg"))

        parentLayout = QVBoxLayout()
        buttonLayout = QVBoxLayout()

        self.button1 = QPushButton("Physical Items")
        self.button2 = QPushButton("Magic Items")
        self.button3 = QPushButton("Defence Items")
        self.button4 = QPushButton("Roaming / Jungling boots")

        buttonLayout.addWidget(self.button1)
        buttonLayout.addSpacing(50)
        buttonLayout.addWidget(self.button2)
        buttonLayout.addSpacing(50)
        buttonLayout.addWidget(self.button3)
        buttonLayout.addSpacing(50)
        buttonLayout.addWidget(self.button4)

        

        parentLayout.addLayout(buttonLayout)


        centerWidget= QWidget()
        centerWidget.setLayout(parentLayout)
        self.setCentralWidget(centerWidget)

app = QApplication([])

window = Window()


window.show()
app.exec()