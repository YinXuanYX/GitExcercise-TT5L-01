from calculatormain1 import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow
import sqlite3
import icon_rc

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

        self.rrbtn.clicked.connect(self.switch_to_rankpg)
        self.rrbtn1.clicked.connect(self.switch_to_rankpg)

        self.calcbtn1.clicked.connect(self.calculate1)
        self.calcbtn2.clicked.connect(self.calculate2)
        self.calcbtn3.clicked.connect(self.calculate3)

        self.warriorbtn.clicked.connect(self.switch_to_warriorpg)
        self.masterbtn.clicked.connect(self.switch_to_masterpg)
        self.elitebtn.clicked.connect(self.switch_to_elitepg)
        self.grandmasterbtn.clicked.connect(self.switch_to_grandmasterpg)
        self.epicbtn.clicked.connect(self.switch_to_epicpg)
        self.legendbtn.clicked.connect(self.switch_to_legendpg)
        self.mythicbtn.clicked.connect(self.switch_to_mythicpg)
        self.rtrnbtn1.clicked.connect(self.switch_to_rankpg)
        self.rtrnbtn2.clicked.connect(self.switch_to_rankpg)
        self.rtrnbtn3.clicked.connect(self.switch_to_rankpg)
        self.rtrnbtn4.clicked.connect(self.switch_to_rankpg)
        self.rtrnbtn5.clicked.connect(self.switch_to_rankpg)
        self.rtrnbtn6.clicked.connect(self.switch_to_rankpg)
        self.rtrnbtn7.clicked.connect(self.switch_to_rankpg)
        self.honorbtn.clicked.connect(self.switch_to_hononarypg)
        self.load_data()
    
    def switch_to_overallpg(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def switch_to_heropg(self):
        self.stackedWidget.setCurrentIndex(1)
   
    def switch_to_gamespg(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_rankpg(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_warriorpg(self):
        self.stackedWidget.setCurrentIndex(4)
        self.load_data()

    def switch_to_elitepg(self):
        self.stackedWidget.setCurrentIndex(5)
        self.load_data()

    def switch_to_masterpg(self):
        self.stackedWidget.setCurrentIndex(6)
        self.load_data()

    def switch_to_grandmasterpg(self):
        self.stackedWidget.setCurrentIndex(7)
        self.load_data()

    def switch_to_epicpg(self):
        self.stackedWidget.setCurrentIndex(8)
        self.load_data()

    def switch_to_legendpg(self):
        self.stackedWidget.setCurrentIndex(9)
        self.load_data()

    def switch_to_mythicpg(self):
        self.stackedWidget.setCurrentIndex(10)
        self.load_data()

    def switch_to_hononarypg(self):
        self.stackedWidget.setCurrentIndex(11)
        self.load_data()


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
            result = (((((value3 / 100) * value1) - (value2 * value1 / 100)) / (1 - (value3 / 100))))
            self.gwreqlabel.setText(f" {int(result)}")
        except Exception as e:
            self.gwreqlabel.setText(f"Error: {e}")

    def load_data(self):
        conn = sqlite3.connect('rank.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM "Ranking Rewards" ORDER BY id')
        data = cursor.fetchall()

        labels = [self.warriorinfo, self.eliteinfo, self.masterinfo, self.grandmasterinfo, self.epicinfo, self.legendinfo, self.myhticinfo]
        
        for i, row in enumerate(data[:7]): 
            display_text = "\n".join(f"• {str(item)}" for item in row[2:])
            labels[i].setText(display_text)

        conn.close()
             
def main():
    app = QApplication([])
    window = MySideBar()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
