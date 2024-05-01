import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow,QStackedWidget,QVBoxLayout,QHBoxLayout,QLineEdit,QLabel, QComboBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(1440,840)
        self.setWindowTitle("Mobile Legends Ultimate Guide")
        self.setWindowIcon(QIcon("Logo_Mobile_Legends-_Bang_Bang.jpg"))

        self.comboBox = QComboBox()
        self.comboBox.addItem(QIcon("Assassin_Icon (1).webp"),'Assassin')
        self.comboBox.addItem(QIcon("Tank_Icon.webp"),'Tank')
        self.comboBox.addItem(QIcon("Fighter_Icon.webp"),'Fighter')
        self.comboBox.addItem(QIcon("Marksman_Icon.webp"),'Marksman')
        self.comboBox.addItem(QIcon("Mage_Icon.webp"),'Mage')
        self.comboBox.addItem(QIcon("Support_Icon.webp"),'Support')

        parentLayout = QHBoxLayout()
        buttonLayout = QHBoxLayout()


        self.label = QLabel("Heroes", alignment=Qt.AlignmentFlag.AlignTop)
        font = self.font()
        font.setPointSize(45)
        font.setBold(True)
        self.label.setFont(font)
        parentLayout.addLayout(buttonLayout)
        parentLayout.addWidget(self.label)
        parentLayout.addWidget(self.comboBox)

        centerWidget= QWidget()
        centerWidget.setLayout(parentLayout)
        self.setCentralWidget(centerWidget)


app = QApplication([])
window = Window()


window.show()
app.exec()
