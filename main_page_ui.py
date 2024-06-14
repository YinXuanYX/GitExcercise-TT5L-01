# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_page.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1402, 698)
        MainWindow.setStyleSheet(u"background-color: #D1E7FF\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Welcome = QLabel(self.frame)
        self.Welcome.setObjectName(u"Welcome")
        self.Welcome.setMaximumSize(QSize(16777215, 120))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.Welcome.setFont(font)
        self.Welcome.setStyleSheet(u"QLabel {\n"
"    background: qlineargradient(\n"
"        spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,\n"
"        stop:0 #E6E6FA, stop:0.2 #B3E5FC, stop: 0.4 #E6E6FA,\n"
"        stop: 0.6 #B3E5FC, stop: 0.8 #B3E5FC, stop: 1 #E6E6FA\n"
"    );\n"
"}\n"
"")
        self.Welcome.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.Welcome)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(25)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel {\n"
"    background: qlineargradient(\n"
"        spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,\n"
"        stop:0 #E6E6FA, stop:0.2 #B3E5FC, stop: 0.4 #E6E6FA,\n"
"        stop: 0.6 #B3E5FC, stop: 0.8 #B3E5FC, stop: 1 #E6E6FA\n"
"    );\n"
"}\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Items_page = QPushButton(self.frame)
        self.Items_page.setObjectName(u"Items_page")
        self.Items_page.setMinimumSize(QSize(0, 50))
        self.Items_page.setMaximumSize(QSize(16777215, 50))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.Items_page.setFont(font2)
        self.Items_page.setStyleSheet(u"QPushButton {\n"
"    background-color: #E6E6FA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #CCCCFF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D8BFD8;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.Items_page.setCheckable(True)
        self.Items_page.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Items_page)

        self.Heroes_page = QPushButton(self.frame)
        self.Heroes_page.setObjectName(u"Heroes_page")
        self.Heroes_page.setMinimumSize(QSize(0, 50))
        self.Heroes_page.setFont(font2)
        self.Heroes_page.setStyleSheet(u"QPushButton {\n"
"    background-color: #E6E6FA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #CCCCFF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D8BFD8;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.Heroes_page.setCheckable(True)
        self.Heroes_page.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Heroes_page)

        self.Calculator_page = QPushButton(self.frame)
        self.Calculator_page.setObjectName(u"Calculator_page")
        self.Calculator_page.setMinimumSize(QSize(0, 50))
        self.Calculator_page.setFont(font2)
        self.Calculator_page.setStyleSheet(u"QPushButton {\n"
"    background-color: #E6E6FA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #CCCCFF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D8BFD8;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.Calculator_page.setCheckable(True)
        self.Calculator_page.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Calculator_page)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1402, 26))
        self.menuMain_Page = QMenu(self.menubar)
        self.menuMain_Page.setObjectName(u"menuMain_Page")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMain_Page.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Welcome.setText(QCoreApplication.translate("MainWindow", u"WELCOME TO THE MLBB ULTIMATE GUIDE!!!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CLICK THE BUTTONS BELOW TO NAVIGATE AROUND OUR APP", None))
        self.Items_page.setText(QCoreApplication.translate("MainWindow", u"Items Page", None))
        self.Heroes_page.setText(QCoreApplication.translate("MainWindow", u"Heroes Page", None))
        self.Calculator_page.setText(QCoreApplication.translate("MainWindow", u"Win Rate Calculator + Rank Info", None))
        self.menuMain_Page.setTitle(QCoreApplication.translate("MainWindow", u"Main Page", None))
    # retranslateUi

