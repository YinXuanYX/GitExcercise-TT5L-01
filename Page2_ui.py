# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Page2.ui'
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
from PySide6.QtWidgets import (QApplication, QLCDNumber, QLabel, QMainWindow,
    QPlainTextEdit, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(403, 359)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 80, 131, 31))
        font = QFont()
        font.setFamilies([u"MS Serif"])
        font.setPointSize(20)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 140, 131, 31))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 200, 131, 31))
        self.label_3.setFont(font)
        self.GPipt = QPlainTextEdit(self.centralwidget)
        self.GPipt.setObjectName(u"GPipt")
        self.GPipt.setGeometry(QRect(170, 90, 101, 31))
        self.GWipt = QPlainTextEdit(self.centralwidget)
        self.GWipt.setObjectName(u"GWipt")
        self.GWipt.setGeometry(QRect(170, 150, 101, 31))
        self.WRpercentage = QLCDNumber(self.centralwidget)
        self.WRpercentage.setObjectName(u"WRpercentage")
        self.WRpercentage.setGeometry(QRect(170, 210, 64, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Games Played:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Games Won   :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"WinRate        :", None))
    # retranslateUi

