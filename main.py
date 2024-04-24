from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(720,1280)
        self.setWindowTitle("Mobile Legends Ultimate Guide")
        self.setWindowIcon(QIcon("Logo_Mobile_Legends-_Bang_Bang.jpg"))

        parentLayout = QVBoxLayout()
        buttonLayout = QHBoxLayout()

        self.button1 = QPushButton("Heroes")
        self.button2 = QPushButton("Skins")
        self.button3 = QPushButton("Line ups")
        self.button4 = QPushButton("Button 4")

        buttonLayout.addWidget(self.button1)
        buttonLayout.addSpacing(50)
        buttonLayout.addWidget(self.button2)
        buttonLayout.addSpacing(50)
        buttonLayout.addWidget(self.button3)
        buttonLayout.addSpacing(50)
        buttonLayout.addWidget(self.button4)

        self.label = QLabel("Newlabel", alignment=Qt.AlignmentFlag.AlignCenter)
        font = self.font()
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        parentLayout.addLayout(buttonLayout)

        parentLayout.addWidget(self.label)

        centerWidget= QWidget()
        centerWidget.setLayout(parentLayout)
        self.setCentralWidget(centerWidget)

app = QApplication([])

window = Window()


window.show()
app.exec()


