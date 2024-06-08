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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSplitter,
    QStackedWidget, QVBoxLayout, QWidget)
import resources_items
import resources_items

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1439, 860)
        MainWindow.setStyleSheet(u"\n"
"background-color: rgb(147, 172, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        font = QFont()
        font.setBold(False)
        self.main_menu.setFont(font)
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget = QWidget(self.main_menu)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menu = QPushButton(self.widget)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"border:none;")
        icon = QIcon()
        icon.addFile(u":/images/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu.setIcon(icon)
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
        icon1 = QIcon()
        icon1.addFile(u":/images/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search.setIcon(icon1)

        self.horizontalLayout.addWidget(self.search)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.stackedWidget.setFont(font1)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(207, 207, 207);\n"
"\n"
"")
        self.Landing_Page = QWidget()
        self.Landing_Page.setObjectName(u"Landing_Page")
        self.verticalLayout_10 = QVBoxLayout(self.Landing_Page)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(188, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.welcome_text = QLabel(self.Landing_Page)
        self.welcome_text.setObjectName(u"welcome_text")
        self.welcome_text.setMinimumSize(QSize(120, 120))
        self.welcome_text.setMaximumSize(QSize(1000, 1000))
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.welcome_text.setFont(font2)

        self.horizontalLayout_5.addWidget(self.welcome_text)

        self.horizontalSpacer_3 = QSpacerItem(188, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.WelcomeDescription = QLabel(self.Landing_Page)
        self.WelcomeDescription.setObjectName(u"WelcomeDescription")
        font3 = QFont()
        font3.setPointSize(19)
        font3.setBold(True)
        self.WelcomeDescription.setFont(font3)
        self.WelcomeDescription.setLineWidth(1)
        self.WelcomeDescription.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.WelcomeDescription.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.WelcomeDescription)

        self.splitter = QSplitter(self.Landing_Page)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.label_4 = QLabel(self.splitter)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 350))
        self.label_4.setPixmap(QPixmap(u":/images/images.jpeg"))
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.label_4)
        self.label_5 = QLabel(self.splitter)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u":/images/blade_of_kibou.jpeg"))
        self.label_5.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.label_5)

        self.verticalLayout_10.addWidget(self.splitter)

        self.stackedWidget.addWidget(self.Landing_Page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_21 = QVBoxLayout(self.page_2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.scrollArea = QScrollArea(self.page_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1222, 1222))
        self.verticalLayout_22 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(1200, 1200))
        self.frame.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_22.addWidget(self.frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_21.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.page_2)
        self.physical_page = QWidget()
        self.physical_page.setObjectName(u"physical_page")
        self.verticalLayout_9 = QVBoxLayout(self.physical_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.Physical_pageIntro = QLabel(self.physical_page)
        self.Physical_pageIntro.setObjectName(u"Physical_pageIntro")
        self.Physical_pageIntro.setMaximumSize(QSize(16777215, 120))
        self.Physical_pageIntro.setFont(font3)
        self.Physical_pageIntro.setStyleSheet(u"background-color: rgb(204, 115, 255);")
        self.Physical_pageIntro.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.Physical_pageIntro)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.BOD_button = QPushButton(self.physical_page)
        self.BOD_button.setObjectName(u"BOD_button")
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        self.BOD_button.setFont(font4)
        self.BOD_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.BOD_button.setCheckable(True)
        self.BOD_button.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.BOD_button)

        self.melefic_button = QPushButton(self.physical_page)
        self.melefic_button.setObjectName(u"melefic_button")
        self.melefic_button.setFont(font4)
        self.melefic_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.melefic_button.setCheckable(True)
        self.melefic_button.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.melefic_button)

        self.GreatDragon_button = QPushButton(self.physical_page)
        self.GreatDragon_button.setObjectName(u"GreatDragon_button")
        self.GreatDragon_button.setFont(font4)
        self.GreatDragon_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.GreatDragon_button.setCheckable(True)
        self.GreatDragon_button.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.GreatDragon_button)

        self.SeaHalbert_button = QPushButton(self.physical_page)
        self.SeaHalbert_button.setObjectName(u"SeaHalbert_button")
        self.SeaHalbert_button.setFont(font4)
        self.SeaHalbert_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.SeaHalbert_button.setCheckable(True)
        self.SeaHalbert_button.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.SeaHalbert_button)

        self.Bloodlust_button = QPushButton(self.physical_page)
        self.Bloodlust_button.setObjectName(u"Bloodlust_button")
        self.Bloodlust_button.setFont(font4)
        self.Bloodlust_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.Bloodlust_button.setCheckable(True)
        self.Bloodlust_button.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Bloodlust_button)

        self.Hunter_button = QPushButton(self.physical_page)
        self.Hunter_button.setObjectName(u"Hunter_button")
        self.Hunter_button.setFont(font4)
        self.Hunter_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.Hunter_button.setCheckable(True)
        self.Hunter_button.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Hunter_button)

        self.RoseGold_button = QPushButton(self.physical_page)
        self.RoseGold_button.setObjectName(u"RoseGold_button")
        self.RoseGold_button.setFont(font4)
        self.RoseGold_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.RoseGold_button.setCheckable(True)
        self.RoseGold_button.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.RoseGold_button)

        self.Heptaseas_button = QPushButton(self.physical_page)
        self.Heptaseas_button.setObjectName(u"Heptaseas_button")
        self.Heptaseas_button.setFont(font4)
        self.Heptaseas_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.Heptaseas_button.setCheckable(True)
        self.Heptaseas_button.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Heptaseas_button)

        self.Windtalker_button = QPushButton(self.physical_page)
        self.Windtalker_button.setObjectName(u"Windtalker_button")
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(True)
        font5.setItalic(False)
        self.Windtalker_button.setFont(font5)
        self.Windtalker_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.Windtalker_button.setCheckable(True)
        self.Windtalker_button.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Windtalker_button)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.Endless_button = QPushButton(self.physical_page)
        self.Endless_button.setObjectName(u"Endless_button")
        self.Endless_button.setFont(font4)
        self.Endless_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.Endless_button.setCheckable(True)
        self.Endless_button.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.Endless_button)

        self.Berserker_button = QPushButton(self.physical_page)
        self.Berserker_button.setObjectName(u"Berserker_button")
        self.Berserker_button.setFont(font4)
        self.Berserker_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.Berserker_button.setCheckable(True)
        self.Berserker_button.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.Berserker_button)

        self.Haas_button = QPushButton(self.physical_page)
        self.Haas_button.setObjectName(u"Haas_button")
        self.Haas_button.setFont(font4)
        self.Haas_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.Haas_button.setCheckable(True)
        self.Haas_button.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.Haas_button)

        self.WarX_button = QPushButton(self.physical_page)
        self.WarX_button.setObjectName(u"WarX_button")
        self.WarX_button.setFont(font4)
        self.WarX_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.WarX_button.setCheckable(True)
        self.WarX_button.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.WarX_button)

        self.WON_button = QPushButton(self.physical_page)
        self.WON_button.setObjectName(u"WON_button")
        self.WON_button.setFont(font4)
        self.WON_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.WON_button.setCheckable(True)
        self.WON_button.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.WON_button)

        self.Golden_button = QPushButton(self.physical_page)
        self.Golden_button.setObjectName(u"Golden_button")
        self.Golden_button.setFont(font4)
        self.Golden_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.Golden_button.setCheckable(True)
        self.Golden_button.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.Golden_button)

        self.Corrosion_button = QPushButton(self.physical_page)
        self.Corrosion_button.setObjectName(u"Corrosion_button")
        self.Corrosion_button.setFont(font4)
        self.Corrosion_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.Corrosion_button.setCheckable(True)
        self.Corrosion_button.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.Corrosion_button)

        self.DHS_button = QPushButton(self.physical_page)
        self.DHS_button.setObjectName(u"DHS_button")
        self.DHS_button.setFont(font4)
        self.DHS_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.DHS_button.setCheckable(True)
        self.DHS_button.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.DHS_button)


        self.horizontalLayout_6.addLayout(self.verticalLayout_7)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.stackedWidget.addWidget(self.physical_page)
        self.magic_page = QWidget()
        self.magic_page.setObjectName(u"magic_page")
        self.verticalLayout_13 = QVBoxLayout(self.magic_page)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.MagicItemTitle = QLabel(self.magic_page)
        self.MagicItemTitle.setObjectName(u"MagicItemTitle")
        self.MagicItemTitle.setMaximumSize(QSize(10000, 120))
        self.MagicItemTitle.setFont(font3)
        self.MagicItemTitle.setStyleSheet(u"background-color: rgb(46, 154, 255);")
        self.MagicItemTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.MagicItemTitle)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.Flask_button = QPushButton(self.magic_page)
        self.Flask_button.setObjectName(u"Flask_button")
        self.Flask_button.setFont(font4)
        self.Flask_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.Flask_button.setCheckable(True)
        self.Flask_button.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.Flask_button)

        self.Genius_button = QPushButton(self.magic_page)
        self.Genius_button.setObjectName(u"Genius_button")
        self.Genius_button.setFont(font4)
        self.Genius_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.Genius_button.setCheckable(True)
        self.Genius_button.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.Genius_button)

        self.lightning_button = QPushButton(self.magic_page)
        self.lightning_button.setObjectName(u"lightning_button")
        self.lightning_button.setFont(font4)
        self.lightning_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.lightning_button.setCheckable(True)
        self.lightning_button.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.lightning_button)

        self.fleeting_button = QPushButton(self.magic_page)
        self.fleeting_button.setObjectName(u"fleeting_button")
        self.fleeting_button.setFont(font4)
        self.fleeting_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.fleeting_button.setCheckable(True)
        self.fleeting_button.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.fleeting_button)

        self.BloodWings_button = QPushButton(self.magic_page)
        self.BloodWings_button.setObjectName(u"BloodWings_button")
        self.BloodWings_button.setFont(font4)
        self.BloodWings_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.BloodWings_button.setCheckable(True)
        self.BloodWings_button.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.BloodWings_button)

        self.COD_button = QPushButton(self.magic_page)
        self.COD_button.setObjectName(u"COD_button")
        self.COD_button.setFont(font4)
        self.COD_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.COD_button.setCheckable(True)
        self.COD_button.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.COD_button)

        self.Starlium_button = QPushButton(self.magic_page)
        self.Starlium_button.setObjectName(u"Starlium_button")
        self.Starlium_button.setFont(font4)
        self.Starlium_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.Starlium_button.setCheckable(True)
        self.Starlium_button.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.Starlium_button)


        self.horizontalLayout_7.addLayout(self.verticalLayout_12)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.Glowing_button = QPushButton(self.magic_page)
        self.Glowing_button.setObjectName(u"Glowing_button")
        self.Glowing_button.setFont(font4)
        self.Glowing_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.Glowing_button.setCheckable(True)
        self.Glowing_button.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.Glowing_button)

        self.IceQueenWand_button = QPushButton(self.magic_page)
        self.IceQueenWand_button.setObjectName(u"IceQueenWand_button")
        self.IceQueenWand_button.setFont(font4)
        self.IceQueenWand_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.IceQueenWand_button.setCheckable(True)
        self.IceQueenWand_button.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.IceQueenWand_button)

        self.Concentrated_button = QPushButton(self.magic_page)
        self.Concentrated_button.setObjectName(u"Concentrated_button")
        self.Concentrated_button.setFont(font4)
        self.Concentrated_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.Concentrated_button.setCheckable(True)
        self.Concentrated_button.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.Concentrated_button)

        self.Holy_button = QPushButton(self.magic_page)
        self.Holy_button.setObjectName(u"Holy_button")
        self.Holy_button.setFont(font4)
        self.Holy_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.Holy_button.setCheckable(True)
        self.Holy_button.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.Holy_button)

        self.Divine_button = QPushButton(self.magic_page)
        self.Divine_button.setObjectName(u"Divine_button")
        self.Divine_button.setFont(font4)
        self.Divine_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.Divine_button.setCheckable(True)
        self.Divine_button.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.Divine_button)

        self.NOD_button = QPushButton(self.magic_page)
        self.NOD_button.setObjectName(u"NOD_button")
        self.NOD_button.setFont(font4)
        self.NOD_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.NOD_button.setCheckable(True)
        self.NOD_button.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.NOD_button)

        self.Feather_button = QPushButton(self.magic_page)
        self.Feather_button.setObjectName(u"Feather_button")
        self.Feather_button.setFont(font4)
        self.Feather_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.Feather_button.setCheckable(True)
        self.Feather_button.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.Feather_button)

        self.Winter_button = QPushButton(self.magic_page)
        self.Winter_button.setObjectName(u"Winter_button")
        self.Winter_button.setFont(font4)
        self.Winter_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.Winter_button.setCheckable(True)
        self.Winter_button.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.Winter_button)

        self.Enchanted_button = QPushButton(self.magic_page)
        self.Enchanted_button.setObjectName(u"Enchanted_button")
        self.Enchanted_button.setFont(font4)
        self.Enchanted_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.Enchanted_button.setCheckable(True)
        self.Enchanted_button.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.Enchanted_button)


        self.horizontalLayout_7.addLayout(self.verticalLayout_11)


        self.verticalLayout_13.addLayout(self.horizontalLayout_7)

        self.stackedWidget.addWidget(self.magic_page)
        self.defense_page = QWidget()
        self.defense_page.setObjectName(u"defense_page")
        self.verticalLayout_16 = QVBoxLayout(self.defense_page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_6 = QLabel(self.defense_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(10000, 120))
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"background-color: rgb(158, 158, 158);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.radiant_button = QPushButton(self.defense_page)
        self.radiant_button.setObjectName(u"radiant_button")
        self.radiant_button.setFont(font4)
        self.radiant_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.radiant_button.setCheckable(True)
        self.radiant_button.setAutoExclusive(True)

        self.verticalLayout_14.addWidget(self.radiant_button)

        self.twilight_button = QPushButton(self.defense_page)
        self.twilight_button.setObjectName(u"twilight_button")
        self.twilight_button.setFont(font4)
        self.twilight_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.twilight_button.setCheckable(True)
        self.twilight_button.setAutoExclusive(True)

        self.verticalLayout_14.addWidget(self.twilight_button)

        self.bruteforce_button = QPushButton(self.defense_page)
        self.bruteforce_button.setObjectName(u"bruteforce_button")
        self.bruteforce_button.setFont(font4)
        self.bruteforce_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.bruteforce_button.setCheckable(True)
        self.bruteforce_button.setAutoExclusive(True)

        self.verticalLayout_14.addWidget(self.bruteforce_button)

        self.immo_button = QPushButton(self.defense_page)
        self.immo_button.setObjectName(u"immo_button")
        self.immo_button.setFont(font4)
        self.immo_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.immo_button.setCheckable(True)
        self.immo_button.setAutoExclusive(True)

        self.verticalLayout_14.addWidget(self.immo_button)

        self.dominance_button = QPushButton(self.defense_page)
        self.dominance_button.setObjectName(u"dominance_button")
        self.dominance_button.setFont(font4)
        self.dominance_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.dominance_button.setCheckable(True)
        self.dominance_button.setAutoExclusive(True)

        self.verticalLayout_14.addWidget(self.dominance_button)

        self.athena_button = QPushButton(self.defense_page)
        self.athena_button.setObjectName(u"athena_button")
        self.athena_button.setFont(font4)
        self.athena_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.athena_button.setCheckable(True)
        self.athena_button.setAutoExclusive(True)

        self.verticalLayout_14.addWidget(self.athena_button)


        self.horizontalLayout_8.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.Oracle_button = QPushButton(self.defense_page)
        self.Oracle_button.setObjectName(u"Oracle_button")
        self.Oracle_button.setFont(font4)
        self.Oracle_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.Oracle_button.setCheckable(True)
        self.Oracle_button.setAutoExclusive(True)

        self.verticalLayout_15.addWidget(self.Oracle_button)

        self.antique_button = QPushButton(self.defense_page)
        self.antique_button.setObjectName(u"antique_button")
        self.antique_button.setFont(font4)
        self.antique_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.antique_button.setCheckable(True)
        self.antique_button.setAutoExclusive(True)

        self.verticalLayout_15.addWidget(self.antique_button)

        self.Guardian_button = QPushButton(self.defense_page)
        self.Guardian_button.setObjectName(u"Guardian_button")
        self.Guardian_button.setFont(font4)
        self.Guardian_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.Guardian_button.setCheckable(True)
        self.Guardian_button.setAutoExclusive(True)

        self.verticalLayout_15.addWidget(self.Guardian_button)

        self.cursehelmet_button = QPushButton(self.defense_page)
        self.cursehelmet_button.setObjectName(u"cursehelmet_button")
        self.cursehelmet_button.setFont(font4)
        self.cursehelmet_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.cursehelmet_button.setCheckable(True)
        self.cursehelmet_button.setAutoExclusive(True)

        self.verticalLayout_15.addWidget(self.cursehelmet_button)

        self.thunder_button = QPushButton(self.defense_page)
        self.thunder_button.setObjectName(u"thunder_button")
        self.thunder_button.setFont(font4)
        self.thunder_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.thunder_button.setCheckable(True)
        self.thunder_button.setAutoExclusive(True)

        self.verticalLayout_15.addWidget(self.thunder_button)

        self.queenswings_button = QPushButton(self.defense_page)
        self.queenswings_button.setObjectName(u"queenswings_button")
        self.queenswings_button.setFont(font4)
        self.queenswings_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.queenswings_button.setCheckable(True)
        self.queenswings_button.setAutoExclusive(True)

        self.verticalLayout_15.addWidget(self.queenswings_button)

        self.Bladearmor_button = QPushButton(self.defense_page)
        self.Bladearmor_button.setObjectName(u"Bladearmor_button")
        self.Bladearmor_button.setFont(font4)
        self.Bladearmor_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.Bladearmor_button.setCheckable(True)
        self.Bladearmor_button.setAutoExclusive(True)

        self.verticalLayout_15.addWidget(self.Bladearmor_button)


        self.horizontalLayout_8.addLayout(self.verticalLayout_15)


        self.verticalLayout_16.addLayout(self.horizontalLayout_8)

        self.stackedWidget.addWidget(self.defense_page)
        self.movement_page = QWidget()
        self.movement_page.setObjectName(u"movement_page")
        self.verticalLayout_20 = QVBoxLayout(self.movement_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_7 = QLabel(self.movement_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 120))
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"background-color: rgb(245, 229, 255);")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.demonBoots_button = QPushButton(self.movement_page)
        self.demonBoots_button.setObjectName(u"demonBoots_button")
        self.demonBoots_button.setFont(font4)
        self.demonBoots_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.demonBoots_button.setCheckable(True)
        self.demonBoots_button.setAutoExclusive(True)

        self.verticalLayout_17.addWidget(self.demonBoots_button)

        self.RapidBoots_button = QPushButton(self.movement_page)
        self.RapidBoots_button.setObjectName(u"RapidBoots_button")
        self.RapidBoots_button.setFont(font4)
        self.RapidBoots_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.RapidBoots_button.setCheckable(True)
        self.RapidBoots_button.setAutoExclusive(True)

        self.verticalLayout_17.addWidget(self.RapidBoots_button)

        self.swiftboots_button = QPushButton(self.movement_page)
        self.swiftboots_button.setObjectName(u"swiftboots_button")
        self.swiftboots_button.setFont(font4)
        self.swiftboots_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.swiftboots_button.setCheckable(True)
        self.swiftboots_button.setAutoExclusive(True)

        self.verticalLayout_17.addWidget(self.swiftboots_button)

        self.ArcaneBoots_button = QPushButton(self.movement_page)
        self.ArcaneBoots_button.setObjectName(u"ArcaneBoots_button")
        self.ArcaneBoots_button.setFont(font4)
        self.ArcaneBoots_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.ArcaneBoots_button.setCheckable(True)
        self.ArcaneBoots_button.setAutoExclusive(True)

        self.verticalLayout_17.addWidget(self.ArcaneBoots_button)

        self.MagicBoots_button = QPushButton(self.movement_page)
        self.MagicBoots_button.setObjectName(u"MagicBoots_button")
        self.MagicBoots_button.setFont(font4)
        self.MagicBoots_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.MagicBoots_button.setCheckable(True)
        self.MagicBoots_button.setAutoExclusive(True)

        self.verticalLayout_17.addWidget(self.MagicBoots_button)

        self.ToughBoots_button = QPushButton(self.movement_page)
        self.ToughBoots_button.setObjectName(u"ToughBoots_button")
        self.ToughBoots_button.setFont(font4)
        self.ToughBoots_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.ToughBoots_button.setCheckable(True)
        self.ToughBoots_button.setAutoExclusive(True)

        self.verticalLayout_17.addWidget(self.ToughBoots_button)

        self.WarriorBoots_button = QPushButton(self.movement_page)
        self.WarriorBoots_button.setObjectName(u"WarriorBoots_button")
        self.WarriorBoots_button.setFont(font4)
        self.WarriorBoots_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.WarriorBoots_button.setCheckable(True)
        self.WarriorBoots_button.setAutoExclusive(True)

        self.verticalLayout_17.addWidget(self.WarriorBoots_button)


        self.horizontalLayout_9.addLayout(self.verticalLayout_17)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.FlameRetri_button = QPushButton(self.movement_page)
        self.FlameRetri_button.setObjectName(u"FlameRetri_button")
        self.FlameRetri_button.setFont(font4)
        self.FlameRetri_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.FlameRetri_button.setCheckable(True)
        self.FlameRetri_button.setAutoExclusive(True)

        self.verticalLayout_18.addWidget(self.FlameRetri_button)

        self.IceRetri_button = QPushButton(self.movement_page)
        self.IceRetri_button.setObjectName(u"IceRetri_button")
        self.IceRetri_button.setFont(font4)
        self.IceRetri_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.IceRetri_button.setCheckable(True)
        self.IceRetri_button.setAutoExclusive(True)

        self.verticalLayout_18.addWidget(self.IceRetri_button)

        self.BloodyRetri_button = QPushButton(self.movement_page)
        self.BloodyRetri_button.setObjectName(u"BloodyRetri_button")
        self.BloodyRetri_button.setFont(font4)
        self.BloodyRetri_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.BloodyRetri_button.setCheckable(True)
        self.BloodyRetri_button.setAutoExclusive(True)

        self.verticalLayout_18.addWidget(self.BloodyRetri_button)

        self.Conceal_button = QPushButton(self.movement_page)
        self.Conceal_button.setObjectName(u"Conceal_button")
        self.Conceal_button.setFont(font4)
        self.Conceal_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.Conceal_button.setCheckable(True)
        self.Conceal_button.setAutoExclusive(True)

        self.verticalLayout_18.addWidget(self.Conceal_button)

        self.Encourage_button = QPushButton(self.movement_page)
        self.Encourage_button.setObjectName(u"Encourage_button")
        self.Encourage_button.setFont(font4)
        self.Encourage_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.Encourage_button.setCheckable(True)
        self.Encourage_button.setAutoExclusive(True)

        self.verticalLayout_18.addWidget(self.Encourage_button)

        self.Favour_button = QPushButton(self.movement_page)
        self.Favour_button.setObjectName(u"Favour_button")
        self.Favour_button.setFont(font4)
        self.Favour_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.Favour_button.setCheckable(True)
        self.Favour_button.setAutoExclusive(True)

        self.verticalLayout_18.addWidget(self.Favour_button)

        self.Dire_button = QPushButton(self.movement_page)
        self.Dire_button.setObjectName(u"Dire_button")
        self.Dire_button.setFont(font4)
        self.Dire_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(146, 74, 255);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(206, 121, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(135, 88, 255);\n"
" color:white;\n"
"}\n"
"")
        self.Dire_button.setCheckable(True)
        self.Dire_button.setAutoExclusive(True)

        self.verticalLayout_18.addWidget(self.Dire_button)


        self.horizontalLayout_9.addLayout(self.verticalLayout_18)


        self.verticalLayout_19.addLayout(self.horizontalLayout_9)


        self.verticalLayout_20.addLayout(self.verticalLayout_19)

        self.stackedWidget.addWidget(self.movement_page)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_8 = QVBoxLayout(self.page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.ItemIMG = QLabel(self.page)
        self.ItemIMG.setObjectName(u"ItemIMG")
        font6 = QFont()
        font6.setPointSize(20)
        font6.setBold(True)
        self.ItemIMG.setFont(font6)
        self.ItemIMG.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.ItemIMG)

        self.ItemName = QLabel(self.page)
        self.ItemName.setObjectName(u"ItemName")
        font7 = QFont()
        font7.setPointSize(18)
        font7.setBold(True)
        font7.setItalic(False)
        font7.setUnderline(True)
        self.ItemName.setFont(font7)
        self.ItemName.setLayoutDirection(Qt.LeftToRight)
        self.ItemName.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.ItemName)

        self.ItemName_2 = QLabel(self.page)
        self.ItemName_2.setObjectName(u"ItemName_2")
        self.ItemName_2.setFont(font2)
        self.ItemName_2.setStyleSheet(u"background-color: rgb(210, 255, 206);")

        self.verticalLayout_8.addWidget(self.ItemName_2)

        self.ItemAttributes = QLabel(self.page)
        self.ItemAttributes.setObjectName(u"ItemAttributes")
        font8 = QFont()
        font8.setPointSize(16)
        font8.setBold(True)
        self.ItemAttributes.setFont(font8)
        self.ItemAttributes.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.ItemAttributes.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.ItemAttributes)

        self.ItemType = QLabel(self.page)
        self.ItemType.setObjectName(u"ItemType")
        self.ItemType.setFont(font2)
        self.ItemType.setStyleSheet(u"background-color: rgb(170, 170, 255);")

        self.verticalLayout_8.addWidget(self.ItemType)

        self.ItemPassive = QLabel(self.page)
        self.ItemPassive.setObjectName(u"ItemPassive")
        font9 = QFont()
        font9.setPointSize(16)
        font9.setBold(False)
        self.ItemPassive.setFont(font9)
        self.ItemPassive.setStyleSheet(u"background-color: rgb(160, 128, 255);")
        self.ItemPassive.setScaledContents(False)
        self.ItemPassive.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.ItemPassive.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.ItemPassive)

        self.stackedWidget.addWidget(self.page)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        self.stackedWidget.raise_()
        self.widget.raise_()

        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(106, 166, 255);\n"
"color:white;\n"
"	\n"
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
        font10 = QFont()
        font10.setPointSize(12)
        font10.setBold(True)
        self.label_3.setFont(font10)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.Homename = QPushButton(self.icon_name_widget)
        self.Homename.setObjectName(u"Homename")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Homename.sizePolicy().hasHeightForWidth())
        self.Homename.setSizePolicy(sizePolicy)
        icon2 = QIcon()
        icon2.addFile(u":/images/home_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Homename.setIcon(icon2)
        self.Homename.setIconSize(QSize(30, 30))
        self.Homename.setCheckable(True)
        self.Homename.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Homename)

        self.physicalname = QPushButton(self.icon_name_widget)
        self.physicalname.setObjectName(u"physicalname")
        icon3 = QIcon()
        icon3.addFile(u":/images/Blade_of_Despair.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.physicalname.setIcon(icon3)
        self.physicalname.setIconSize(QSize(30, 30))
        self.physicalname.setCheckable(True)
        self.physicalname.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.physicalname)

        self.magicname = QPushButton(self.icon_name_widget)
        self.magicname.setObjectName(u"magicname")
        icon4 = QIcon()
        icon4.addFile(u":/images/Genius_Wand.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.magicname.setIcon(icon4)
        self.magicname.setIconSize(QSize(30, 30))
        self.magicname.setCheckable(True)
        self.magicname.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.magicname)

        self.defensename = QPushButton(self.icon_name_widget)
        self.defensename.setObjectName(u"defensename")
        icon5 = QIcon()
        icon5.addFile(u":/images/Antique_Cuirass.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.defensename.setIcon(icon5)
        self.defensename.setIconSize(QSize(30, 30))
        self.defensename.setCheckable(True)
        self.defensename.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.defensename)

        self.bootsname = QPushButton(self.icon_name_widget)
        self.bootsname.setObjectName(u"bootsname")
        icon6 = QIcon()
        icon6.addFile(u":/images/Swift_Boots.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.bootsname.setIcon(icon6)
        self.bootsname.setIconSize(QSize(30, 30))
        self.bootsname.setCheckable(True)
        self.bootsname.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.bootsname)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 341, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.exitname = QPushButton(self.icon_name_widget)
        self.exitname.setObjectName(u"exitname")
        icon7 = QIcon()
        icon7.addFile(u":/images/log_out.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exitname.setIcon(icon7)
        self.exitname.setIconSize(QSize(30, 30))
        self.exitname.setCheckable(True)

        self.verticalLayout_4.addWidget(self.exitname)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(106, 166, 255);\n"
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
        self.Homeicon = QPushButton(self.icon_only_widget)
        self.Homeicon.setObjectName(u"Homeicon")
        self.Homeicon.setIcon(icon2)
        self.Homeicon.setIconSize(QSize(30, 30))
        self.Homeicon.setCheckable(True)
        self.Homeicon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Homeicon)

        self.physicalicon = QPushButton(self.icon_only_widget)
        self.physicalicon.setObjectName(u"physicalicon")
        self.physicalicon.setIcon(icon3)
        self.physicalicon.setIconSize(QSize(30, 30))
        self.physicalicon.setCheckable(True)
        self.physicalicon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.physicalicon)

        self.magicicon = QPushButton(self.icon_only_widget)
        self.magicicon.setObjectName(u"magicicon")
        self.magicicon.setIcon(icon4)
        self.magicicon.setIconSize(QSize(30, 30))
        self.magicicon.setCheckable(True)
        self.magicicon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.magicicon)

        self.defenseicon = QPushButton(self.icon_only_widget)
        self.defenseicon.setObjectName(u"defenseicon")
        self.defenseicon.setIcon(icon5)
        self.defenseicon.setIconSize(QSize(30, 30))
        self.defenseicon.setCheckable(True)
        self.defenseicon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.defenseicon)

        self.bootsicon = QPushButton(self.icon_only_widget)
        self.bootsicon.setObjectName(u"bootsicon")
        self.bootsicon.setIcon(icon6)
        self.bootsicon.setIconSize(QSize(30, 30))
        self.bootsicon.setCheckable(True)
        self.bootsicon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.bootsicon)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 336, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.exiticon = QPushButton(self.icon_only_widget)
        self.exiticon.setObjectName(u"exiticon")
        self.exiticon.setIcon(icon7)
        self.exiticon.setIconSize(QSize(30, 30))
        self.exiticon.setCheckable(True)

        self.verticalLayout_3.addWidget(self.exiticon)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
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
        self.menu.toggled.connect(self.icon_only_widget.setHidden)
        self.menu.toggled.connect(self.icon_name_widget.setVisible)

        self.stackedWidget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu.setText("")
        self.search.setText("")
        self.welcome_text.setText(QCoreApplication.translate("MainWindow", u"WELCOME TO THE ULTIMATE MLBB ITEMS GUIDE", None))
        self.WelcomeDescription.setText(QCoreApplication.translate("MainWindow", u"Are you ready to elevate your Mobile Legends gameplay? Whether you're a seasoned veteran or just starting your journey in the Land of Dawn, mastering the right items can make all the difference between victory and defeat. Our comprehensive items guide is designed to provide you with detailed insights, strategies, and tips to optimize your hero builds and dominate the battlefield. ", None))
        self.label_4.setText("")
        self.label_5.setText("")
        self.Physical_pageIntro.setText(QCoreApplication.translate("MainWindow", u"PHYSICAL ITEMS PAGE", None))
        self.BOD_button.setText(QCoreApplication.translate("MainWindow", u"Blade of Despair", None))
        self.melefic_button.setText(QCoreApplication.translate("MainWindow", u"Melefic Roar", None))
        self.GreatDragon_button.setText(QCoreApplication.translate("MainWindow", u"Great Dragon Spear", None))
        self.SeaHalbert_button.setText(QCoreApplication.translate("MainWindow", u"Sea Halbert", None))
        self.Bloodlust_button.setText(QCoreApplication.translate("MainWindow", u"Bloodlust Axe", None))
        self.Hunter_button.setText(QCoreApplication.translate("MainWindow", u"Hunter Strike", None))
        self.RoseGold_button.setText(QCoreApplication.translate("MainWindow", u"Rose Gold Meteor", None))
        self.Heptaseas_button.setText(QCoreApplication.translate("MainWindow", u"Blade of Heptaseas", None))
        self.Windtalker_button.setText(QCoreApplication.translate("MainWindow", u"Windtalker", None))
        self.Endless_button.setText(QCoreApplication.translate("MainWindow", u"Endless Battle", None))
        self.Berserker_button.setText(QCoreApplication.translate("MainWindow", u"Berserker's Fury", None))
        self.Haas_button.setText(QCoreApplication.translate("MainWindow", u"Hass's Claws", None))
        self.WarX_button.setText(QCoreApplication.translate("MainWindow", u"War Axe", None))
        self.WON_button.setText(QCoreApplication.translate("MainWindow", u"Wind of Nature", None))
        self.Golden_button.setText(QCoreApplication.translate("MainWindow", u"Golden Staff", None))
        self.Corrosion_button.setText(QCoreApplication.translate("MainWindow", u"Corrosion Scythe", None))
        self.DHS_button.setText(QCoreApplication.translate("MainWindow", u"Demon Hunter Sword", None))
        self.MagicItemTitle.setText(QCoreApplication.translate("MainWindow", u"MAGIC ITEMS PAGE", None))
        self.Flask_button.setText(QCoreApplication.translate("MainWindow", u"Flask of The Oasis", None))
        self.Genius_button.setText(QCoreApplication.translate("MainWindow", u"Genius Wand", None))
        self.lightning_button.setText(QCoreApplication.translate("MainWindow", u"Lightning Truncheon", None))
        self.fleeting_button.setText(QCoreApplication.translate("MainWindow", u"Fleeting Time", None))
        self.BloodWings_button.setText(QCoreApplication.translate("MainWindow", u"Blood Wings", None))
        self.COD_button.setText(QCoreApplication.translate("MainWindow", u"Clock of Destiny", None))
        self.Starlium_button.setText(QCoreApplication.translate("MainWindow", u"Starlium Scythe", None))
        self.Glowing_button.setText(QCoreApplication.translate("MainWindow", u"Glowing Wand", None))
        self.IceQueenWand_button.setText(QCoreApplication.translate("MainWindow", u"Ice Queen Wand", None))
        self.Concentrated_button.setText(QCoreApplication.translate("MainWindow", u"Concentrated Energy", None))
        self.Holy_button.setText(QCoreApplication.translate("MainWindow", u"Holy Crystal", None))
        self.Divine_button.setText(QCoreApplication.translate("MainWindow", u"Divine Glaive", None))
        self.NOD_button.setText(QCoreApplication.translate("MainWindow", u"Necklace of Durance", None))
        self.Feather_button.setText(QCoreApplication.translate("MainWindow", u"Feather of Heaven", None))
        self.Winter_button.setText(QCoreApplication.translate("MainWindow", u"Winter Truncheon", None))
        self.Enchanted_button.setText(QCoreApplication.translate("MainWindow", u"Enchanted Tailsman", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"DEFENSE ITEMS PAGE", None))
        self.radiant_button.setText(QCoreApplication.translate("MainWindow", u"Radiant Armor", None))
        self.twilight_button.setText(QCoreApplication.translate("MainWindow", u"Twilight Armor", None))
        self.bruteforce_button.setText(QCoreApplication.translate("MainWindow", u"Brute Force Breastplate", None))
        self.immo_button.setText(QCoreApplication.translate("MainWindow", u"Immortality", None))
        self.dominance_button.setText(QCoreApplication.translate("MainWindow", u"Dominance Ice", None))
        self.athena_button.setText(QCoreApplication.translate("MainWindow", u"AthenaSheild", None))
        self.Oracle_button.setText(QCoreApplication.translate("MainWindow", u"Oracle", None))
        self.antique_button.setText(QCoreApplication.translate("MainWindow", u"Antique Cuirass", None))
        self.Guardian_button.setText(QCoreApplication.translate("MainWindow", u"Guardian Helmet", None))
        self.cursehelmet_button.setText(QCoreApplication.translate("MainWindow", u"Cursed Helmet", None))
        self.thunder_button.setText(QCoreApplication.translate("MainWindow", u"Thunder Belt", None))
        self.queenswings_button.setText(QCoreApplication.translate("MainWindow", u"Queen's Wings", None))
        self.Bladearmor_button.setText(QCoreApplication.translate("MainWindow", u"Blade Armor", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"MOVEMENT ITEMS PAGE", None))
        self.demonBoots_button.setText(QCoreApplication.translate("MainWindow", u"Demon Boots", None))
        self.RapidBoots_button.setText(QCoreApplication.translate("MainWindow", u"Rapid Boots", None))
        self.swiftboots_button.setText(QCoreApplication.translate("MainWindow", u"Swift Boots", None))
        self.ArcaneBoots_button.setText(QCoreApplication.translate("MainWindow", u"Arcane Boots", None))
        self.MagicBoots_button.setText(QCoreApplication.translate("MainWindow", u"Magic Boots", None))
        self.ToughBoots_button.setText(QCoreApplication.translate("MainWindow", u"Tough Boots", None))
        self.WarriorBoots_button.setText(QCoreApplication.translate("MainWindow", u"Warrior Boots", None))
        self.FlameRetri_button.setText(QCoreApplication.translate("MainWindow", u"Flame Retribution", None))
        self.IceRetri_button.setText(QCoreApplication.translate("MainWindow", u"Ice Retribution", None))
        self.BloodyRetri_button.setText(QCoreApplication.translate("MainWindow", u"Bloody Retribution", None))
        self.Conceal_button.setText(QCoreApplication.translate("MainWindow", u"Conceal", None))
        self.Encourage_button.setText(QCoreApplication.translate("MainWindow", u"Encourage", None))
        self.Favour_button.setText(QCoreApplication.translate("MainWindow", u"Favour", None))
        self.Dire_button.setText(QCoreApplication.translate("MainWindow", u"DireHit", None))
        self.ItemIMG.setText(QCoreApplication.translate("MainWindow", u"ITEM IMAGE", None))
        self.ItemName.setText(QCoreApplication.translate("MainWindow", u"SUPER_LONG_ITEM_NAME", None))
        self.ItemName_2.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.ItemAttributes.setText(QCoreApplication.translate("MainWindow", u"Attributes", None))
        self.ItemType.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.ItemPassive.setText(QCoreApplication.translate("MainWindow", u" Super_long_item_passive Super_long_item_passive Super_long_item_passive Super_long_item_passive Super_long_item_passive Super_long_item_passive Super_long_item_passiveSuper_long_item_passiveSuper_long_item_passiveSuper_lon Super_long_item_passive Super_long_item_passive Super_long_item_passive Super_long_item_passive Super_long_item_passive Super_long_item_passive Super_long_item_passive Super_long_item_passive g_item_passiveSuper_long_item_passive", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ITEMS", None))
        self.Homename.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.physicalname.setText(QCoreApplication.translate("MainWindow", u"PHYSICAL", None))
        self.magicname.setText(QCoreApplication.translate("MainWindow", u"MAGIC", None))
        self.defensename.setText(QCoreApplication.translate("MainWindow", u"DEFENSE", None))
        self.bootsname.setText(QCoreApplication.translate("MainWindow", u"MOVEMENT", None))
        self.exitname.setText(QCoreApplication.translate("MainWindow", u"CLOSE", None))
        self.label.setText("")
        self.Homeicon.setText("")
        self.physicalicon.setText("")
        self.magicicon.setText("")
        self.defenseicon.setText("")
        self.bootsicon.setText("")
        self.exiticon.setText("")
    # retranslateUi

