import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget, QDialog, QStackedWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt


class Heroes(QWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(1440,740)
        self.setWindowTitle("Mobile Legends Ultimate Guide")
        self.setWindowIcon(QIcon("Logo_Mobile_Legends-_Bang_Bang.jpg"))

        mainLayout = QHBoxLayout()
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(WidgetRadioButtons())
        self.stackedWidget.addWidget(WidgetButtons())

        buttonAsassin = QPushButton('Assassin')
        buttonAsassin.clicked.connect(self.nextWidget)
        buttonPrevious = QPushButton('Previous')
        buttonPrevious.clicked.connect(self.previousWidget)
        buttonNext = QPushButton('Next')
        buttonNext.clicked.connect(self.nextWidget)

        


        buttonLayout = QHBoxLayout()
        buttonLayout2 = QHBoxLayout()
        buttonLayout.addWidget(buttonPrevious)
        buttonLayout.addWidget(buttonNext)
        buttonLayout2.addWidget(buttonAsassin)

        mainLayout.addWidget(self.stackedWidget)
        mainLayout.addLayout(buttonLayout)
        self.setLayout(mainLayout)
    
    def nextWidget(self):
        self.stackedWidget.setCurrentIndex((self.stackedWidget.currentIndex() + 1) % 3)
    def previousWidget(self):
        self.stackedWidget.setCurrentIndex((self.stackedWidget.currentIndex() - 1) % 3)    

class WidgetRadioButtons(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Heroes", alignment=Qt.AlignmentFlag.AlignTop))
        layout.addWidget(QPushButton(f'Tank'))
        layout.addWidget(QPushButton(f'Fighter'))
        layout.addWidget(QPushButton(f'Mage'))

        self.setLayout(layout)

class WidgetButtons(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        for i in range(1,5):
            layout.addWidget(QPushButton(f'Heroe#{i}'))
        self.setLayout(layout)



app = QApplication(sys.argv)
demo = Heroes()

demo.show()
sys.exit(app.exec())