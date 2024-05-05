# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newpage.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(980, 711)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 161, 711))
        self.widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(117, 58, 175);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(71, 142, 213);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/mlbb.jpg"))
        self.label.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.assa = QPushButton(self.widget)
        self.assa.setObjectName(u"assa")
        icon = QIcon()
        icon.addFile(u":/Assassin_Icon.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.assa.setIcon(icon)
        self.assa.setCheckable(True)

        self.verticalLayout.addWidget(self.assa)

        self.tank = QPushButton(self.widget)
        self.tank.setObjectName(u"tank")
        icon1 = QIcon()
        icon1.addFile(u":/Tank_Icon.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.tank.setIcon(icon1)
        self.tank.setCheckable(True)

        self.verticalLayout.addWidget(self.tank)

        self.fighter = QPushButton(self.widget)
        self.fighter.setObjectName(u"fighter")
        icon2 = QIcon()
        icon2.addFile(u":/Fighter_Icon.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.fighter.setIcon(icon2)
        self.fighter.setCheckable(True)

        self.verticalLayout.addWidget(self.fighter)

        self.mage = QPushButton(self.widget)
        self.mage.setObjectName(u"mage")
        icon3 = QIcon()
        icon3.addFile(u":/Mage_Icon.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.mage.setIcon(icon3)
        self.mage.setCheckable(True)

        self.verticalLayout.addWidget(self.mage)

        self.mm = QPushButton(self.widget)
        self.mm.setObjectName(u"mm")
        icon4 = QIcon()
        icon4.addFile(u":/Marksman_Icon.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.mm.setIcon(icon4)
        self.mm.setCheckable(True)

        self.verticalLayout.addWidget(self.mm)

        self.sup = QPushButton(self.widget)
        self.sup.setObjectName(u"sup")
        icon5 = QIcon()
        icon5.addFile(u":/Support_Icon.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.sup.setIcon(icon5)
        self.sup.setCheckable(True)

        self.verticalLayout.addWidget(self.sup)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 325, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.cls = QPushButton(self.widget)
        self.cls.setObjectName(u"cls")
        self.cls.setCheckable(True)

        self.verticalLayout_2.addWidget(self.cls)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(160, 0, 821, 711))
        self.widget_2.setStyleSheet(u"QWidget{\n"
"background-color: rgb(0, 0, 255);\n"
"}")
        self.stackedWidget = QStackedWidget(self.widget_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(30, 30, 741, 661))
        self.stackedWidget.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.assaspage = QWidget()
        self.assaspage.setObjectName(u"assaspage")
        self.label_3 = QLabel(self.assaspage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 30, 341, 41))
        font = QFont()
        font.setFamilies([u"Sitka Banner Semibold"])
        font.setPointSize(19)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.assaspage)
        self.tankspage = QWidget()
        self.tankspage.setObjectName(u"tankspage")
        self.label_4 = QLabel(self.tankspage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(200, 70, 341, 41))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.tankspage)
        self.fighterspage = QWidget()
        self.fighterspage.setObjectName(u"fighterspage")
        self.label_5 = QLabel(self.fighterspage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(190, 40, 341, 41))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.fighterspage)
        self.magepage = QWidget()
        self.magepage.setObjectName(u"magepage")
        self.label_6 = QLabel(self.magepage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(190, 30, 341, 41))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.magepage)
        self.mmpage = QWidget()
        self.mmpage.setObjectName(u"mmpage")
        self.label_7 = QLabel(self.mmpage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(200, 30, 341, 41))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.mmpage)
        self.supportpage = QWidget()
        self.supportpage.setObjectName(u"supportpage")
        self.label_2 = QLabel(self.supportpage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 30, 341, 41))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.supportpage)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.cls.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.assa.setText(QCoreApplication.translate("MainWindow", u"Assassins", None))
        self.tank.setText(QCoreApplication.translate("MainWindow", u"Tank", None))
        self.fighter.setText(QCoreApplication.translate("MainWindow", u"Fighter", None))
        self.mage.setText(QCoreApplication.translate("MainWindow", u"Mage", None))
        self.mm.setText(QCoreApplication.translate("MainWindow", u"Marksman", None))
        self.sup.setText(QCoreApplication.translate("MainWindow", u"Support", None))
        self.cls.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Assassins", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tanks", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Fighters", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Mage", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Marksman", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Supports", None))
    # retranslateUi

