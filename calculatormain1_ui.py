# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculatormain1.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget)
import icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(698, 427)
        MainWindow.setStyleSheet(u"background-color: rgb(100,181,246);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.iconwgt = QWidget(self.centralwidget)
        self.iconwgt.setObjectName(u"iconwgt")
        self.iconwgt.setStyleSheet(u"\n"
"QPushButton{\n"
"height:30px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"}\n"
"\n"
"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"\n"
"")
        self.gridLayout = QGridLayout(self.iconwgt)
        self.gridLayout.setObjectName(u"gridLayout")
        self.icon = QLabel(self.iconwgt)
        self.icon.setObjectName(u"icon")
        self.icon.setMinimumSize(QSize(40, 40))
        self.icon.setMaximumSize(QSize(40, 40))
        self.icon.setStyleSheet(u"QLabel {\n"
"    border-radius: 200px\n"
"\n"
"}\n"
"")
        self.icon.setPixmap(QPixmap(u":/icons/mlbb.jpg"))
        self.icon.setScaledContents(True)

        self.gridLayout.addWidget(self.icon, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.overallbtn = QPushButton(self.iconwgt)
        self.overallbtn.setObjectName(u"overallbtn")
        self.overallbtn.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.overallbtn.setCheckable(True)

        self.verticalLayout.addWidget(self.overallbtn)

        self.herobtn = QPushButton(self.iconwgt)
        self.herobtn.setObjectName(u"herobtn")
        self.herobtn.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.herobtn.setCheckable(True)

        self.verticalLayout.addWidget(self.herobtn)

        self.gamesbtn = QPushButton(self.iconwgt)
        self.gamesbtn.setObjectName(u"gamesbtn")
        self.gamesbtn.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.gamesbtn.setCheckable(True)

        self.verticalLayout.addWidget(self.gamesbtn)

        self.rrbtn = QPushButton(self.iconwgt)
        self.rrbtn.setObjectName(u"rrbtn")
        self.rrbtn.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.rrbtn.setCheckable(True)

        self.verticalLayout.addWidget(self.rrbtn)

        self.verticalSpacer_3 = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.signout_2 = QPushButton(self.iconwgt)
        self.signout_2.setObjectName(u"signout_2")
        self.signout_2.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/signout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.signout_2.setIcon(icon1)
        self.signout_2.setIconSize(QSize(30, 30))
        self.signout_2.setCheckable(True)

        self.gridLayout.addWidget(self.signout_2, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.iconwgt, 0, 0, 2, 1)

        self.iconnamewgt = QWidget(self.centralwidget)
        self.iconnamewgt.setObjectName(u"iconnamewgt")
        self.iconnamewgt.setStyleSheet(u"\n"
"QPushButton{\n"
"height:30px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"}\n"
"\n"
"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;")
        self.gridLayout_4 = QGridLayout(self.iconnamewgt)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.signout = QPushButton(self.iconnamewgt)
        self.signout.setObjectName(u"signout")
        self.signout.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.signout.setIcon(icon1)
        self.signout.setIconSize(QSize(30, 30))
        self.signout.setCheckable(True)

        self.gridLayout_4.addWidget(self.signout, 2, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.overbtn1 = QPushButton(self.iconnamewgt)
        self.overbtn1.setObjectName(u"overbtn1")
        self.overbtn1.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.overbtn1.setCheckable(True)
        self.overbtn1.setAutoDefault(True)

        self.verticalLayout_2.addWidget(self.overbtn1)

        self.herobtn1 = QPushButton(self.iconnamewgt)
        self.herobtn1.setObjectName(u"herobtn1")
        self.herobtn1.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.herobtn1.setCheckable(True)

        self.verticalLayout_2.addWidget(self.herobtn1)

        self.gamesbtn1 = QPushButton(self.iconnamewgt)
        self.gamesbtn1.setObjectName(u"gamesbtn1")
        self.gamesbtn1.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.gamesbtn1.setCheckable(True)

        self.verticalLayout_2.addWidget(self.gamesbtn1)

        self.rrbtn1 = QPushButton(self.iconnamewgt)
        self.rrbtn1.setObjectName(u"rrbtn1")
        self.rrbtn1.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.rrbtn1.setCheckable(True)

        self.verticalLayout_2.addWidget(self.rrbtn1)

        self.verticalSpacer_2 = QSpacerItem(88, 142, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.gridLayout_4.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.iconnamewgt)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setStyleSheet(u"QLabel{\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"}")
        self.label_2.setPixmap(QPixmap(u":/icons/mlbb.jpg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.iconnamewgt)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"MS Serif"])
        font.setPointSize(4)
        font.setBold(False)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 4pt \"MS Serif\";\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.label_3)


        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.iconnamewgt, 0, 1, 2, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.gridLayout_12 = QGridLayout(self.widget)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.signout_3 = QPushButton(self.widget)
        self.signout_3.setObjectName(u"signout_3")
        self.signout_3.setMinimumSize(QSize(40, 40))
        self.signout_3.setMaximumSize(QSize(40, 40))
        self.signout_3.setStyleSheet(u"\n"
"border: none\n"
"")
        self.signout_3.setIcon(icon1)
        self.signout_3.setIconSize(QSize(40, 40))
        self.signout_3.setCheckable(True)
        self.signout_3.setAutoDefault(True)

        self.gridLayout_12.addWidget(self.signout_3, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_9 = QPushButton(self.widget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(30, 30))
        self.pushButton_9.setMaximumSize(QSize(30, 30))
        self.pushButton_9.setStyleSheet(u"border: none")
        icon2 = QIcon()
        icon2.addFile(u":/icons/menubtn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setIconSize(QSize(40, 40))
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setAutoExclusive(True)
        self.pushButton_9.setAutoDefault(True)

        self.horizontalLayout.addWidget(self.pushButton_9)

        self.horizontalSpacer = QSpacerItem(288, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_12.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 2, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.overallpg = QWidget()
        self.overallpg.setObjectName(u"overallpg")
        self.calcbtn1 = QPushButton(self.overallpg)
        self.calcbtn1.setObjectName(u"calcbtn1")
        self.calcbtn1.setGeometry(QRect(190, 240, 111, 31))
        font1 = QFont()
        font1.setFamilies([u"MS Sans Serif"])
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setItalic(False)
        self.calcbtn1.setFont(font1)
        self.calcbtn1.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.calcbtn1.setCheckable(True)
        self.layoutWidget = QWidget(self.overallpg)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(80, 50, 351, 168))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_6)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.nog1 = QTextEdit(self.layoutWidget)
        self.nog1.setObjectName(u"nog1")
        self.nog1.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.nog1.setOverwriteMode(False)
        self.nog1.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.verticalLayout_6.addWidget(self.nog1)

        self.now1 = QTextEdit(self.layoutWidget)
        self.now1.setObjectName(u"now1")
        self.now1.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.now1.setOverwriteMode(False)
        self.now1.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.verticalLayout_6.addWidget(self.now1)

        self.wrlabel1 = QLabel(self.layoutWidget)
        self.wrlabel1.setObjectName(u"wrlabel1")
        self.wrlabel1.setMinimumSize(QSize(0, 50))
        self.wrlabel1.setFont(font1)
        self.wrlabel1.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.wrlabel1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.wrlabel1)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)

        self.stackedWidget.addWidget(self.overallpg)
        self.heropg = QWidget()
        self.heropg.setObjectName(u"heropg")
        self.calcbtn2 = QPushButton(self.heropg)
        self.calcbtn2.setObjectName(u"calcbtn2")
        self.calcbtn2.setGeometry(QRect(190, 230, 111, 31))
        self.calcbtn2.setFont(font1)
        self.calcbtn2.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.calcbtn2.setCheckable(True)
        self.layoutWidget1 = QWidget(self.heropg)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(80, 40, 331, 166))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_8 = QLabel(self.layoutWidget1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_8)

        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_7)

        self.label_9 = QLabel(self.layoutWidget1)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_9)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.nog2 = QTextEdit(self.layoutWidget1)
        self.nog2.setObjectName(u"nog2")
        self.nog2.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.nog2.setOverwriteMode(False)
        self.nog2.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.verticalLayout_8.addWidget(self.nog2)

        self.now2 = QTextEdit(self.layoutWidget1)
        self.now2.setObjectName(u"now2")
        self.now2.setMinimumSize(QSize(10, 50))
        self.now2.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.now2.setOverwriteMode(False)
        self.now2.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.verticalLayout_8.addWidget(self.now2)

        self.wrlabel2 = QLabel(self.layoutWidget1)
        self.wrlabel2.setObjectName(u"wrlabel2")
        self.wrlabel2.setMinimumSize(QSize(0, 50))
        self.wrlabel2.setMaximumSize(QSize(16777215, 16777215))
        self.wrlabel2.setFont(font1)
        self.wrlabel2.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.wrlabel2.setLineWidth(0)
        self.wrlabel2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.wrlabel2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_8)

        self.stackedWidget.addWidget(self.heropg)
        self.gamespg = QWidget()
        self.gamespg.setObjectName(u"gamespg")
        self.calcbtn3 = QPushButton(self.gamespg)
        self.calcbtn3.setObjectName(u"calcbtn3")
        self.calcbtn3.setGeometry(QRect(190, 240, 111, 31))
        self.calcbtn3.setFont(font1)
        self.calcbtn3.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.calcbtn3.setCheckable(True)
        self.layoutWidget2 = QWidget(self.gamespg)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(60, 10, 371, 222))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 15, -1)
        self.label = QLabel(self.layoutWidget2)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.label_11 = QLabel(self.layoutWidget2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_11)

        self.label_10 = QLabel(self.layoutWidget2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_10)

        self.label_12 = QLabel(self.layoutWidget2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_12)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.cmtext = QTextEdit(self.layoutWidget2)
        self.cmtext.setObjectName(u"cmtext")
        self.cmtext.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.cmtext.setOverwriteMode(False)
        self.cmtext.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.verticalLayout_7.addWidget(self.cmtext)

        self.cwrtext = QTextEdit(self.layoutWidget2)
        self.cwrtext.setObjectName(u"cwrtext")
        self.cwrtext.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.cwrtext.setOverwriteMode(False)
        self.cwrtext.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.verticalLayout_7.addWidget(self.cwrtext)

        self.dwrtext = QTextEdit(self.layoutWidget2)
        self.dwrtext.setObjectName(u"dwrtext")
        self.dwrtext.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.dwrtext.setOverwriteMode(False)
        self.dwrtext.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.verticalLayout_7.addWidget(self.dwrtext)

        self.gwreqlabel = QLabel(self.layoutWidget2)
        self.gwreqlabel.setObjectName(u"gwreqlabel")
        self.gwreqlabel.setMinimumSize(QSize(0, 50))
        self.gwreqlabel.setFont(font1)
        self.gwreqlabel.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.gwreqlabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.gwreqlabel)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.stackedWidget.addWidget(self.gamespg)
        self.rankpg = QWidget()
        self.rankpg.setObjectName(u"rankpg")
        self.gridLayout_13 = QGridLayout(self.rankpg)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_23 = QLabel(self.rankpg)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 70))
        self.label_23.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamilies([u"MS Serif"])
        font2.setPointSize(27)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_23.setFont(font2)
        self.label_23.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 27pt \"MS Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_23, 0, 0, 1, 1)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.epicbtn = QPushButton(self.rankpg)
        self.epicbtn.setObjectName(u"epicbtn")
        self.epicbtn.setMinimumSize(QSize(0, 100))
        self.epicbtn.setMaximumSize(QSize(120, 90))
        self.epicbtn.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Epic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.epicbtn.setIcon(icon3)
        self.epicbtn.setIconSize(QSize(80, 80))

        self.horizontalLayout_8.addWidget(self.epicbtn)

        self.legendbtn = QPushButton(self.rankpg)
        self.legendbtn.setObjectName(u"legendbtn")
        self.legendbtn.setMinimumSize(QSize(0, 100))
        self.legendbtn.setMaximumSize(QSize(120, 90))
        self.legendbtn.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/Legend.png", QSize(), QIcon.Normal, QIcon.Off)
        self.legendbtn.setIcon(icon4)
        self.legendbtn.setIconSize(QSize(80, 80))

        self.horizontalLayout_8.addWidget(self.legendbtn)

        self.mythicbtn = QPushButton(self.rankpg)
        self.mythicbtn.setObjectName(u"mythicbtn")
        self.mythicbtn.setMinimumSize(QSize(0, 100))
        self.mythicbtn.setMaximumSize(QSize(120, 90))
        self.mythicbtn.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/Mythic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mythicbtn.setIcon(icon5)
        self.mythicbtn.setIconSize(QSize(80, 80))

        self.horizontalLayout_8.addWidget(self.mythicbtn)

        self.honorbtn = QPushButton(self.rankpg)
        self.honorbtn.setObjectName(u"honorbtn")
        self.honorbtn.setMinimumSize(QSize(0, 100))
        self.honorbtn.setMaximumSize(QSize(120, 90))
        self.honorbtn.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.honorbtn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.honorbtn)


        self.gridLayout_11.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.warriorbtn = QPushButton(self.rankpg)
        self.warriorbtn.setObjectName(u"warriorbtn")
        self.warriorbtn.setMinimumSize(QSize(0, 100))
        self.warriorbtn.setMaximumSize(QSize(120, 90))
        self.warriorbtn.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/Warrior.png", QSize(), QIcon.Normal, QIcon.Off)
        self.warriorbtn.setIcon(icon6)
        self.warriorbtn.setIconSize(QSize(80, 90))
        self.warriorbtn.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.warriorbtn)

        self.elitebtn = QPushButton(self.rankpg)
        self.elitebtn.setObjectName(u"elitebtn")
        self.elitebtn.setMinimumSize(QSize(0, 100))
        self.elitebtn.setMaximumSize(QSize(120, 90))
        self.elitebtn.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/Elite.png", QSize(), QIcon.Normal, QIcon.Off)
        self.elitebtn.setIcon(icon7)
        self.elitebtn.setIconSize(QSize(80, 80))

        self.horizontalLayout_7.addWidget(self.elitebtn)

        self.masterbtn = QPushButton(self.rankpg)
        self.masterbtn.setObjectName(u"masterbtn")
        self.masterbtn.setMinimumSize(QSize(0, 100))
        self.masterbtn.setMaximumSize(QSize(120, 90))
        self.masterbtn.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/Master.png", QSize(), QIcon.Normal, QIcon.Off)
        self.masterbtn.setIcon(icon8)
        self.masterbtn.setIconSize(QSize(80, 80))

        self.horizontalLayout_7.addWidget(self.masterbtn)

        self.grandmasterbtn = QPushButton(self.rankpg)
        self.grandmasterbtn.setObjectName(u"grandmasterbtn")
        self.grandmasterbtn.setMinimumSize(QSize(0, 100))
        self.grandmasterbtn.setMaximumSize(QSize(120, 90))
        self.grandmasterbtn.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/Grandmaster.png", QSize(), QIcon.Normal, QIcon.Off)
        self.grandmasterbtn.setIcon(icon9)
        self.grandmasterbtn.setIconSize(QSize(80, 80))

        self.horizontalLayout_7.addWidget(self.grandmasterbtn)


        self.gridLayout_11.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_11, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.rankpg)
        self.warriorpg = QWidget()
        self.warriorpg.setObjectName(u"warriorpg")
        self.gridLayout_10 = QGridLayout(self.warriorpg)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.rtrnbtn1 = QPushButton(self.warriorpg)
        self.rtrnbtn1.setObjectName(u"rtrnbtn1")
        self.rtrnbtn1.setMinimumSize(QSize(0, 40))
        self.rtrnbtn1.setMaximumSize(QSize(50, 16777215))
        self.rtrnbtn1.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")

        self.gridLayout_10.addWidget(self.rtrnbtn1, 0, 0, 1, 1)

        self.label_24 = QLabel(self.warriorpg)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 27pt \"MS Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_24, 0, 1, 1, 1)

        self.warriorinfo = QLabel(self.warriorpg)
        self.warriorinfo.setObjectName(u"warriorinfo")
        self.warriorinfo.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 27pt \"MS Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.warriorinfo.setTextFormat(Qt.PlainText)
        self.warriorinfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_10.addWidget(self.warriorinfo, 1, 0, 1, 2)

        self.stackedWidget.addWidget(self.warriorpg)
        self.elitepg = QWidget()
        self.elitepg.setObjectName(u"elitepg")
        self.gridLayout_9 = QGridLayout(self.elitepg)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.rtrnbtn2 = QPushButton(self.elitepg)
        self.rtrnbtn2.setObjectName(u"rtrnbtn2")
        self.rtrnbtn2.setMinimumSize(QSize(0, 40))
        self.rtrnbtn2.setMaximumSize(QSize(50, 16777215))
        self.rtrnbtn2.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")

        self.gridLayout_9.addWidget(self.rtrnbtn2, 0, 0, 1, 1)

        self.label_25 = QLabel(self.elitepg)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 27pt \"MS Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_25, 0, 1, 1, 1)

        self.eliteinfo = QLabel(self.elitepg)
        self.eliteinfo.setObjectName(u"eliteinfo")
        self.eliteinfo.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 27pt \"MS Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.eliteinfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_9.addWidget(self.eliteinfo, 1, 0, 1, 2)

        self.stackedWidget.addWidget(self.elitepg)
        self.masterpg = QWidget()
        self.masterpg.setObjectName(u"masterpg")
        self.gridLayout_8 = QGridLayout(self.masterpg)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.rtrnbtn3 = QPushButton(self.masterpg)
        self.rtrnbtn3.setObjectName(u"rtrnbtn3")
        self.rtrnbtn3.setMinimumSize(QSize(0, 40))
        self.rtrnbtn3.setMaximumSize(QSize(50, 16777215))
        self.rtrnbtn3.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")

        self.gridLayout_8.addWidget(self.rtrnbtn3, 0, 0, 1, 1)

        self.label_26 = QLabel(self.masterpg)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 27pt \"MS Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_26, 0, 1, 1, 1)

        self.masterinfo = QLabel(self.masterpg)
        self.masterinfo.setObjectName(u"masterinfo")
        self.masterinfo.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 27pt \"MS Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.masterinfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_8.addWidget(self.masterinfo, 1, 0, 1, 2)

        self.stackedWidget.addWidget(self.masterpg)
        self.grandmasterpg = QWidget()
        self.grandmasterpg.setObjectName(u"grandmasterpg")
        self.gridLayout_7 = QGridLayout(self.grandmasterpg)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.rtrnbtn4 = QPushButton(self.grandmasterpg)
        self.rtrnbtn4.setObjectName(u"rtrnbtn4")
        self.rtrnbtn4.setMinimumSize(QSize(0, 40))
        self.rtrnbtn4.setMaximumSize(QSize(50, 16777215))
        self.rtrnbtn4.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")

        self.gridLayout_7.addWidget(self.rtrnbtn4, 0, 0, 1, 1)

        self.label_27 = QLabel(self.grandmasterpg)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 27pt \"MS Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_27, 0, 1, 1, 1)

        self.grandmasterinfo = QLabel(self.grandmasterpg)
        self.grandmasterinfo.setObjectName(u"grandmasterinfo")
        self.grandmasterinfo.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 27pt \"MS Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.grandmasterinfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_7.addWidget(self.grandmasterinfo, 1, 0, 1, 2)

        self.stackedWidget.addWidget(self.grandmasterpg)
        self.epicpg = QWidget()
        self.epicpg.setObjectName(u"epicpg")
        self.gridLayout_6 = QGridLayout(self.epicpg)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.rtrnbtn5 = QPushButton(self.epicpg)
        self.rtrnbtn5.setObjectName(u"rtrnbtn5")
        self.rtrnbtn5.setMinimumSize(QSize(40, 50))
        self.rtrnbtn5.setMaximumSize(QSize(50, 16777215))
        self.rtrnbtn5.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")

        self.gridLayout_6.addWidget(self.rtrnbtn5, 0, 0, 1, 1)

        self.label_28 = QLabel(self.epicpg)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 27pt \"MS Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_28, 0, 1, 1, 1)

        self.epicinfo = QLabel(self.epicpg)
        self.epicinfo.setObjectName(u"epicinfo")
        self.epicinfo.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 27pt \"MS Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.epicinfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_6.addWidget(self.epicinfo, 1, 0, 1, 2)

        self.stackedWidget.addWidget(self.epicpg)
        self.legendpg = QWidget()
        self.legendpg.setObjectName(u"legendpg")
        self.gridLayout_5 = QGridLayout(self.legendpg)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.rtrnbtn6 = QPushButton(self.legendpg)
        self.rtrnbtn6.setObjectName(u"rtrnbtn6")
        self.rtrnbtn6.setMinimumSize(QSize(0, 40))
        self.rtrnbtn6.setMaximumSize(QSize(50, 16777215))
        self.rtrnbtn6.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")

        self.gridLayout_5.addWidget(self.rtrnbtn6, 0, 0, 1, 1)

        self.label_29 = QLabel(self.legendpg)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 27pt \"MS Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_29, 0, 1, 1, 1)

        self.legendinfo = QLabel(self.legendpg)
        self.legendinfo.setObjectName(u"legendinfo")
        self.legendinfo.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 27pt \"MS Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.legendinfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_5.addWidget(self.legendinfo, 1, 0, 1, 2)

        self.stackedWidget.addWidget(self.legendpg)
        self.mythicpg = QWidget()
        self.mythicpg.setObjectName(u"mythicpg")
        self.gridLayout_3 = QGridLayout(self.mythicpg)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.rtrnbtn7 = QPushButton(self.mythicpg)
        self.rtrnbtn7.setObjectName(u"rtrnbtn7")
        self.rtrnbtn7.setMinimumSize(QSize(40, 40))
        self.rtrnbtn7.setMaximumSize(QSize(50, 16777215))
        self.rtrnbtn7.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.rtrnbtn7.setIconSize(QSize(40, 40))

        self.gridLayout_3.addWidget(self.rtrnbtn7, 0, 0, 1, 1)

        self.label_30 = QLabel(self.mythicpg)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 0))
        self.label_30.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 27pt \"MS Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_30, 0, 1, 1, 1)

        self.myhticinfo = QLabel(self.mythicpg)
        self.myhticinfo.setObjectName(u"myhticinfo")
        self.myhticinfo.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 27pt \"MS Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.myhticinfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_3.addWidget(self.myhticinfo, 1, 0, 1, 2)

        self.stackedWidget.addWidget(self.mythicpg)
        self.hononarypg = QWidget()
        self.hononarypg.setObjectName(u"hononarypg")
        self.label_31 = QLabel(self.hononarypg)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(10, 30, 471, 261))
        self.label_31.setStyleSheet(u"background-color: rgb(100,181,246);")
        self.label_31.setTextFormat(Qt.AutoText)
        self.label_31.setPixmap(QPixmap(u":/icons/honorary titles.png"))
        self.label_31.setScaledContents(True)
        self.label_31.setAlignment(Qt.AlignCenter)
        self.beginnerlbl = QLabel(self.hononarypg)
        self.beginnerlbl.setObjectName(u"beginnerlbl")
        self.beginnerlbl.setGeometry(QRect(10, 80, 121, 81))
        self.beginnerlbl.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.beginnerlbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.juniorlbl = QLabel(self.hononarypg)
        self.juniorlbl.setObjectName(u"juniorlbl")
        self.juniorlbl.setGeometry(QRect(360, 80, 121, 81))
        self.juniorlbl.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.juniorlbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.suprelbl = QLabel(self.hononarypg)
        self.suprelbl.setObjectName(u"suprelbl")
        self.suprelbl.setGeometry(QRect(360, 170, 121, 81))
        self.suprelbl.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.suprelbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.seniorlbl = QLabel(self.hononarypg)
        self.seniorlbl.setObjectName(u"seniorlbl")
        self.seniorlbl.setGeometry(QRect(10, 170, 121, 81))
        self.seniorlbl.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"")
        self.seniorlbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.stackedWidget.addWidget(self.hononarypg)

        self.gridLayout_2.addWidget(self.stackedWidget, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_9.toggled.connect(self.iconwgt.setHidden)
        self.pushButton_9.toggled.connect(self.iconnamewgt.setVisible)
        self.gamesbtn.toggled.connect(self.gamesbtn1.setChecked)
        self.herobtn.toggled.connect(self.herobtn1.setChecked)
        self.overallbtn.toggled.connect(self.overbtn1.setChecked)
        self.gamesbtn1.toggled.connect(self.gamesbtn.setChecked)
        self.herobtn1.toggled.connect(self.herobtn.setChecked)
        self.signout_2.toggled.connect(MainWindow.close)
        self.signout.toggled.connect(MainWindow.close)
        self.signout_3.toggled.connect(MainWindow.close)
        self.rrbtn.toggled.connect(self.rrbtn1.setChecked)
        self.rrbtn1.toggled.connect(self.rrbtn.setChecked)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.icon.setText("")
        self.overallbtn.setText(QCoreApplication.translate("MainWindow", u"Overall", None))
        self.herobtn.setText(QCoreApplication.translate("MainWindow", u"Hero", None))
        self.gamesbtn.setText(QCoreApplication.translate("MainWindow", u"Games", None))
        self.rrbtn.setText(QCoreApplication.translate("MainWindow", u"Rank", None))
        self.signout_2.setText("")
        self.signout.setText(QCoreApplication.translate("MainWindow", u"Sign Out", None))
        self.overbtn1.setText(QCoreApplication.translate("MainWindow", u"Overall", None))
        self.herobtn1.setText(QCoreApplication.translate("MainWindow", u"Hero", None))
        self.gamesbtn1.setText(QCoreApplication.translate("MainWindow", u"Games Needed", None))
        self.rrbtn1.setText(QCoreApplication.translate("MainWindow", u"Rank Rewards", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"WinRate\n"
"Calculator\n"
"", None))
        self.signout_3.setText("")
        self.pushButton_9.setText("")
        self.calcbtn1.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Number Of Games:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Number Of Wins:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Winrate:", None))
#if QT_CONFIG(tooltip)
        self.nog1.setToolTip(QCoreApplication.translate("MainWindow", u"input1", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.now1.setToolTip(QCoreApplication.translate("MainWindow", u"input2", None))
#endif // QT_CONFIG(tooltip)
        self.wrlabel1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.calcbtn2.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Number Of Games:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Number Of Wins:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Winrate:", None))
#if QT_CONFIG(tooltip)
        self.nog2.setToolTip(QCoreApplication.translate("MainWindow", u"input3", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.now2.setToolTip(QCoreApplication.translate("MainWindow", u"input4", None))
#endif // QT_CONFIG(tooltip)
        self.wrlabel2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.calcbtn3.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Current Matches:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Current Winrate:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Desired Winrate:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Games Won Required:", None))
#if QT_CONFIG(tooltip)
        self.cmtext.setToolTip(QCoreApplication.translate("MainWindow", u"input5", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cwrtext.setToolTip(QCoreApplication.translate("MainWindow", u"input6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.dwrtext.setToolTip(QCoreApplication.translate("MainWindow", u"input6", None))
#endif // QT_CONFIG(tooltip)
        self.gwreqlabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Rank Rewards", None))
        self.epicbtn.setText("")
        self.legendbtn.setText("")
        self.mythicbtn.setText("")
        self.honorbtn.setText(QCoreApplication.translate("MainWindow", u"Hononary", None))
        self.warriorbtn.setText("")
        self.elitebtn.setText("")
        self.masterbtn.setText("")
        self.grandmasterbtn.setText("")
        self.rtrnbtn1.setText(QCoreApplication.translate("MainWindow", u"Return", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Warrior Rewards", None))
        self.warriorinfo.setText("")
        self.rtrnbtn2.setText(QCoreApplication.translate("MainWindow", u"Return", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Elite Rewards", None))
        self.eliteinfo.setText("")
        self.rtrnbtn3.setText(QCoreApplication.translate("MainWindow", u"Return", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Master Rewards", None))
        self.masterinfo.setText("")
        self.rtrnbtn4.setText(QCoreApplication.translate("MainWindow", u"Return", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Grandmaster Rewards", None))
        self.grandmasterinfo.setText("")
        self.rtrnbtn5.setText(QCoreApplication.translate("MainWindow", u"Return", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Epic Rewards", None))
        self.epicinfo.setText("")
        self.rtrnbtn6.setText(QCoreApplication.translate("MainWindow", u"Return", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Legend Rewards", None))
        self.legendinfo.setText("")
        self.rtrnbtn7.setText(QCoreApplication.translate("MainWindow", u"Return", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Myhtic Rewards", None))
        self.myhticinfo.setText("")
        self.label_31.setText("")
        self.beginnerlbl.setText("")
        self.juniorlbl.setText("")
        self.suprelbl.setText("")
        self.seniorlbl.setText("")
    # retranslateUi

