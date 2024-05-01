import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QRadioButton,QStackedWidget,QVBoxLayout,QHBoxLayout,QLineEdit
from PyQt6.QtCore import Qt


class WidgetButtons(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        for i in range(4):
            layout.addWidget(QPushButton(f'Button #{i}'))
        
        self.setLayout(layout)

class WidgetLineEdits(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        for i in range(4):
            layout.addWidget(QLineEdit(f'LineEdit #{i}'))
        self.setLayout(layout)

class WidgetRadioButtons(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        for i in range(4):
            layout.addWidget(QRadioButton(f'RadioButton #{i}'))
        self.setLayout(layout)

class Heroes(QWidget):
    def __init__(self):
        super().__init__()

        mainLayout = QVBoxLayout()
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(WidgetButtons())
        self.stackedWidget.addWidget(WidgetLineEdits())
        self.stackedWidget.addWidget(WidgetRadioButtons())

        buttonPrevious = QPushButton('Previous')
        buttonPrevious.clicked.connect(self.previousWidget)
        buttonNext = QPushButton('Next')
        buttonNext.clicked.connect(self.nextWidget)
        


        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(buttonPrevious)
        buttonLayout.addWidget(buttonNext)

        mainLayout.addWidget(self.stackedWidget)
        mainLayout.addLayout(buttonLayout)
        self.setLayout(mainLayout)
    
    def nextWidget(self):
        self.stackedWidget.setCurrentIndex((self.stackedWidget.currentIndex() + 1) % 3)
    def previousWidget(self):
        self.stackedWidget.setCurrentIndex((self.stackedWidget.currentIndex() - 1) % 3)    



app = QApplication(sys.argv)
demo = Heroes()
demo.show()
sys.exit(app.exec())