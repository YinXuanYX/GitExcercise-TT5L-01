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
    QSpacerItem, QSplitter, QStackedWidget, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1426, 829)
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
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 244, 202);\n"
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
        font2.setPointSize(17)
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
        self.WelcomeDescription.setAlignment(Qt.AlignCenter)
        self.WelcomeDescription.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.WelcomeDescription)

        self.splitter = QSplitter(self.Landing_Page)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.bloodyretri_pic = QLabel(self.splitter)
        self.bloodyretri_pic.setObjectName(u"bloodyretri_pic")
        self.bloodyretri_pic.setMinimumSize(QSize(40, 40))
        self.bloodyretri_pic.setPixmap(QPixmap(u":/images/retri.jpg"))
        self.bloodyretri_pic.setScaledContents(False)
        self.bloodyretri_pic.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.bloodyretri_pic)
        self.bladeofkibou_pic = QLabel(self.splitter)
        self.bladeofkibou_pic.setObjectName(u"bladeofkibou_pic")
        self.bladeofkibou_pic.setPixmap(QPixmap(u":/images/blade_of_kibou.jpeg"))
        self.bladeofkibou_pic.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.bladeofkibou_pic)
        self.geniuswand_pic = QLabel(self.splitter)
        self.geniuswand_pic.setObjectName(u"geniuswand_pic")
        self.geniuswand_pic.setMinimumSize(QSize(40, 40))
        self.geniuswand_pic.setPixmap(QPixmap(u":/images/glowing_wand.jpg"))
        self.geniuswand_pic.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.geniuswand_pic)

        self.verticalLayout_10.addWidget(self.splitter)

        self.stackedWidget.addWidget(self.Landing_Page)
        self.physical_page = QWidget()
        self.physical_page.setObjectName(u"physical_page")
        self.verticalLayout_9 = QVBoxLayout(self.physical_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.Physical_pageIntro = QLabel(self.physical_page)
        self.Physical_pageIntro.setObjectName(u"Physical_pageIntro")
        self.Physical_pageIntro.setMaximumSize(QSize(16777215, 120))
        self.Physical_pageIntro.setFont(font1)
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
" background-color: rgb(255, 0, 17);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}")
        self.BOD_button.setCheckable(True)
        self.BOD_button.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.BOD_button)

        self.melefic_button = QPushButton(self.physical_page)
        self.melefic_button.setObjectName(u"melefic_button")
        self.melefic_button.setFont(font4)
        self.melefic_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(255, 0, 17);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}")
        self.melefic_button.setCheckable(True)
        self.melefic_button.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.melefic_button)

        self.GreatDragon_button = QPushButton(self.physical_page)
        self.GreatDragon_button.setObjectName(u"GreatDragon_button")
        self.GreatDragon_button.setFont(font4)
        self.GreatDragon_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(255, 0, 17);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}")
        self.GreatDragon_button.setCheckable(True)
        self.GreatDragon_button.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.GreatDragon_button)

        self.SeaHalbert_button = QPushButton(self.physical_page)
        self.SeaHalbert_button.setObjectName(u"SeaHalbert_button")
        self.SeaHalbert_button.setFont(font4)
        self.SeaHalbert_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(255, 0, 17);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}")
        self.SeaHalbert_button.setCheckable(True)
        self.SeaHalbert_button.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.SeaHalbert_button)

        self.RoseGold_button = QPushButton(self.physical_page)
        self.RoseGold_button.setObjectName(u"RoseGold_button")
        self.RoseGold_button.setFont(font4)
        self.RoseGold_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(255, 0, 17);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}")
        self.RoseGold_button.setCheckable(True)
        self.RoseGold_button.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.RoseGold_button)

        self.Bloodlust_button = QPushButton(self.physical_page)
        self.Bloodlust_button.setObjectName(u"Bloodlust_button")
        self.Bloodlust_button.setFont(font4)
        self.Bloodlust_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(255, 0, 17);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}")
        self.Bloodlust_button.setCheckable(True)
        self.Bloodlust_button.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Bloodlust_button)

        self.Hunter_button = QPushButton(self.physical_page)
        self.Hunter_button.setObjectName(u"Hunter_button")
        self.Hunter_button.setFont(font4)
        self.Hunter_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(255, 0, 17);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}")
        self.Hunter_button.setCheckable(True)
        self.Hunter_button.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Hunter_button)

        self.Heptaseas_button = QPushButton(self.physical_page)
        self.Heptaseas_button.setObjectName(u"Heptaseas_button")
        self.Heptaseas_button.setFont(font4)
        self.Heptaseas_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(255, 0, 17);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}")
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
" background-color: rgb(255, 0, 17);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}")
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
" background-color: rgb(255, 0, 17);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}")
        self.Endless_button.setCheckable(True)
        self.Endless_button.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.Endless_button)

        self.Berserker_button = QPushButton(self.physical_page)
        self.Berserker_button.setObjectName(u"Berserker_button")
        self.Berserker_button.setFont(font4)
        self.Berserker_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(255, 0, 17);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}")
        self.Berserker_button.setCheckable(True)
        self.Berserker_button.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.Berserker_button)

        self.Haas_button = QPushButton(self.physical_page)
        self.Haas_button.setObjectName(u"Haas_button")
        self.Haas_button.setFont(font4)
        self.Haas_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(255, 0, 17);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}")
        self.Haas_button.setCheckable(True)
        self.Haas_button.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.Haas_button)

        self.WarX_button = QPushButton(self.physical_page)
        self.WarX_button.setObjectName(u"WarX_button")
        self.WarX_button.setFont(font4)
        self.WarX_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(255, 0, 17);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}")
        self.WarX_button.setCheckable(True)
        self.WarX_button.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.WarX_button)

        self.WON_button = QPushButton(self.physical_page)
        self.WON_button.setObjectName(u"WON_button")
        self.WON_button.setFont(font4)
        self.WON_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(255, 0, 17);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}")
        self.WON_button.setCheckable(True)
        self.WON_button.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.WON_button)

        self.Golden_button = QPushButton(self.physical_page)
        self.Golden_button.setObjectName(u"Golden_button")
        self.Golden_button.setFont(font4)
        self.Golden_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(255, 0, 17);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}")
        self.Golden_button.setCheckable(True)
        self.Golden_button.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.Golden_button)

        self.Corrosion_button = QPushButton(self.physical_page)
        self.Corrosion_button.setObjectName(u"Corrosion_button")
        self.Corrosion_button.setFont(font4)
        self.Corrosion_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(255, 0, 17);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}")
        self.Corrosion_button.setCheckable(True)
        self.Corrosion_button.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.Corrosion_button)

        self.DHS_button = QPushButton(self.physical_page)
        self.DHS_button.setObjectName(u"DHS_button")
        self.DHS_button.setFont(font4)
        self.DHS_button.setStyleSheet(u"QPushButton:checked{\n"
" background-color: rgb(255, 0, 17);\n"
" color: #1F95EF;\n"
" font-weight:bold;\n"
"}")
        self.DHS_button.setCheckable(True)
        self.DHS_button.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.DHS_button)


        self.horizontalLayout_6.addLayout(self.verticalLayout_7)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.stackedWidget.addWidget(self.physical_page)
        self.magic_page = QWidget()
        self.magic_page.setObjectName(u"magic_page")
        self.label_5 = QLabel(self.magic_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(160, 160, 311, 141))
        self.label_5.setFont(font1)
        self.stackedWidget.addWidget(self.magic_page)
        self.defense_page = QWidget()
        self.defense_page.setObjectName(u"defense_page")
        self.label_6 = QLabel(self.defense_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(180, 200, 311, 151))
        self.label_6.setFont(font1)
        self.stackedWidget.addWidget(self.defense_page)
        self.movement_page = QWidget()
        self.movement_page.setObjectName(u"movement_page")
        self.label_7 = QLabel(self.movement_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(140, 180, 331, 171))
        self.label_7.setFont(font1)
        self.stackedWidget.addWidget(self.movement_page)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_8 = QVBoxLayout(self.page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        font6 = QFont()
        font6.setPointSize(20)
        font6.setBold(True)
        self.label_4.setFont(font6)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_4)

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
        self.ItemName_2.setFont(font4)

        self.verticalLayout_8.addWidget(self.ItemName_2)

        self.ItemAttributes = QLabel(self.page)
        self.ItemAttributes.setObjectName(u"ItemAttributes")
        font8 = QFont()
        font8.setPointSize(12)
        font8.setBold(True)
        self.ItemAttributes.setFont(font8)
        self.ItemAttributes.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.ItemAttributes)

        self.ItemType = QLabel(self.page)
        self.ItemType.setObjectName(u"ItemType")
        self.ItemType.setFont(font8)

        self.verticalLayout_8.addWidget(self.ItemType)

        self.ItemPassive = QLabel(self.page)
        self.ItemPassive.setObjectName(u"ItemPassive")
        font9 = QFont()
        font9.setPointSize(11)
        font9.setBold(False)
        self.ItemPassive.setFont(font9)
        self.ItemPassive.setScaledContents(False)
        self.ItemPassive.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.ItemPassive)

        self.stackedWidget.addWidget(self.page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


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
        self.label_3.setFont(font8)

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
        icon3.addFile(u":/images/melific.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.physicalname.setIcon(icon3)
        self.physicalname.setIconSize(QSize(30, 30))
        self.physicalname.setCheckable(True)
        self.physicalname.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.physicalname)

        self.magicname = QPushButton(self.icon_name_widget)
        self.magicname.setObjectName(u"magicname")
        icon4 = QIcon()
        icon4.addFile(u":/images/glowing_wand.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.magicname.setIcon(icon4)
        self.magicname.setIconSize(QSize(30, 30))
        self.magicname.setCheckable(True)
        self.magicname.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.magicname)

        self.defensename = QPushButton(self.icon_name_widget)
        self.defensename.setObjectName(u"defensename")
        icon5 = QIcon()
        icon5.addFile(u":/images/blade_armour.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.defensename.setIcon(icon5)
        self.defensename.setIconSize(QSize(30, 30))
        self.defensename.setCheckable(True)
        self.defensename.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.defensename)

        self.bootsname = QPushButton(self.icon_name_widget)
        self.bootsname.setObjectName(u"bootsname")
        icon6 = QIcon()
        icon6.addFile(u":/images/movement.jpg", QSize(), QIcon.Normal, QIcon.Off)
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

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu.setText("")
        self.search.setText("")
        self.welcome_text.setText(QCoreApplication.translate("MainWindow", u"WELCOME TO THE ULTIMATE MLBB ITEMS GUIDE", None))
        self.WelcomeDescription.setText(QCoreApplication.translate("MainWindow", u"Are you ready to elevate your Mobile Legends gameplay? Whether you're a seasoned veteran or just starting your journey in the Land of Dawn, mastering the right items can make all the difference between victory and defeat. Our comprehensive items guide is designed to provide you with detailed insights, strategies, and tips to optimize your hero builds and dominate the battlefield. ", None))
        self.bloodyretri_pic.setText("")
        self.bladeofkibou_pic.setText("")
        self.geniuswand_pic.setText("")
        self.Physical_pageIntro.setText(QCoreApplication.translate("MainWindow", u"PHYSICAL ITEMS PAGE", None))
        self.BOD_button.setText(QCoreApplication.translate("MainWindow", u"Blade of Despair", None))
        self.melefic_button.setText(QCoreApplication.translate("MainWindow", u"Melefic Roar", None))
        self.GreatDragon_button.setText(QCoreApplication.translate("MainWindow", u"Great Dragon Spear", None))
        self.SeaHalbert_button.setText(QCoreApplication.translate("MainWindow", u"Sea Halbert", None))
        self.RoseGold_button.setText(QCoreApplication.translate("MainWindow", u"Rose Gold Meteor", None))
        self.Bloodlust_button.setText(QCoreApplication.translate("MainWindow", u"Bloodlust Axe", None))
        self.Hunter_button.setText(QCoreApplication.translate("MainWindow", u"Hunter Strike", None))
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
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"MAGIC ITEMS PAGE", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"DEFENSE ITEMS PAGE", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"MOVEMENT ITEMS PAGE", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"ITEMIMAGE", None))
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

