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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLCDNumber,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTextEdit, QVBoxLayout,
    QWidget)
import icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(670, 377)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 248, 254);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.iconnamewgt = QWidget(self.centralwidget)
        self.iconnamewgt.setObjectName(u"iconnamewgt")
        self.iconnamewgt.setStyleSheet(u"QWidget{\n"
"background-color: rgb(148, 148, 148);\n"
"}\n"
"QPushButton{\n"
"height:30px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"}\n"
"")
        self.gridLayout_2 = QGridLayout(self.iconnamewgt)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.signout = QPushButton(self.iconnamewgt)
        self.signout.setObjectName(u"signout")
        self.signout.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/icons/signoutbtn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.signout.setIcon(icon)
        self.signout.setCheckable(True)

        self.gridLayout_2.addWidget(self.signout, 3, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.iconnamewgt)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/icons/calcbtn.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.iconnamewgt)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Nirmala UI Semilight"])
        font.setPointSize(10)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.overbtn1 = QPushButton(self.iconnamewgt)
        self.overbtn1.setObjectName(u"overbtn1")
        self.overbtn1.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.overbtn1.setCheckable(True)
        self.overbtn1.setAutoDefault(True)

        self.verticalLayout_2.addWidget(self.overbtn1)

        self.herobtn1 = QPushButton(self.iconnamewgt)
        self.herobtn1.setObjectName(u"herobtn1")
        self.herobtn1.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.herobtn1.setCheckable(True)

        self.verticalLayout_2.addWidget(self.herobtn1)

        self.gamesbtn1 = QPushButton(self.iconnamewgt)
        self.gamesbtn1.setObjectName(u"gamesbtn1")
        self.gamesbtn1.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.gamesbtn1.setCheckable(True)

        self.verticalLayout_2.addWidget(self.gamesbtn1)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.iconnamewgt, 0, 1, 2, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(148, 148, 148);\n"
"}\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_9 = QPushButton(self.widget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(30, 30))
        self.pushButton_9.setMaximumSize(QSize(30, 30))
        self.pushButton_9.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/menubtn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon1)
        self.pushButton_9.setIconSize(QSize(40, 40))
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setAutoExclusive(True)
        self.pushButton_9.setAutoDefault(True)

        self.horizontalLayout.addWidget(self.pushButton_9)

        self.horizontalSpacer = QSpacerItem(288, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.pushButton_10 = QPushButton(self.widget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(40, 40))
        self.pushButton_10.setMaximumSize(QSize(40, 40))
        self.pushButton_10.setStyleSheet(u"QWidget{\n"
"	border:none;\n"
"background-color: rgb(148, 148, 148);\n"
"}\n"
"")
        self.pushButton_10.setIcon(icon)
        self.pushButton_10.setIconSize(QSize(30, 30))
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setAutoDefault(True)

        self.horizontalLayout_3.addWidget(self.pushButton_10)


        self.gridLayout_3.addWidget(self.widget, 0, 2, 1, 1)

        self.iconwgt = QWidget(self.centralwidget)
        self.iconwgt.setObjectName(u"iconwgt")
        self.iconwgt.setStyleSheet(u"QWidget{\n"
"background-color: rgb(148, 148, 148);\n"
"}\n"
"QPushButton{\n"
"height:30px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"}\n"
"")
        self.gridLayout = QGridLayout(self.iconwgt)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.iconwgt)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/icons/calcbtn.png"))
        self.label.setScaledContents(True)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.overallbtn = QPushButton(self.iconwgt)
        self.overallbtn.setObjectName(u"overallbtn")
        self.overallbtn.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.overallbtn.setCheckable(True)

        self.verticalLayout.addWidget(self.overallbtn)

        self.herobtn = QPushButton(self.iconwgt)
        self.herobtn.setObjectName(u"herobtn")
        self.herobtn.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.herobtn.setCheckable(True)

        self.verticalLayout.addWidget(self.herobtn)

        self.gamesbtn = QPushButton(self.iconwgt)
        self.gamesbtn.setObjectName(u"gamesbtn")
        self.gamesbtn.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.gamesbtn.setCheckable(True)

        self.verticalLayout.addWidget(self.gamesbtn)

        self.verticalSpacer_3 = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.iconwgt)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setCheckable(True)

        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.iconwgt, 0, 0, 2, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.overallpg = QWidget()
        self.overallpg.setObjectName(u"overallpg")
        self.label_4 = QLabel(self.overallpg)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(34, 59, 201, 41))
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic Light"])
        font1.setPointSize(20)
        self.label_4.setFont(font1)
        self.label_5 = QLabel(self.overallpg)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 110, 201, 41))
        self.label_5.setFont(font1)
        self.label_6 = QLabel(self.overallpg)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 160, 201, 41))
        self.label_6.setFont(font1)
        self.textEdit = QTextEdit(self.overallpg)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(220, 70, 131, 31))
        self.textEdit.setOverwriteMode(False)
        self.textEdit.setTextInteractionFlags(Qt.TextEditorInteraction)
        self.textEdit_2 = QTextEdit(self.overallpg)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(220, 120, 131, 31))
        self.textEdit_2.setOverwriteMode(False)
        self.textEdit_2.setTextInteractionFlags(Qt.TextEditorInteraction)
        self.lcdNumber = QLCDNumber(self.overallpg)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(220, 160, 131, 31))
        self.stackedWidget.addWidget(self.overallpg)
        self.heropg = QWidget()
        self.heropg.setObjectName(u"heropg")
        self.label_7 = QLabel(self.heropg)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(60, 90, 151, 41))
        self.label_7.setFont(font1)
        self.textEdit_3 = QTextEdit(self.heropg)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(240, 50, 131, 31))
        self.textEdit_3.setOverwriteMode(False)
        self.textEdit_3.setTextInteractionFlags(Qt.TextEditorInteraction)
        self.lcdNumber_2 = QLCDNumber(self.heropg)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setGeometry(QRect(240, 140, 131, 31))
        self.label_8 = QLabel(self.heropg)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 50, 171, 41))
        self.label_8.setFont(font1)
        self.textEdit_4 = QTextEdit(self.heropg)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(240, 100, 131, 31))
        self.textEdit_4.setOverwriteMode(False)
        self.textEdit_4.setTextInteractionFlags(Qt.TextEditorInteraction)
        self.label_9 = QLabel(self.heropg)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(140, 130, 81, 41))
        self.label_9.setFont(font1)
        self.stackedWidget.addWidget(self.heropg)
        self.gamespg = QWidget()
        self.gamespg.setObjectName(u"gamespg")
        self.lcdNumber_3 = QLCDNumber(self.gamespg)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")
        self.lcdNumber_3.setGeometry(QRect(260, 150, 131, 31))
        self.textEdit_5 = QTextEdit(self.gamespg)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(260, 60, 131, 31))
        self.textEdit_5.setOverwriteMode(False)
        self.textEdit_5.setTextInteractionFlags(Qt.TextEditorInteraction)
        self.label_10 = QLabel(self.gamespg)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(50, 150, 201, 41))
        self.label_10.setFont(font1)
        self.label_11 = QLabel(self.gamespg)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(110, 100, 131, 41))
        self.label_11.setFont(font1)
        self.textEdit_6 = QTextEdit(self.gamespg)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(260, 110, 131, 31))
        self.textEdit_6.setOverwriteMode(False)
        self.textEdit_6.setTextInteractionFlags(Qt.TextEditorInteraction)
        self.label_12 = QLabel(self.gamespg)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(160, 50, 91, 41))
        self.label_12.setFont(font1)
        self.stackedWidget.addWidget(self.gamespg)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_3.addWidget(self.stackedWidget, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.iconnamewgt.raise_()
        self.iconwgt.raise_()
        self.widget.raise_()
        self.stackedWidget.raise_()

        self.retranslateUi(MainWindow)
        self.pushButton_9.toggled.connect(self.iconwgt.setHidden)
        self.pushButton_9.toggled.connect(self.iconnamewgt.setVisible)
        self.gamesbtn.toggled.connect(self.gamesbtn1.setChecked)
        self.herobtn.toggled.connect(self.herobtn1.setChecked)
        self.overallbtn.toggled.connect(self.overbtn1.setChecked)
        self.gamesbtn1.toggled.connect(self.gamesbtn.setChecked)
        self.herobtn1.toggled.connect(self.herobtn.setChecked)
        self.pushButton_7.toggled.connect(MainWindow.close)
        self.signout.toggled.connect(MainWindow.close)
        self.pushButton_10.toggled.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.signout.setText(QCoreApplication.translate("MainWindow", u"Sign Out", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"WinRate\n"
"Calculator\n"
"", None))
        self.overbtn1.setText(QCoreApplication.translate("MainWindow", u"Overall", None))
        self.herobtn1.setText(QCoreApplication.translate("MainWindow", u"Hero", None))
        self.gamesbtn1.setText(QCoreApplication.translate("MainWindow", u"Games Needed", None))
        self.pushButton_9.setText("")
        self.pushButton_10.setText("")
        self.label.setText("")
        self.overallbtn.setText(QCoreApplication.translate("MainWindow", u"Overall", None))
        self.herobtn.setText(QCoreApplication.translate("MainWindow", u"Hero", None))
        self.gamesbtn.setText(QCoreApplication.translate("MainWindow", u"Games", None))
        self.pushButton_7.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Number Of Games:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Number Of Wins:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Winrate:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Number Of Wins:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Number Of Games:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Winrate:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Games Won Required:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Games Played:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"WinRate:", None))
    # retranslateUi

