from calculatormain1 import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget


class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Sidebar Menu")

        self.iconnamewgt.setHidden(True)

        self.overallbtn.clicked.connect(self.switch_to_overallpg)
        self.overbtn1.clicked.connect(self.switch_to_overallpg)
       
        self.herobtn.clicked.connect(self.switch_to_heropg)
        self.herobtn1.clicked.connect(self.switch_to_heropg)
       
        self.gamesbtn.clicked.connect(self.switch_to_gamespg)
        self.gamesbtn1.clicked.connect(self.switch_to_gamespg)

        self.calcbtn1.clicked.connect(self.calculate1)
        self.calcbtn2.clicked.connect(self.calculate2)
        self.calcbtn3.clicked.connect(self.calculate3)

    def switch_to_overallpg(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def switch_to_heropg(self):
        self.stackedWidget.setCurrentIndex(1)
   
    def switch_to_gamespg(self):
        self.stackedWidget.setCurrentIndex(2)

    def calculate1(self):
        input_text1 = self.now1.toPlainText()
        input_text2 = self.nog1.toPlainText()

        try:
            value1 = float(input_text1)
            value2 = float(input_text2)
            result = (value1 / value2) * 100
            self.wrlabel1.setText(f" {result:.2f}%")
        except Exception as e:
            self.wrlabel1.setText(f"Error: {e}")

    def calculate2(self):
        input_text3 = self.now2.toPlainText()
        input_text4 = self.nog2.toPlainText()

        try:
            value1 = float(input_text3)
            value2 = float(input_text4)
            result = (value1 / value2) * 100
            self.wrlabel2.setText(f" {result:.2f}%")
        except Exception as e:
            self.wrlabel2.setText(f"Error: {e}")
    
    def calculate3(self):
        input_text5 = self.cmtext.toPlainText()
        input_text6 = self.cwrtext.toPlainText()
        input_text7 = self.dwrtext.toPlainText()
        try:
            value1 = float(input_text5)
            value2 = float(input_text6)
            value3 = float(input_text7) 
            result = ((value1 * value2) -(value1 * value3))/ (value2 -100)
            self.gwreqlabel.setText(f" {int(result)}")
        except Exception as e:
            self.gwreqlabel.setText(f"Error: {e}")


def main():
    app = QApplication([])
    window = MySideBar()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()