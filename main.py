from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget, QDialog
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(1440,840)
        self.setWindowTitle("Mobile Legends Ultimate Guide")
        self.setWindowIcon(QIcon("Logo_Mobile_Legends-_Bang_Bang.jpg"))

        parentLayout = QVBoxLayout()
        buttonLayout = QHBoxLayout()
        

        self.setStyleSheet('''
            QMainWindow{
                background-color: QLinearGradient(x0: 0, y0: 0, x1: 1, y1: 1, stop: 0 #5DE3E2, stop: 1 #FC00FF)           
            }
            QLabel{
                color: #FFE53B;           
            }
            QPushButton{
                background-color: QLinearGradient(x0: 0, y0: 0, x1: 0, y1: 1, stop: 0 #4158D0, stop: 1 #FFCC70)        
            }
        ''')

        self.button1 = QPushButton("Heroes")
        self.button2 = QPushButton("Skins")
        self.button3 = QPushButton("Events and recharge")
        self.button4 = QPushButton("Rank system and line ups")

        buttonLayout.addWidget(self.button1)
        buttonLayout.addSpacing(50)
        buttonLayout.addWidget(self.button2)
        buttonLayout.addSpacing(50)
        buttonLayout.addWidget(self.button3)
        buttonLayout.addSpacing(50)
        buttonLayout.addWidget(self.button4)

        self.label = QLabel("Welcome to the best guides app for Mobile Legends Bang Bang", alignment=Qt.AlignmentFlag.AlignCenter)
        font = self.font()
        font.setPointSize(20)
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


