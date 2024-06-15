from PySide6.QtCore import Qt
from calculatormain1_ui import Ui_MainWindow
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PySide6.QtSql import *
import sqlite3
import icon_rc

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Mobile Legends Guide")# Window Name

        self.iconnamewgt.setHidden(True)#to hide expandable sidebar

        #linking buttons to respective pages
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
    #defining pages according to index(0-11) page number in stacked widget 
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
        self.load_ranking_rewards()

    def switch_to_elitepg(self):
        self.stackedWidget.setCurrentIndex(5)
        self.load_ranking_rewards()

    def switch_to_masterpg(self):
        self.stackedWidget.setCurrentIndex(6)
        self.load_ranking_rewards()

    def switch_to_grandmasterpg(self):
        self.stackedWidget.setCurrentIndex(7)
        self.load_ranking_rewards()

    def switch_to_epicpg(self):
        self.stackedWidget.setCurrentIndex(8)
        self.load_ranking_rewards()

    def switch_to_legendpg(self):
        self.stackedWidget.setCurrentIndex(9)
        self.load_ranking_rewards()

    def switch_to_mythicpg(self):
        self.stackedWidget.setCurrentIndex(10)
        self.load_ranking_rewards()

    def switch_to_hononarypg(self):
        self.stackedWidget.setCurrentIndex(11)
        self.load_honorary_titles()
    #define buttons in overall winrate page
    def calculate1(self):
        self.calculate(self.now1, self.nog1, self.wrlabel1)
    #define buttons in hero page
    def calculate2(self):
        self.calculate(self.now2, self.nog2, self.wrlabel2)
    #define buttons in games required page
    def calculate3(self):
        input_text5 = self.cmtext.toPlainText()
        input_text6 = self.cwrtext.toPlainText()
        input_text7 = self.dwrtext.toPlainText()
        #calculate games required
        try:
            value1 = float(input_text5)
            value2 = float(input_text6)
            value3 = float(input_text7)
            result = (((((value3 / 100) * value1) - (value2 * value1 / 100)) / (1 - (value3 / 100))))
            self.gwreqlabel.setText(f"{int(result)}")
        #print error when error detected
        except ValueError:
            self.gwreqlabel.setText("Error")

    def calculate(self, now_widget, nog_widget, result_label):
        input_text1 = now_widget.toPlainText()
        input_text2 = nog_widget.toPlainText()

        try:#formula to calculate hero and overall winrate
            value1 = float(input_text1)
            value2 = float(input_text2)
            result = (value1 / value2) * 100
            result_label.setText(f"{result:.2f}%")
        except ValueError:
            result_label.setText("Error")

    def load_data(self):#define tables from database
        self.load_ranking_rewards()
        self.load_honorary_titles()

    def load_ranking_rewards(self):#read data from database
        try:
            conn = sqlite3.connect('rank.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM "Ranking Rewards" ORDER BY id')
            data = cursor.fetchall()
            labels = [self.warriorinfo, self.eliteinfo, self.masterinfo, self.grandmasterinfo, self.epicinfo, self.legendinfo, self.myhticinfo]

            for i, row in enumerate(data[:7]):#print data accordingly to id(7rows) in different labels
                display_text = "\n".join(f"• {str(item)}" for item in row[2:])#print data starting from the second row
                labels[i].setText(display_text)
        except sqlite3.Error as e:
            print(f"Database error: {e}")#print e when data is unable to be retrieved
        finally:
            if conn:
                conn.close()

    def load_honorary_titles(self):
        try:
            conn = sqlite3.connect('titles.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM "hononary titles" ORDER BY id')
            data = cursor.fetchall()
            labels = [self.beginnerlbl, self.juniorlbl, self.seniorlbl, self.suprelbl]#labels in hononary page

            for i, row in enumerate(data[:4]):
                display_text = "\n".join(f"• {str(item)}" for item in row[1:])#print data starting from first row
                labels[i].setText(display_text)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            if conn:
                conn.close()

def main():
    app = QApplication([])
    window = MySideBar()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
