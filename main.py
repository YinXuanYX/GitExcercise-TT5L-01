from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

app = QApplication([])

window = QMainWindow()
#Setting up window
window.setMinimumSize(720,1280)
window.setWindowTitle("Mobile Legends Ultimate Guide")
window.setWindowIcon(QIcon("Logo_Mobile_Legends-_Bang_Bang.jpg"))

#Adding widgets
parentLayout = QVBoxLayout()
buttonLayout = QHBoxLayout()

button1 = QPushButton("Heroes")
button2 = QPushButton("Skins")
button3 = QPushButton("Line ups")
button4 = QPushButton("Button 4")

buttonLayout.addWidget(button1)
buttonLayout.addSpacing(50)
buttonLayout.addWidget(button2)
buttonLayout.addSpacing(50)
buttonLayout.addWidget(button3)
buttonLayout.addSpacing(50)
buttonLayout.addWidget(button4)

label = QLabel("Newlabel", alignment=Qt.AlignmentFlag.AlignCenter)
font = window.font()
font.setPointSize(24)
font.setBold(True)
label.setFont(font)
parentLayout.addLayout(buttonLayout)

parentLayout.addWidget(label)

centerWidget= QWidget()
centerWidget.setLayout(parentLayout)

window.setCentralWidget(centerWidget)

window.show()
app.exec()


