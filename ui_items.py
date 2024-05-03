# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'items.ui'
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(894, 690)
        MainWindow.setStyleSheet(u"background-color: rgb(219, 239, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(177, 177, 177);\n"
"}\n"
"\n"
"QPushButton{\n"
" color:white;\n"
" height:30px;\n"
" border:none;\n"
" border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
" background-color: #F5FAFE;\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/images/mlbb.jpg"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 20, -1, -1)
        self.physicalicon = QPushButton(self.icon_only_widget)
        self.physicalicon.setObjectName(u"physicalicon")
        icon = QIcon()
        icon.addFile(u":/images/melific.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.physicalicon.setIcon(icon)
        self.physicalicon.setCheckable(True)
        self.physicalicon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.physicalicon)

        self.magicicon = QPushButton(self.icon_only_widget)
        self.magicicon.setObjectName(u"magicicon")
        icon1 = QIcon()
        icon1.addFile(u":/images/glowing_wand.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.magicicon.setIcon(icon1)
        self.magicicon.setCheckable(True)
        self.magicicon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.magicicon)

        self.defenseicon = QPushButton(self.icon_only_widget)
        self.defenseicon.setObjectName(u"defenseicon")
        icon2 = QIcon()
        icon2.addFile(u":/images/blade_armour.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.defenseicon.setIcon(icon2)
        self.defenseicon.setCheckable(True)
        self.defenseicon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.defenseicon)

        self.bootsicon = QPushButton(self.icon_only_widget)
        self.bootsicon.setObjectName(u"bootsicon")
        icon3 = QIcon()
        icon3.addFile(u":/images/movement.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.bootsicon.setIcon(icon3)
        self.bootsicon.setCheckable(True)
        self.bootsicon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.bootsicon)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 336, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.exiticon = QPushButton(self.icon_only_widget)
        self.exiticon.setObjectName(u"exiticon")
        icon4 = QIcon()
        icon4.addFile(u":/images/log_out.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exiticon.setIcon(icon4)
        self.exiticon.setCheckable(True)

        self.verticalLayout_3.addWidget(self.exiticon)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(177, 177, 177);\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton{\n"
" color:white;\n"
" text-align:left;\n"
" height:30px;\n"
" border:none;\n"
" padding-left:10px;\n"
" border-top-left-radius:10px;\n"
" border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
" background-color: #F5FAFE;\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 20, -1)
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/images/mlbb.jpg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_name_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.physicalname = QPushButton(self.icon_name_widget)
        self.physicalname.setObjectName(u"physicalname")
        self.physicalname.setIcon(icon)
        self.physicalname.setCheckable(True)
        self.physicalname.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.physicalname)

        self.magicname = QPushButton(self.icon_name_widget)
        self.magicname.setObjectName(u"magicname")
        self.magicname.setIcon(icon1)
        self.magicname.setCheckable(True)
        self.magicname.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.magicname)

        self.defensename = QPushButton(self.icon_name_widget)
        self.defensename.setObjectName(u"defensename")
        self.defensename.setIcon(icon2)
        self.defensename.setCheckable(True)
        self.defensename.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.defensename)

        self.bootsname = QPushButton(self.icon_name_widget)
        self.bootsname.setObjectName(u"bootsname")
        self.bootsname.setIcon(icon3)
        self.bootsname.setCheckable(True)
        self.bootsname.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.bootsname)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 341, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.exitname = QPushButton(self.icon_name_widget)
        self.exitname.setObjectName(u"exitname")
        self.exitname.setIcon(icon4)
        self.exitname.setCheckable(True)

        self.verticalLayout_4.addWidget(self.exitname)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        font1 = QFont()
        font1.setBold(False)
        self.main_menu.setFont(font1)
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget = QWidget(self.main_menu)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menu = QPushButton(self.widget)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"border:none;")
        icon5 = QIcon()
        icon5.addFile(u":/images/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu.setIcon(icon5)
        self.menu.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.menu)

        self.horizontalSpacer_2 = QSpacerItem(292, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.search = QPushButton(self.widget)
        self.search.setObjectName(u"search")
        icon6 = QIcon()
        icon6.addFile(u":/images/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search.setIcon(icon6)

        self.horizontalLayout.addWidget(self.search)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.stackedWidget.setFont(font2)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.physical_page = QWidget()
        self.physical_page.setObjectName(u"physical_page")
        self.label_4 = QLabel(self.physical_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(170, 160, 331, 91))
        self.label_4.setFont(font2)
        self.stackedWidget.addWidget(self.physical_page)
        self.magic_page = QWidget()
        self.magic_page.setObjectName(u"magic_page")
        self.label_5 = QLabel(self.magic_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(160, 160, 311, 141))
        self.label_5.setFont(font2)
        self.stackedWidget.addWidget(self.magic_page)
        self.defense_page = QWidget()
        self.defense_page.setObjectName(u"defense_page")
        self.label_6 = QLabel(self.defense_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(180, 200, 311, 151))
        self.label_6.setFont(font2)
        self.stackedWidget.addWidget(self.defense_page)
        self.movement_page = QWidget()
        self.movement_page.setObjectName(u"movement_page")
        self.label_7 = QLabel(self.movement_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(140, 180, 331, 171))
        self.label_7.setFont(font2)
        self.stackedWidget.addWidget(self.movement_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu.toggled.connect(self.icon_only_widget.setHidden)
        self.menu.toggled.connect(self.icon_name_widget.setVisible)
        self.bootsicon.toggled.connect(self.bootsname.setChecked)
        self.defenseicon.toggled.connect(self.defensename.setChecked)
        self.magicicon.toggled.connect(self.magicname.setChecked)
        self.physicalicon.toggled.connect(self.physicalname.setChecked)
        self.physicalname.toggled.connect(self.physicalicon.setChecked)
        self.magicname.toggled.connect(self.magicicon.setChecked)
        self.defensename.toggled.connect(self.defenseicon.setChecked)
        self.bootsname.toggled.connect(self.bootsicon.setChecked)
        self.exiticon.toggled.connect(MainWindow.close)
        self.exitname.toggled.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.physicalicon.setText("")
        self.magicicon.setText("")
        self.defenseicon.setText("")
        self.bootsicon.setText("")
        self.exiticon.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ITEMS", None))
        self.physicalname.setText(QCoreApplication.translate("MainWindow", u"PHYSICAL", None))
        self.magicname.setText(QCoreApplication.translate("MainWindow", u"MAGIC", None))
        self.defensename.setText(QCoreApplication.translate("MainWindow", u"DEFENSE", None))
        self.bootsname.setText(QCoreApplication.translate("MainWindow", u"MOVEMENT", None))
        self.exitname.setText(QCoreApplication.translate("MainWindow", u"CLOSE", None))
        self.menu.setText("")
        self.search.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"PHYSICAL ITEMS PAGE", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"MAGIC ITEMS PAGE", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"DEFENSE ITEMS PAGE", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"MOVEMENT ITEMS PAGE", None))
    # retranslateUi

