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
        self.stackedWidget.setGeometry(QRect(30, 30, 771, 661))
        self.stackedWidget.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.assaspage = QWidget()
        self.assaspage.setObjectName(u"assaspage")
        self.label_3 = QLabel(self.assaspage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(210, 10, 341, 41))
        font = QFont()
        font.setFamilies([u"Sitka Banner Semibold"])
        font.setPointSize(19)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.Saber = QPushButton(self.assaspage)
        self.Saber.setObjectName(u"Saber")
        self.Saber.setGeometry(QRect(40, 130, 75, 23))
        self.Saber.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Saber.setCheckable(True)
        self.pushButton_2 = QPushButton(self.assaspage)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(170, 130, 75, 23))
        self.pushButton_3 = QPushButton(self.assaspage)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(290, 130, 75, 23))
        self.pushButton_4 = QPushButton(self.assaspage)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(410, 130, 75, 23))
        self.pushButton_5 = QPushButton(self.assaspage)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(530, 130, 75, 23))
        self.pushButton_6 = QPushButton(self.assaspage)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(650, 130, 75, 23))
        self.label_8 = QLabel(self.assaspage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 70, 71, 51))
        self.label_8.setPixmap(QPixmap(u":/Saber.png"))
        self.label_8.setScaledContents(True)
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
        self.saberpage = QWidget()
        self.saberpage.setObjectName(u"saberpage")
        self.widget_3 = QWidget(self.saberpage)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(10, 10, 751, 641))
        self.widget_3.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.label_9 = QLabel(self.widget_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 10, 381, 181))
        self.label_9.setPixmap(QPixmap(u":/Saber.png"))
        self.label_9.setScaledContents(True)
        self.label_11 = QLabel(self.widget_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(80, 220, 111, 21))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setUnderline(True)
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_12 = QLabel(self.widget_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 200, 61, 16))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 220, 47, 51))
        self.label_10.setPixmap(QPixmap(u":/EnemyBane.png"))
        self.label_10.setScaledContents(True)
        self.label_13 = QLabel(self.widget_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(80, 240, 591, 21))
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_14 = QLabel(self.widget_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 280, 51, 16))
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_15 = QLabel(self.widget_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 300, 51, 51))
        self.label_15.setPixmap(QPixmap(u":/Orbiting_Swords.png"))
        self.label_15.setScaledContents(True)
        self.label_16 = QLabel(self.widget_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(90, 290, 111, 16))
        self.label_16.setFont(font1)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_17 = QLabel(self.widget_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(90, 310, 631, 81))
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_17.setWordWrap(True)
        self.label_18 = QLabel(self.widget_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(20, 390, 51, 16))
        self.label_18.setFont(font2)
        self.label_18.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_19 = QLabel(self.widget_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(20, 410, 51, 51))
        self.label_19.setPixmap(QPixmap(u":/Charge.png"))
        self.label_19.setScaledContents(True)
        self.stackedWidget.addWidget(self.saberpage)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.cls.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(6)


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
        self.Saber.setText(QCoreApplication.translate("MainWindow", u"Saber", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_8.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tanks", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Fighters", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Mage", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Marksman", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Supports", None))
        self.label_9.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Enemy's bane", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Passive", None))
        self.label_10.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Saber's attacks reduce enemies' Physical Defense by 3\u20138 for 5 seconds on hit. This effect stacks up to 5 times.", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Skill 1", None))
        self.label_15.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Orbiting Swords", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Saber releases 5 swords that orbit around him and deal 80\u2013105 (+30% Extra Physical Attack) Physical Damage to nearby enemies on hit. The swords will retract back to him after a while.\n"
"When the swords are present, Saber sends a sword toward his target on each attack, dealing 210\u2013260 (+60% Extra Physical Attack) Physical Damage to the target and 50% of the damage to other enemies it passes through (damage against minions is reduced to 50%). Each attack also reduces the cooldown of Charge by 1 second.", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Skill 2", None))
        self.label_19.setText("")
    # retranslateUi

