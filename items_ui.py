#ui file
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSplitter, QStackedWidget,
    QVBoxLayout, QWidget)
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

        self.horizontalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font1 = QFont()
        font1.setPointSize(19)
        font1.setBold(True)
        self.stackedWidget.setFont(font1)
        self.stackedWidget.setStyleSheet(u"background-color: #D1E7FF\n"
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
        self.WelcomeDescription.setFont(font1)
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
        self.All_page = QWidget()
        self.All_page.setObjectName(u"All_page")
        self.verticalLayout_21 = QVBoxLayout(self.All_page)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.scrollArea = QScrollArea(self.All_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: 1px solid #E0BAFF;\n"
"    background: #FFDFBA;\n"
"    width: 20px;\n"
"    margin: 20px 0 20px 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #BAFFC9;\n"
"    min-height: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #BAE1FF;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background: #E0BAFF;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: 1px solid #E0BAFF;\n"
"    background: #FFB3BA;\n"
"    height: 20px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"    background: #FFDFBA;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {\n"
"    background: #FFFFBA;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: 1px solid #E0BAFF;\n"
"    background: #FFB3BA;\n"
"    height: 20px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBa"
                        "r::sub-line:vertical:hover {\n"
"    background: #FFDFBA;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"    background: #FFFFBA;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    border: 1px solid #E0BAFF;\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    background: #BAFFC9;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:hover, QScrollBar::down-arrow:vertical:hover {\n"
"    background: #BAE1FF;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed, QScrollBar::down-arrow:vertical:pressed {\n"
"    background: #E0BAFF;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: #FFDFBA;\n"
"}\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1151, 2022))
        self.verticalLayout_22 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 2000))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 120))
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"QLabel {\n"
"    background: qlineargradient(\n"
"        spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,\n"
"        stop: 0 #FFB3BA, stop: 0.2 #FFDFBA, stop: 0.4 #FFFFBA,\n"
"        stop: 0.6 #BAFFC9, stop: 0.8 #BAE1FF, stop: 1 #E0BAFF\n"
"    );\n"
"}\n"
"")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.BOD_button_2 = QPushButton(self.frame)
        self.BOD_button_2.setObjectName(u"BOD_button_2")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.BOD_button_2.setFont(font3)
        self.BOD_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/images/Blade_of_Despair.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.BOD_button_2.setIcon(icon1)
        self.BOD_button_2.setIconSize(QSize(40, 40))
        self.BOD_button_2.setCheckable(True)
        self.BOD_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.BOD_button_2)

        self.Endless_button_2 = QPushButton(self.frame)
        self.Endless_button_2.setObjectName(u"Endless_button_2")
        self.Endless_button_2.setFont(font3)
        self.Endless_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/images/Endless_Battle.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.Endless_button_2.setIcon(icon2)
        self.Endless_button_2.setIconSize(QSize(40, 40))
        self.Endless_button_2.setCheckable(True)
        self.Endless_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.Endless_button_2)

        self.SeaHalbert_button_2 = QPushButton(self.frame)
        self.SeaHalbert_button_2.setObjectName(u"SeaHalbert_button_2")
        self.SeaHalbert_button_2.setFont(font3)
        self.SeaHalbert_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/images/Sea_Halberd.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.SeaHalbert_button_2.setIcon(icon3)
        self.SeaHalbert_button_2.setIconSize(QSize(40, 40))
        self.SeaHalbert_button_2.setCheckable(True)
        self.SeaHalbert_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.SeaHalbert_button_2)

        self.Heptaseas_button_2 = QPushButton(self.frame)
        self.Heptaseas_button_2.setObjectName(u"Heptaseas_button_2")
        self.Heptaseas_button_2.setFont(font3)
        self.Heptaseas_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/images/Blade_of_the_Heptaseas.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.Heptaseas_button_2.setIcon(icon4)
        self.Heptaseas_button_2.setIconSize(QSize(40, 40))
        self.Heptaseas_button_2.setCheckable(True)
        self.Heptaseas_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.Heptaseas_button_2)

        self.WON_button_2 = QPushButton(self.frame)
        self.WON_button_2.setObjectName(u"WON_button_2")
        self.WON_button_2.setFont(font3)
        self.WON_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/images/Wind_of_Nature.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.WON_button_2.setIcon(icon5)
        self.WON_button_2.setIconSize(QSize(40, 40))
        self.WON_button_2.setCheckable(True)
        self.WON_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.WON_button_2)

        self.DHS_button_2 = QPushButton(self.frame)
        self.DHS_button_2.setObjectName(u"DHS_button_2")
        self.DHS_button_2.setFont(font3)
        self.DHS_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/images/Demon_Hunter_Sword.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.DHS_button_2.setIcon(icon6)
        self.DHS_button_2.setIconSize(QSize(40, 40))
        self.DHS_button_2.setCheckable(True)
        self.DHS_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.DHS_button_2)

        self.Corrosion_button_2 = QPushButton(self.frame)
        self.Corrosion_button_2.setObjectName(u"Corrosion_button_2")
        self.Corrosion_button_2.setFont(font3)
        self.Corrosion_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/images/Corrosion_Scythe.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.Corrosion_button_2.setIcon(icon7)
        self.Corrosion_button_2.setIconSize(QSize(40, 40))
        self.Corrosion_button_2.setCheckable(True)
        self.Corrosion_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.Corrosion_button_2)

        self.Windtalker_button_2 = QPushButton(self.frame)
        self.Windtalker_button_2.setObjectName(u"Windtalker_button_2")
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setItalic(False)
        self.Windtalker_button_2.setFont(font4)
        self.Windtalker_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/images/Windtalker.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.Windtalker_button_2.setIcon(icon8)
        self.Windtalker_button_2.setIconSize(QSize(40, 40))
        self.Windtalker_button_2.setCheckable(True)
        self.Windtalker_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.Windtalker_button_2)

        self.melefic_button_2 = QPushButton(self.frame)
        self.melefic_button_2.setObjectName(u"melefic_button_2")
        self.melefic_button_2.setFont(font3)
        self.melefic_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/images/Malefic_Roar.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.melefic_button_2.setIcon(icon9)
        self.melefic_button_2.setIconSize(QSize(40, 40))
        self.melefic_button_2.setCheckable(True)
        self.melefic_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.melefic_button_2)

        self.IceQueenWand_button_2 = QPushButton(self.frame)
        self.IceQueenWand_button_2.setObjectName(u"IceQueenWand_button_2")
        self.IceQueenWand_button_2.setFont(font3)
        self.IceQueenWand_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/images/Ice_Queen_Wand.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.IceQueenWand_button_2.setIcon(icon10)
        self.IceQueenWand_button_2.setIconSize(QSize(40, 40))
        self.IceQueenWand_button_2.setCheckable(True)
        self.IceQueenWand_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.IceQueenWand_button_2)

        self.Holy_button_2 = QPushButton(self.frame)
        self.Holy_button_2.setObjectName(u"Holy_button_2")
        self.Holy_button_2.setFont(font3)
        self.Holy_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/images/Holy_Crystal.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.Holy_button_2.setIcon(icon11)
        self.Holy_button_2.setIconSize(QSize(40, 40))
        self.Holy_button_2.setCheckable(True)
        self.Holy_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.Holy_button_2)

        self.Divine_button_2 = QPushButton(self.frame)
        self.Divine_button_2.setObjectName(u"Divine_button_2")
        self.Divine_button_2.setFont(font3)
        self.Divine_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/images/Divine_Glaive.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.Divine_button_2.setIcon(icon12)
        self.Divine_button_2.setIconSize(QSize(40, 40))
        self.Divine_button_2.setCheckable(True)
        self.Divine_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.Divine_button_2)

        self.COD_button_2 = QPushButton(self.frame)
        self.COD_button_2.setObjectName(u"COD_button_2")
        self.COD_button_2.setFont(font3)
        self.COD_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon13 = QIcon()
        icon13.addFile(u":/images/Clock_of_Destiny.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.COD_button_2.setIcon(icon13)
        self.COD_button_2.setIconSize(QSize(40, 40))
        self.COD_button_2.setCheckable(True)
        self.COD_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.COD_button_2)

        self.Genius_button_2 = QPushButton(self.frame)
        self.Genius_button_2.setObjectName(u"Genius_button_2")
        self.Genius_button_2.setFont(font3)
        self.Genius_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon14 = QIcon()
        icon14.addFile(u":/images/Genius_Wand.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.Genius_button_2.setIcon(icon14)
        self.Genius_button_2.setIconSize(QSize(40, 40))
        self.Genius_button_2.setCheckable(True)
        self.Genius_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.Genius_button_2)

        self.Starlium_button_2 = QPushButton(self.frame)
        self.Starlium_button_2.setObjectName(u"Starlium_button_2")
        self.Starlium_button_2.setFont(font3)
        self.Starlium_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon15 = QIcon()
        icon15.addFile(u":/images/Starlium_Scythe.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.Starlium_button_2.setIcon(icon15)
        self.Starlium_button_2.setIconSize(QSize(40, 40))
        self.Starlium_button_2.setCheckable(True)
        self.Starlium_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.Starlium_button_2)

        self.Oracle_button_2 = QPushButton(self.frame)
        self.Oracle_button_2.setObjectName(u"Oracle_button_2")
        self.Oracle_button_2.setFont(font3)
        self.Oracle_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon16 = QIcon()
        icon16.addFile(u":/images/Oracle.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.Oracle_button_2.setIcon(icon16)
        self.Oracle_button_2.setIconSize(QSize(40, 40))
        self.Oracle_button_2.setCheckable(True)
        self.Oracle_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.Oracle_button_2)

        self.radiant_button_2 = QPushButton(self.frame)
        self.radiant_button_2.setObjectName(u"radiant_button_2")
        self.radiant_button_2.setFont(font3)
        self.radiant_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon17 = QIcon()
        icon17.addFile(u":/images/Radiant_Armor.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.radiant_button_2.setIcon(icon17)
        self.radiant_button_2.setIconSize(QSize(40, 40))
        self.radiant_button_2.setCheckable(True)
        self.radiant_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.radiant_button_2)

        self.queenswings_button_2 = QPushButton(self.frame)
        self.queenswings_button_2.setObjectName(u"queenswings_button_2")
        self.queenswings_button_2.setFont(font3)
        self.queenswings_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon18 = QIcon()
        icon18.addFile(u":/images/Queen%27s_Wings.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.queenswings_button_2.setIcon(icon18)
        self.queenswings_button_2.setIconSize(QSize(40, 40))
        self.queenswings_button_2.setCheckable(True)
        self.queenswings_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.queenswings_button_2)

        self.dominance_button_2 = QPushButton(self.frame)
        self.dominance_button_2.setObjectName(u"dominance_button_2")
        self.dominance_button_2.setFont(font3)
        self.dominance_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon19 = QIcon()
        icon19.addFile(u":/images/Dominance_Ice.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.dominance_button_2.setIcon(icon19)
        self.dominance_button_2.setIconSize(QSize(40, 40))
        self.dominance_button_2.setCheckable(True)
        self.dominance_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.dominance_button_2)

        self.thunder_button_2 = QPushButton(self.frame)
        self.thunder_button_2.setObjectName(u"thunder_button_2")
        self.thunder_button_2.setFont(font3)
        self.thunder_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon20 = QIcon()
        icon20.addFile(u":/images/Thunder_Belt.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.thunder_button_2.setIcon(icon20)
        self.thunder_button_2.setIconSize(QSize(40, 40))
        self.thunder_button_2.setCheckable(True)
        self.thunder_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.thunder_button_2)

        self.athena_button_2 = QPushButton(self.frame)
        self.athena_button_2.setObjectName(u"athena_button_2")
        self.athena_button_2.setFont(font3)
        self.athena_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon21 = QIcon()
        icon21.addFile(u":/images/Athena%27s_Shield.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.athena_button_2.setIcon(icon21)
        self.athena_button_2.setIconSize(QSize(40, 40))
        self.athena_button_2.setCheckable(True)
        self.athena_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.athena_button_2)

        self.Bladearmor_button_2 = QPushButton(self.frame)
        self.Bladearmor_button_2.setObjectName(u"Bladearmor_button_2")
        self.Bladearmor_button_2.setFont(font3)
        self.Bladearmor_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon22 = QIcon()
        icon22.addFile(u":/images/Blade_Armor.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.Bladearmor_button_2.setIcon(icon22)
        self.Bladearmor_button_2.setIconSize(QSize(40, 40))
        self.Bladearmor_button_2.setCheckable(True)
        self.Bladearmor_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.Bladearmor_button_2)

        self.demonBoots_button_2 = QPushButton(self.frame)
        self.demonBoots_button_2.setObjectName(u"demonBoots_button_2")
        self.demonBoots_button_2.setFont(font3)
        self.demonBoots_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon23 = QIcon()
        icon23.addFile(u":/images/Demon_Shoes.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.demonBoots_button_2.setIcon(icon23)
        self.demonBoots_button_2.setIconSize(QSize(40, 40))
        self.demonBoots_button_2.setCheckable(True)
        self.demonBoots_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.demonBoots_button_2)

        self.RapidBoots_button_2 = QPushButton(self.frame)
        self.RapidBoots_button_2.setObjectName(u"RapidBoots_button_2")
        self.RapidBoots_button_2.setFont(font3)
        self.RapidBoots_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon24 = QIcon()
        icon24.addFile(u":/images/Rapid_Boots.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.RapidBoots_button_2.setIcon(icon24)
        self.RapidBoots_button_2.setIconSize(QSize(40, 40))
        self.RapidBoots_button_2.setCheckable(True)
        self.RapidBoots_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.RapidBoots_button_2)

        self.FlameRetri_button_2 = QPushButton(self.frame)
        self.FlameRetri_button_2.setObjectName(u"FlameRetri_button_2")
        self.FlameRetri_button_2.setFont(font3)
        self.FlameRetri_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon25 = QIcon()
        icon25.addFile(u":/images/Flame_Retribution.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.FlameRetri_button_2.setIcon(icon25)
        self.FlameRetri_button_2.setIconSize(QSize(40, 40))
        self.FlameRetri_button_2.setCheckable(True)
        self.FlameRetri_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.FlameRetri_button_2)

        self.IceRetri_button_2 = QPushButton(self.frame)
        self.IceRetri_button_2.setObjectName(u"IceRetri_button_2")
        self.IceRetri_button_2.setFont(font3)
        self.IceRetri_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon26 = QIcon()
        icon26.addFile(u":/images/Ice_Retribution.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.IceRetri_button_2.setIcon(icon26)
        self.IceRetri_button_2.setIconSize(QSize(40, 40))
        self.IceRetri_button_2.setCheckable(True)
        self.IceRetri_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.IceRetri_button_2)

        self.BloodyRetri_button_2 = QPushButton(self.frame)
        self.BloodyRetri_button_2.setObjectName(u"BloodyRetri_button_2")
        self.BloodyRetri_button_2.setFont(font3)
        self.BloodyRetri_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon27 = QIcon()
        icon27.addFile(u":/images/Bloody_Retribution.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.BloodyRetri_button_2.setIcon(icon27)
        self.BloodyRetri_button_2.setIconSize(QSize(40, 40))
        self.BloodyRetri_button_2.setCheckable(True)
        self.BloodyRetri_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.BloodyRetri_button_2)

        self.ToughBoots_button_2 = QPushButton(self.frame)
        self.ToughBoots_button_2.setObjectName(u"ToughBoots_button_2")
        self.ToughBoots_button_2.setFont(font3)
        self.ToughBoots_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon28 = QIcon()
        icon28.addFile(u":/images/Tough_Boots.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.ToughBoots_button_2.setIcon(icon28)
        self.ToughBoots_button_2.setIconSize(QSize(40, 40))
        self.ToughBoots_button_2.setCheckable(True)
        self.ToughBoots_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.ToughBoots_button_2)

        self.WarriorBoots_button_2 = QPushButton(self.frame)
        self.WarriorBoots_button_2.setObjectName(u"WarriorBoots_button_2")
        self.WarriorBoots_button_2.setFont(font3)
        self.WarriorBoots_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon29 = QIcon()
        icon29.addFile(u":/images/Warrior_Boots.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.WarriorBoots_button_2.setIcon(icon29)
        self.WarriorBoots_button_2.setIconSize(QSize(40, 40))
        self.WarriorBoots_button_2.setCheckable(True)
        self.WarriorBoots_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.WarriorBoots_button_2)

        self.MagicBoots_button_2 = QPushButton(self.frame)
        self.MagicBoots_button_2.setObjectName(u"MagicBoots_button_2")
        self.MagicBoots_button_2.setFont(font3)
        self.MagicBoots_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon30 = QIcon()
        icon30.addFile(u":/images/Magic_Shoes.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.MagicBoots_button_2.setIcon(icon30)
        self.MagicBoots_button_2.setIconSize(QSize(40, 40))
        self.MagicBoots_button_2.setCheckable(True)
        self.MagicBoots_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.MagicBoots_button_2)

        self.ArcaneBoots_button_2 = QPushButton(self.frame)
        self.ArcaneBoots_button_2.setObjectName(u"ArcaneBoots_button_2")
        self.ArcaneBoots_button_2.setFont(font3)
        self.ArcaneBoots_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon31 = QIcon()
        icon31.addFile(u":/images/Arcane_Boots.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.ArcaneBoots_button_2.setIcon(icon31)
        self.ArcaneBoots_button_2.setIconSize(QSize(40, 40))
        self.ArcaneBoots_button_2.setCheckable(True)
        self.ArcaneBoots_button_2.setAutoExclusive(True)

        self.verticalLayout_23.addWidget(self.ArcaneBoots_button_2)


        self.horizontalLayout_10.addLayout(self.verticalLayout_23)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.Berserker_button_2 = QPushButton(self.frame)
        self.Berserker_button_2.setObjectName(u"Berserker_button_2")
        self.Berserker_button_2.setFont(font3)
        self.Berserker_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon32 = QIcon()
        icon32.addFile(u":/images/Berserker%27s_Fury.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.Berserker_button_2.setIcon(icon32)
        self.Berserker_button_2.setIconSize(QSize(40, 40))
        self.Berserker_button_2.setCheckable(True)
        self.Berserker_button_2.setAutoExclusive(True)

        self.verticalLayout_24.addWidget(self.Berserker_button_2)

        self.Haas_button_2 = QPushButton(self.frame)
        self.Haas_button_2.setObjectName(u"Haas_button_2")
        self.Haas_button_2.setFont(font3)
        self.Haas_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon33 = QIcon()
        icon33.addFile(u":/images/Haas%27s_Claws.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.Haas_button_2.setIcon(icon33)
        self.Haas_button_2.setIconSize(QSize(40, 40))
        self.Haas_button_2.setCheckable(True)
        self.Haas_button_2.setAutoExclusive(True)

        self.verticalLayout_24.addWidget(self.Haas_button_2)

        self.WarX_button_2 = QPushButton(self.frame)
        self.WarX_button_2.setObjectName(u"WarX_button_2")
        self.WarX_button_2.setFont(font3)
        self.WarX_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon34 = QIcon()
        icon34.addFile(u":/images/War_Axe.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.WarX_button_2.setIcon(icon34)
        self.WarX_button_2.setIconSize(QSize(40, 40))
        self.WarX_button_2.setCheckable(True)
        self.WarX_button_2.setAutoExclusive(True)

        self.verticalLayout_24.addWidget(self.WarX_button_2)

        self.Hunter_button_2 = QPushButton(self.frame)
        self.Hunter_button_2.setObjectName(u"Hunter_button_2")
        self.Hunter_button_2.setFont(font3)
        self.Hunter_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon35 = QIcon()
        icon35.addFile(u":/images/Hunter_Strike.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.Hunter_button_2.setIcon(icon35)
        self.Hunter_button_2.setIconSize(QSize(40, 40))
        self.Hunter_button_2.setCheckable(True)
        self.Hunter_button_2.setAutoExclusive(True)

        self.verticalLayout_24.addWidget(self.Hunter_button_2)

        self.Golden_button_2 = QPushButton(self.frame)
        self.Golden_button_2.setObjectName(u"Golden_button_2")
        self.Golden_button_2.setFont(font3)
        self.Golden_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon36 = QIcon()
        icon36.addFile(u":/images/Golden_Staff.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.Golden_button_2.setIcon(icon36)
        self.Golden_button_2.setIconSize(QSize(40, 40))
        self.Golden_button_2.setCheckable(True)
        self.Golden_button_2.setAutoExclusive(True)

        self.verticalLayout_24.addWidget(self.Golden_button_2)

        self.RoseGold_button_2 = QPushButton(self.frame)
        self.RoseGold_button_2.setObjectName(u"RoseGold_button_2")
        self.RoseGold_button_2.setFont(font3)
        self.RoseGold_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon37 = QIcon()
        icon37.addFile(u":/images/Rose_Gold_Meteor.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.RoseGold_button_2.setIcon(icon37)
        self.RoseGold_button_2.setIconSize(QSize(40, 40))
        self.RoseGold_button_2.setCheckable(True)
        self.RoseGold_button_2.setAutoExclusive(True)

        self.verticalLayout_24.addWidget(self.RoseGold_button_2)

        self.Bloodlust_button_2 = QPushButton(self.frame)
        self.Bloodlust_button_2.setObjectName(u"Bloodlust_button_2")
        self.Bloodlust_button_2.setFont(font3)
        self.Bloodlust_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon38 = QIcon()
        icon38.addFile(u":/images/Bloodlust_Axe.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.Bloodlust_button_2.setIcon(icon38)
        self.Bloodlust_button_2.setIconSize(QSize(40, 40))
        self.Bloodlust_button_2.setCheckable(True)
        self.Bloodlust_button_2.setAutoExclusive(True)

        self.verticalLayout_24.addWidget(self.Bloodlust_button_2)

        self.GreatDragon_button_2 = QPushButton(self.frame)
        self.GreatDragon_button_2.setObjectName(u"GreatDragon_button_2")
        self.GreatDragon_button_2.setFont(font3)
        self.GreatDragon_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon39 = QIcon()
        icon39.addFile(u":/images/Great_Dragon_Spear.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.GreatDragon_button_2.setIcon(icon39)
        self.GreatDragon_button_2.setIconSize(QSize(40, 40))
        self.GreatDragon_button_2.setCheckable(True)
        self.GreatDragon_button_2.setAutoExclusive(True)

        self.verticalLayout_24.addWidget(self.GreatDragon_button_2)

        self.Flask_button_2 = QPushButton(self.frame)
        self.Flask_button_2.setObjectName(u"Flask_button_2")
        self.Flask_button_2.setFont(font3)
        self.Flask_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon40 = QIcon()
        icon40.addFile(u":/images/Flask_of_the_Oasis.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.Flask_button_2.setIcon(icon40)
        self.Flask_button_2.setIconSize(QSize(40, 40))
        self.Flask_button_2.setCheckable(True)
        self.Flask_button_2.setAutoExclusive(True)

        self.verticalLayout_24.addWidget(self.Flask_button_2)

        self.Concentrated_button_2 = QPushButton(self.frame)
        self.Concentrated_button_2.setObjectName(u"Concentrated_button_2")
        self.Concentrated_button_2.setFont(font3)
        self.Concentrated_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon41 = QIcon()
        icon41.addFile(u":/images/Concentrated_Energy.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.Concentrated_button_2.setIcon(icon41)
        self.Concentrated_button_2.setIconSize(QSize(40, 40))
        self.Concentrated_button_2.setCheckable(True)
        self.Concentrated_button_2.setAutoExclusive(True)

        self.verticalLayout_24.addWidget(self.Concentrated_button_2)

        self.lightning_button_2 = QPushButton(self.frame)
        self.lightning_button_2.setObjectName(u"lightning_button_2")
        self.lightning_button_2.setFont(font3)
        self.lightning_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon42 = QIcon()
        icon42.addFile(u":/images/Lightning_Truncheon.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.lightning_button_2.setIcon(icon42)
        self.lightning_button_2.setIconSize(QSize(40, 40))
        self.lightning_button_2.setCheckable(True)
        self.lightning_button_2.setAutoExclusive(True)

        self.verticalLayout_24.addWidget(self.lightning_button_2)

        self.fleeting_button_2 = QPushButton(self.frame)
        self.fleeting_button_2.setObjectName(u"fleeting_button_2")
        self.fleeting_button_2.setFont(font3)
        self.fleeting_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon43 = QIcon()
        icon43.addFile(u":/images/Fleeting_Time.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.fleeting_button_2.setIcon(icon43)
        self.fleeting_button_2.setIconSize(QSize(40, 40))
        self.fleeting_button_2.setCheckable(True)
        self.fleeting_button_2.setAutoExclusive(True)

        self.verticalLayout_24.addWidget(self.fleeting_button_2)

        self.BloodWings_button_2 = QPushButton(self.frame)
        self.BloodWings_button_2.setObjectName(u"BloodWings_button_2")
        self.BloodWings_button_2.setFont(font3)
        self.BloodWings_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon44 = QIcon()
        icon44.addFile(u":/images/Blood_Wings.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.BloodWings_button_2.setIcon(icon44)
        self.BloodWings_button_2.setIconSize(QSize(40, 40))
        self.BloodWings_button_2.setCheckable(True)
        self.BloodWings_button_2.setAutoExclusive(True)

        self.verticalLayout_24.addWidget(self.BloodWings_button_2)

        self.NOD_button_2 = QPushButton(self.frame)
        self.NOD_button_2.setObjectName(u"NOD_button_2")
        self.NOD_button_2.setFont(font3)
        self.NOD_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon45 = QIcon()
        icon45.addFile(u":/images/Necklace_of_Durance.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.NOD_button_2.setIcon(icon45)
        self.NOD_button_2.setIconSize(QSize(40, 40))
        self.NOD_button_2.setCheckable(True)
        self.NOD_button_2.setAutoExclusive(True)

        self.verticalLayout_24.addWidget(self.NOD_button_2)

        self.Feather_button_2 = QPushButton(self.frame)
        self.Feather_button_2.setObjectName(u"Feather_button_2")
        self.Feather_button_2.setFont(font3)
        self.Feather_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon46 = QIcon()
        icon46.addFile(u":/images/Feather_of_Heaven.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.Feather_button_2.setIcon(icon46)
        self.Feather_button_2.setIconSize(QSize(40, 40))
        self.Feather_button_2.setCheckable(True)
        self.Feather_button_2.setAutoExclusive(True)

        self.verticalLayout_24.addWidget(self.Feather_button_2)

        self.Glowing_button_2 = QPushButton(self.frame)
        self.Glowing_button_2.setObjectName(u"Glowing_button_2")
        self.Glowing_button_2.setFont(font3)
        self.Glowing_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon47 = QIcon()
        icon47.addFile(u":/images/Glowing_Wand.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.Glowing_button_2.setIcon(icon47)
        self.Glowing_button_2.setIconSize(QSize(40, 40))
        self.Glowing_button_2.setCheckable(True)
        self.Glowing_button_2.setAutoExclusive(True)

        self.verticalLayout_24.addWidget(self.Glowing_button_2)

        self.Winter_button_2 = QPushButton(self.frame)
        self.Winter_button_2.setObjectName(u"Winter_button_2")
        self.Winter_button_2.setFont(font3)
        self.Winter_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon48 = QIcon()
        icon48.addFile(u":/images/Winter_Truncheon.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.Winter_button_2.setIcon(icon48)
        self.Winter_button_2.setIconSize(QSize(40, 40))
        self.Winter_button_2.setCheckable(True)
        self.Winter_button_2.setAutoExclusive(True)

        self.verticalLayout_24.addWidget(self.Winter_button_2)

        self.Enchanted_button_2 = QPushButton(self.frame)
        self.Enchanted_button_2.setObjectName(u"Enchanted_button_2")
        self.Enchanted_button_2.setFont(font3)
        self.Enchanted_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon49 = QIcon()
        icon49.addFile(u":/images/Enchanted_Talisman.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.Enchanted_button_2.setIcon(icon49)
        self.Enchanted_button_2.setIconSize(QSize(40, 40))
        self.Enchanted_button_2.setCheckable(True)
        self.Enchanted_button_2.setAutoExclusive(True)

        self.verticalLayout_24.addWidget(self.Enchanted_button_2)

        self.antique_button_2 = QPushButton(self.frame)
        self.antique_button_2.setObjectName(u"antique_button_2")
        self.antique_button_2.setFont(font3)
        self.antique_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon50 = QIcon()
        icon50.addFile(u":/images/Antique_Cuirass.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.antique_button_2.setIcon(icon50)
        self.antique_button_2.setIconSize(QSize(40, 40))
        self.antique_button_2.setCheckable(True)
        self.antique_button_2.setAutoExclusive(True)

        self.verticalLayout_24.addWidget(self.antique_button_2)

        self.Guardian_button_2 = QPushButton(self.frame)
        self.Guardian_button_2.setObjectName(u"Guardian_button_2")
        self.Guardian_button_2.setFont(font3)
        self.Guardian_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon51 = QIcon()
        icon51.addFile(u":/images/Guardian_Helmet.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.Guardian_button_2.setIcon(icon51)
        self.Guardian_button_2.setIconSize(QSize(40, 40))
        self.Guardian_button_2.setCheckable(True)
        self.Guardian_button_2.setAutoExclusive(True)

        self.verticalLayout_24.addWidget(self.Guardian_button_2)

        self.twilight_button_2 = QPushButton(self.frame)
        self.twilight_button_2.setObjectName(u"twilight_button_2")
        self.twilight_button_2.setFont(font3)
        self.twilight_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon52 = QIcon()
        icon52.addFile(u":/images/Twilight_Armor.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.twilight_button_2.setIcon(icon52)
        self.twilight_button_2.setIconSize(QSize(40, 40))
        self.twilight_button_2.setCheckable(True)
        self.twilight_button_2.setAutoExclusive(True)

        self.verticalLayout_24.addWidget(self.twilight_button_2)

        self.cursehelmet_button_2 = QPushButton(self.frame)
        self.cursehelmet_button_2.setObjectName(u"cursehelmet_button_2")
        self.cursehelmet_button_2.setFont(font3)
        self.cursehelmet_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon53 = QIcon()
        icon53.addFile(u":/images/Cursed_Helmet.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.cursehelmet_button_2.setIcon(icon53)
        self.cursehelmet_button_2.setIconSize(QSize(40, 40))
        self.cursehelmet_button_2.setCheckable(True)
        self.cursehelmet_button_2.setAutoExclusive(True)

        self.verticalLayout_24.addWidget(self.cursehelmet_button_2)

        self.immo_button_2 = QPushButton(self.frame)
        self.immo_button_2.setObjectName(u"immo_button_2")
        self.immo_button_2.setFont(font3)
        self.immo_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon54 = QIcon()
        icon54.addFile(u":/images/Immortality.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.immo_button_2.setIcon(icon54)
        self.immo_button_2.setIconSize(QSize(40, 40))
        self.immo_button_2.setCheckable(True)
        self.immo_button_2.setAutoExclusive(True)

        self.verticalLayout_24.addWidget(self.immo_button_2)

        self.bruteforce_button_2 = QPushButton(self.frame)
        self.bruteforce_button_2.setObjectName(u"bruteforce_button_2")
        self.bruteforce_button_2.setFont(font3)
        self.bruteforce_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon55 = QIcon()
        icon55.addFile(u":/images/Brute_Force_Breastplate.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.bruteforce_button_2.setIcon(icon55)
        self.bruteforce_button_2.setIconSize(QSize(40, 40))
        self.bruteforce_button_2.setCheckable(True)
        self.bruteforce_button_2.setAutoExclusive(True)

        self.verticalLayout_24.addWidget(self.bruteforce_button_2)

        self.swiftboots_button_2 = QPushButton(self.frame)
        self.swiftboots_button_2.setObjectName(u"swiftboots_button_2")
        self.swiftboots_button_2.setFont(font3)
        self.swiftboots_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon56 = QIcon()
        icon56.addFile(u":/images/Swift_Boots.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.swiftboots_button_2.setIcon(icon56)
        self.swiftboots_button_2.setIconSize(QSize(40, 40))
        self.swiftboots_button_2.setCheckable(True)
        self.swiftboots_button_2.setAutoExclusive(True)

        self.verticalLayout_24.addWidget(self.swiftboots_button_2)

        self.Conceal_button_2 = QPushButton(self.frame)
        self.Conceal_button_2.setObjectName(u"Conceal_button_2")
        self.Conceal_button_2.setFont(font3)
        self.Conceal_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon57 = QIcon()
        icon57.addFile(u":/images/Active_-_Conceal.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.Conceal_button_2.setIcon(icon57)
        self.Conceal_button_2.setIconSize(QSize(40, 40))
        self.Conceal_button_2.setCheckable(True)
        self.Conceal_button_2.setAutoExclusive(True)

        self.verticalLayout_24.addWidget(self.Conceal_button_2)

        self.Encourage_button_2 = QPushButton(self.frame)
        self.Encourage_button_2.setObjectName(u"Encourage_button_2")
        self.Encourage_button_2.setFont(font3)
        self.Encourage_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon58 = QIcon()
        icon58.addFile(u":/images/Passive_-_Encourage.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.Encourage_button_2.setIcon(icon58)
        self.Encourage_button_2.setIconSize(QSize(40, 40))
        self.Encourage_button_2.setCheckable(True)
        self.Encourage_button_2.setAutoExclusive(True)

        self.verticalLayout_24.addWidget(self.Encourage_button_2)

        self.Favour_button_2 = QPushButton(self.frame)
        self.Favour_button_2.setObjectName(u"Favour_button_2")
        self.Favour_button_2.setFont(font3)
        self.Favour_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon59 = QIcon()
        icon59.addFile(u":/images/Passive_-_Favor.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.Favour_button_2.setIcon(icon59)
        self.Favour_button_2.setIconSize(QSize(40, 40))
        self.Favour_button_2.setCheckable(True)
        self.Favour_button_2.setAutoExclusive(True)

        self.verticalLayout_24.addWidget(self.Favour_button_2)

        self.Dire_button_2 = QPushButton(self.frame)
        self.Dire_button_2.setObjectName(u"Dire_button_2")
        self.Dire_button_2.setFont(font3)
        self.Dire_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFDFBA;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BAE1FF;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0BAFF;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"\n"
"\n"
"")
        icon60 = QIcon()
        icon60.addFile(u":/images/Passive_-_Dire_Hit.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.Dire_button_2.setIcon(icon60)
        self.Dire_button_2.setIconSize(QSize(40, 40))
        self.Dire_button_2.setCheckable(True)
        self.Dire_button_2.setAutoExclusive(True)

        self.verticalLayout_24.addWidget(self.Dire_button_2)


        self.horizontalLayout_10.addLayout(self.verticalLayout_24)


        self.verticalLayout_25.addLayout(self.horizontalLayout_10)


        self.verticalLayout_22.addWidget(self.frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_21.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.All_page)
        self.physical_page = QWidget()
        self.physical_page.setObjectName(u"physical_page")
        self.verticalLayout_9 = QVBoxLayout(self.physical_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.Physical_pageIntro = QLabel(self.physical_page)
        self.Physical_pageIntro.setObjectName(u"Physical_pageIntro")
        self.Physical_pageIntro.setMaximumSize(QSize(16777215, 120))
        self.Physical_pageIntro.setFont(font1)
        self.Physical_pageIntro.setStyleSheet(u"background-color: #B39DDB")
        self.Physical_pageIntro.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.Physical_pageIntro)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.BOD_button = QPushButton(self.physical_page)
        self.BOD_button.setObjectName(u"BOD_button")
        self.BOD_button.setFont(font3)
        self.BOD_button.setStyleSheet(u"QPushButton {\n"
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
        self.BOD_button.setIcon(icon1)
        self.BOD_button.setIconSize(QSize(40, 40))
        self.BOD_button.setCheckable(True)
        self.BOD_button.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.BOD_button)

        self.melefic_button = QPushButton(self.physical_page)
        self.melefic_button.setObjectName(u"melefic_button")
        self.melefic_button.setFont(font3)
        self.melefic_button.setStyleSheet(u"QPushButton {\n"
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
        self.melefic_button.setIcon(icon9)
        self.melefic_button.setIconSize(QSize(40, 40))
        self.melefic_button.setCheckable(True)
        self.melefic_button.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.melefic_button)

        self.GreatDragon_button = QPushButton(self.physical_page)
        self.GreatDragon_button.setObjectName(u"GreatDragon_button")
        self.GreatDragon_button.setFont(font3)
        self.GreatDragon_button.setStyleSheet(u"QPushButton {\n"
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
        self.GreatDragon_button.setIcon(icon39)
        self.GreatDragon_button.setIconSize(QSize(40, 40))
        self.GreatDragon_button.setCheckable(True)
        self.GreatDragon_button.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.GreatDragon_button)

        self.SeaHalbert_button = QPushButton(self.physical_page)
        self.SeaHalbert_button.setObjectName(u"SeaHalbert_button")
        self.SeaHalbert_button.setFont(font3)
        self.SeaHalbert_button.setStyleSheet(u"QPushButton {\n"
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
        self.SeaHalbert_button.setIcon(icon3)
        self.SeaHalbert_button.setIconSize(QSize(40, 40))
        self.SeaHalbert_button.setCheckable(True)
        self.SeaHalbert_button.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.SeaHalbert_button)

        self.Bloodlust_button = QPushButton(self.physical_page)
        self.Bloodlust_button.setObjectName(u"Bloodlust_button")
        self.Bloodlust_button.setFont(font3)
        self.Bloodlust_button.setStyleSheet(u"QPushButton {\n"
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
        self.Bloodlust_button.setIcon(icon38)
        self.Bloodlust_button.setIconSize(QSize(40, 40))
        self.Bloodlust_button.setCheckable(True)
        self.Bloodlust_button.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Bloodlust_button)

        self.Hunter_button = QPushButton(self.physical_page)
        self.Hunter_button.setObjectName(u"Hunter_button")
        self.Hunter_button.setFont(font3)
        self.Hunter_button.setStyleSheet(u"QPushButton {\n"
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
        self.Hunter_button.setIcon(icon35)
        self.Hunter_button.setIconSize(QSize(40, 40))
        self.Hunter_button.setCheckable(True)
        self.Hunter_button.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Hunter_button)

        self.RoseGold_button = QPushButton(self.physical_page)
        self.RoseGold_button.setObjectName(u"RoseGold_button")
        self.RoseGold_button.setFont(font3)
        self.RoseGold_button.setStyleSheet(u"QPushButton {\n"
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
        self.RoseGold_button.setIcon(icon37)
        self.RoseGold_button.setIconSize(QSize(40, 40))
        self.RoseGold_button.setCheckable(True)
        self.RoseGold_button.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.RoseGold_button)

        self.Heptaseas_button = QPushButton(self.physical_page)
        self.Heptaseas_button.setObjectName(u"Heptaseas_button")
        self.Heptaseas_button.setFont(font3)
        self.Heptaseas_button.setStyleSheet(u"QPushButton {\n"
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
        self.Heptaseas_button.setIcon(icon4)
        self.Heptaseas_button.setIconSize(QSize(40, 40))
        self.Heptaseas_button.setCheckable(True)
        self.Heptaseas_button.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Heptaseas_button)

        self.Windtalker_button = QPushButton(self.physical_page)
        self.Windtalker_button.setObjectName(u"Windtalker_button")
        self.Windtalker_button.setFont(font4)
        self.Windtalker_button.setStyleSheet(u"QPushButton {\n"
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
        self.Windtalker_button.setIcon(icon8)
        self.Windtalker_button.setIconSize(QSize(40, 40))
        self.Windtalker_button.setCheckable(True)
        self.Windtalker_button.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Windtalker_button)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.Endless_button = QPushButton(self.physical_page)
        self.Endless_button.setObjectName(u"Endless_button")
        self.Endless_button.setFont(font3)
        self.Endless_button.setStyleSheet(u"QPushButton {\n"
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
        self.Endless_button.setIcon(icon2)
        self.Endless_button.setIconSize(QSize(40, 40))
        self.Endless_button.setCheckable(True)
        self.Endless_button.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.Endless_button)

        self.Berserker_button = QPushButton(self.physical_page)
        self.Berserker_button.setObjectName(u"Berserker_button")
        self.Berserker_button.setFont(font3)
        self.Berserker_button.setStyleSheet(u"QPushButton {\n"
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
        self.Berserker_button.setIcon(icon32)
        self.Berserker_button.setIconSize(QSize(40, 40))
        self.Berserker_button.setCheckable(True)
        self.Berserker_button.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.Berserker_button)

        self.Haas_button = QPushButton(self.physical_page)
        self.Haas_button.setObjectName(u"Haas_button")
        self.Haas_button.setFont(font3)
        self.Haas_button.setStyleSheet(u"QPushButton {\n"
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
        self.Haas_button.setIcon(icon33)
        self.Haas_button.setIconSize(QSize(40, 40))
        self.Haas_button.setCheckable(True)
        self.Haas_button.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.Haas_button)

        self.WarX_button = QPushButton(self.physical_page)
        self.WarX_button.setObjectName(u"WarX_button")
        self.WarX_button.setFont(font3)
        self.WarX_button.setStyleSheet(u"QPushButton {\n"
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
        self.WarX_button.setIcon(icon34)
        self.WarX_button.setIconSize(QSize(40, 40))
        self.WarX_button.setCheckable(True)
        self.WarX_button.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.WarX_button)

        self.WON_button = QPushButton(self.physical_page)
        self.WON_button.setObjectName(u"WON_button")
        self.WON_button.setFont(font3)
        self.WON_button.setStyleSheet(u"QPushButton {\n"
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
        self.WON_button.setIcon(icon5)
        self.WON_button.setIconSize(QSize(40, 40))
        self.WON_button.setCheckable(True)
        self.WON_button.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.WON_button)

        self.Golden_button = QPushButton(self.physical_page)
        self.Golden_button.setObjectName(u"Golden_button")
        self.Golden_button.setFont(font3)
        self.Golden_button.setStyleSheet(u"QPushButton {\n"
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
        self.Golden_button.setIcon(icon36)
        self.Golden_button.setIconSize(QSize(40, 40))
        self.Golden_button.setCheckable(True)
        self.Golden_button.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.Golden_button)

        self.Corrosion_button = QPushButton(self.physical_page)
        self.Corrosion_button.setObjectName(u"Corrosion_button")
        self.Corrosion_button.setFont(font3)
        self.Corrosion_button.setStyleSheet(u"QPushButton {\n"
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
        self.Corrosion_button.setIcon(icon7)
        self.Corrosion_button.setIconSize(QSize(40, 40))
        self.Corrosion_button.setCheckable(True)
        self.Corrosion_button.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.Corrosion_button)

        self.DHS_button = QPushButton(self.physical_page)
        self.DHS_button.setObjectName(u"DHS_button")
        self.DHS_button.setFont(font3)
        self.DHS_button.setStyleSheet(u"QPushButton {\n"
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
        self.DHS_button.setIcon(icon6)
        self.DHS_button.setIconSize(QSize(40, 40))
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
        self.MagicItemTitle.setFont(font1)
        self.MagicItemTitle.setStyleSheet(u"background-color: rgb(46, 154, 255);")
        self.MagicItemTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.MagicItemTitle)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.Flask_button = QPushButton(self.magic_page)
        self.Flask_button.setObjectName(u"Flask_button")
        self.Flask_button.setFont(font3)
        self.Flask_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #90CAF9;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E88E5;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D8BFD8;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.Flask_button.setIcon(icon40)
        self.Flask_button.setIconSize(QSize(40, 40))
        self.Flask_button.setCheckable(True)
        self.Flask_button.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.Flask_button)

        self.Genius_button = QPushButton(self.magic_page)
        self.Genius_button.setObjectName(u"Genius_button")
        self.Genius_button.setFont(font3)
        self.Genius_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #90CAF9;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E88E5;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D8BFD8;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.Genius_button.setIcon(icon14)
        self.Genius_button.setIconSize(QSize(40, 40))
        self.Genius_button.setCheckable(True)
        self.Genius_button.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.Genius_button)

        self.lightning_button = QPushButton(self.magic_page)
        self.lightning_button.setObjectName(u"lightning_button")
        self.lightning_button.setFont(font3)
        self.lightning_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #90CAF9;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E88E5;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D8BFD8;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.lightning_button.setIcon(icon42)
        self.lightning_button.setIconSize(QSize(40, 40))
        self.lightning_button.setCheckable(True)
        self.lightning_button.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.lightning_button)

        self.fleeting_button = QPushButton(self.magic_page)
        self.fleeting_button.setObjectName(u"fleeting_button")
        self.fleeting_button.setFont(font3)
        self.fleeting_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #90CAF9;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E88E5;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D8BFD8;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.fleeting_button.setIcon(icon43)
        self.fleeting_button.setIconSize(QSize(40, 40))
        self.fleeting_button.setCheckable(True)
        self.fleeting_button.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.fleeting_button)

        self.BloodWings_button = QPushButton(self.magic_page)
        self.BloodWings_button.setObjectName(u"BloodWings_button")
        self.BloodWings_button.setFont(font3)
        self.BloodWings_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #90CAF9;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E88E5;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D8BFD8;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.BloodWings_button.setIcon(icon44)
        self.BloodWings_button.setIconSize(QSize(40, 40))
        self.BloodWings_button.setCheckable(True)
        self.BloodWings_button.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.BloodWings_button)

        self.COD_button = QPushButton(self.magic_page)
        self.COD_button.setObjectName(u"COD_button")
        self.COD_button.setFont(font3)
        self.COD_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #90CAF9;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E88E5;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D8BFD8;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.COD_button.setIcon(icon13)
        self.COD_button.setIconSize(QSize(40, 40))
        self.COD_button.setCheckable(True)
        self.COD_button.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.COD_button)

        self.Starlium_button = QPushButton(self.magic_page)
        self.Starlium_button.setObjectName(u"Starlium_button")
        self.Starlium_button.setFont(font3)
        self.Starlium_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #90CAF9;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E88E5;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D8BFD8;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.Starlium_button.setIcon(icon15)
        self.Starlium_button.setIconSize(QSize(40, 40))
        self.Starlium_button.setCheckable(True)
        self.Starlium_button.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.Starlium_button)


        self.horizontalLayout_7.addLayout(self.verticalLayout_12)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.Glowing_button = QPushButton(self.magic_page)
        self.Glowing_button.setObjectName(u"Glowing_button")
        self.Glowing_button.setFont(font3)
        self.Glowing_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #90CAF9;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E88E5;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D8BFD8;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.Glowing_button.setIcon(icon47)
        self.Glowing_button.setIconSize(QSize(40, 40))
        self.Glowing_button.setCheckable(True)
        self.Glowing_button.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.Glowing_button)

        self.IceQueenWand_button = QPushButton(self.magic_page)
        self.IceQueenWand_button.setObjectName(u"IceQueenWand_button")
        self.IceQueenWand_button.setFont(font3)
        self.IceQueenWand_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #90CAF9;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E88E5;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D8BFD8;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.IceQueenWand_button.setIcon(icon10)
        self.IceQueenWand_button.setIconSize(QSize(40, 40))
        self.IceQueenWand_button.setCheckable(True)
        self.IceQueenWand_button.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.IceQueenWand_button)

        self.Concentrated_button = QPushButton(self.magic_page)
        self.Concentrated_button.setObjectName(u"Concentrated_button")
        self.Concentrated_button.setFont(font3)
        self.Concentrated_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #90CAF9;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E88E5;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D8BFD8;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.Concentrated_button.setIcon(icon41)
        self.Concentrated_button.setIconSize(QSize(40, 40))
        self.Concentrated_button.setCheckable(True)
        self.Concentrated_button.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.Concentrated_button)

        self.Holy_button = QPushButton(self.magic_page)
        self.Holy_button.setObjectName(u"Holy_button")
        self.Holy_button.setFont(font3)
        self.Holy_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #90CAF9;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E88E5;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D8BFD8;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.Holy_button.setIcon(icon11)
        self.Holy_button.setIconSize(QSize(40, 40))
        self.Holy_button.setCheckable(True)
        self.Holy_button.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.Holy_button)

        self.Divine_button = QPushButton(self.magic_page)
        self.Divine_button.setObjectName(u"Divine_button")
        self.Divine_button.setFont(font3)
        self.Divine_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #90CAF9;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E88E5;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D8BFD8;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.Divine_button.setIcon(icon12)
        self.Divine_button.setIconSize(QSize(40, 40))
        self.Divine_button.setCheckable(True)
        self.Divine_button.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.Divine_button)

        self.NOD_button = QPushButton(self.magic_page)
        self.NOD_button.setObjectName(u"NOD_button")
        self.NOD_button.setFont(font3)
        self.NOD_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #90CAF9;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E88E5;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D8BFD8;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.NOD_button.setIcon(icon45)
        self.NOD_button.setIconSize(QSize(40, 40))
        self.NOD_button.setCheckable(True)
        self.NOD_button.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.NOD_button)

        self.Feather_button = QPushButton(self.magic_page)
        self.Feather_button.setObjectName(u"Feather_button")
        self.Feather_button.setFont(font3)
        self.Feather_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #90CAF9;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E88E5;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D8BFD8;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.Feather_button.setIcon(icon46)
        self.Feather_button.setIconSize(QSize(40, 40))
        self.Feather_button.setCheckable(True)
        self.Feather_button.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.Feather_button)

        self.Winter_button = QPushButton(self.magic_page)
        self.Winter_button.setObjectName(u"Winter_button")
        self.Winter_button.setFont(font3)
        self.Winter_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #90CAF9;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E88E5;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D8BFD8;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.Winter_button.setIcon(icon48)
        self.Winter_button.setIconSize(QSize(40, 40))
        self.Winter_button.setCheckable(True)
        self.Winter_button.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.Winter_button)

        self.Enchanted_button = QPushButton(self.magic_page)
        self.Enchanted_button.setObjectName(u"Enchanted_button")
        self.Enchanted_button.setFont(font3)
        self.Enchanted_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #90CAF9;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E88E5;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D8BFD8;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.Enchanted_button.setIcon(icon49)
        self.Enchanted_button.setIconSize(QSize(40, 40))
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
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"background-color: #90EE90;")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.radiant_button = QPushButton(self.defense_page)
        self.radiant_button.setObjectName(u"radiant_button")
        self.radiant_button.setFont(font3)
        self.radiant_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #D1FFD1;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #B3FFB3;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #90EE90;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.radiant_button.setIcon(icon17)
        self.radiant_button.setIconSize(QSize(40, 40))
        self.radiant_button.setCheckable(True)
        self.radiant_button.setAutoExclusive(True)

        self.verticalLayout_14.addWidget(self.radiant_button)

        self.twilight_button = QPushButton(self.defense_page)
        self.twilight_button.setObjectName(u"twilight_button")
        self.twilight_button.setFont(font3)
        self.twilight_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #D1FFD1;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #B3FFB3;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #90EE90;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.twilight_button.setIcon(icon52)
        self.twilight_button.setIconSize(QSize(40, 40))
        self.twilight_button.setCheckable(True)
        self.twilight_button.setAutoExclusive(True)

        self.verticalLayout_14.addWidget(self.twilight_button)

        self.bruteforce_button = QPushButton(self.defense_page)
        self.bruteforce_button.setObjectName(u"bruteforce_button")
        self.bruteforce_button.setFont(font3)
        self.bruteforce_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #D1FFD1;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #B3FFB3;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #90EE90;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.bruteforce_button.setIcon(icon55)
        self.bruteforce_button.setIconSize(QSize(40, 40))
        self.bruteforce_button.setCheckable(True)
        self.bruteforce_button.setAutoExclusive(True)

        self.verticalLayout_14.addWidget(self.bruteforce_button)

        self.immo_button = QPushButton(self.defense_page)
        self.immo_button.setObjectName(u"immo_button")
        self.immo_button.setFont(font3)
        self.immo_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #D1FFD1;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #B3FFB3;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #90EE90;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.immo_button.setIcon(icon54)
        self.immo_button.setIconSize(QSize(40, 40))
        self.immo_button.setCheckable(True)
        self.immo_button.setAutoExclusive(True)

        self.verticalLayout_14.addWidget(self.immo_button)

        self.dominance_button = QPushButton(self.defense_page)
        self.dominance_button.setObjectName(u"dominance_button")
        self.dominance_button.setFont(font3)
        self.dominance_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #D1FFD1;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #B3FFB3;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #90EE90;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.dominance_button.setIcon(icon19)
        self.dominance_button.setIconSize(QSize(40, 40))
        self.dominance_button.setCheckable(True)
        self.dominance_button.setAutoExclusive(True)

        self.verticalLayout_14.addWidget(self.dominance_button)

        self.athena_button = QPushButton(self.defense_page)
        self.athena_button.setObjectName(u"athena_button")
        self.athena_button.setFont(font3)
        self.athena_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #D1FFD1;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #B3FFB3;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #90EE90;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.athena_button.setIcon(icon21)
        self.athena_button.setIconSize(QSize(40, 40))
        self.athena_button.setCheckable(True)
        self.athena_button.setAutoExclusive(True)

        self.verticalLayout_14.addWidget(self.athena_button)


        self.horizontalLayout_8.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.Oracle_button = QPushButton(self.defense_page)
        self.Oracle_button.setObjectName(u"Oracle_button")
        self.Oracle_button.setFont(font3)
        self.Oracle_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #D1FFD1;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #B3FFB3;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #90EE90;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.Oracle_button.setIcon(icon16)
        self.Oracle_button.setIconSize(QSize(40, 40))
        self.Oracle_button.setCheckable(True)
        self.Oracle_button.setAutoExclusive(True)

        self.verticalLayout_15.addWidget(self.Oracle_button)

        self.antique_button = QPushButton(self.defense_page)
        self.antique_button.setObjectName(u"antique_button")
        self.antique_button.setFont(font3)
        self.antique_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #D1FFD1;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #B3FFB3;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #90EE90;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.antique_button.setIcon(icon50)
        self.antique_button.setIconSize(QSize(40, 40))
        self.antique_button.setCheckable(True)
        self.antique_button.setAutoExclusive(True)

        self.verticalLayout_15.addWidget(self.antique_button)

        self.Guardian_button = QPushButton(self.defense_page)
        self.Guardian_button.setObjectName(u"Guardian_button")
        self.Guardian_button.setFont(font3)
        self.Guardian_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #D1FFD1;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #B3FFB3;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #90EE90;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.Guardian_button.setIcon(icon51)
        self.Guardian_button.setIconSize(QSize(40, 40))
        self.Guardian_button.setCheckable(True)
        self.Guardian_button.setAutoExclusive(True)

        self.verticalLayout_15.addWidget(self.Guardian_button)

        self.cursehelmet_button = QPushButton(self.defense_page)
        self.cursehelmet_button.setObjectName(u"cursehelmet_button")
        self.cursehelmet_button.setFont(font3)
        self.cursehelmet_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #D1FFD1;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #B3FFB3;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #90EE90;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.cursehelmet_button.setIcon(icon53)
        self.cursehelmet_button.setIconSize(QSize(40, 40))
        self.cursehelmet_button.setCheckable(True)
        self.cursehelmet_button.setAutoExclusive(True)

        self.verticalLayout_15.addWidget(self.cursehelmet_button)

        self.thunder_button = QPushButton(self.defense_page)
        self.thunder_button.setObjectName(u"thunder_button")
        self.thunder_button.setFont(font3)
        self.thunder_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #D1FFD1;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #B3FFB3;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #90EE90;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.thunder_button.setIcon(icon20)
        self.thunder_button.setIconSize(QSize(40, 40))
        self.thunder_button.setCheckable(True)
        self.thunder_button.setAutoExclusive(True)

        self.verticalLayout_15.addWidget(self.thunder_button)

        self.queenswings_button = QPushButton(self.defense_page)
        self.queenswings_button.setObjectName(u"queenswings_button")
        self.queenswings_button.setFont(font3)
        self.queenswings_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #D1FFD1;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #B3FFB3;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #90EE90;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.queenswings_button.setIcon(icon18)
        self.queenswings_button.setIconSize(QSize(40, 40))
        self.queenswings_button.setCheckable(True)
        self.queenswings_button.setAutoExclusive(True)

        self.verticalLayout_15.addWidget(self.queenswings_button)

        self.Bladearmor_button = QPushButton(self.defense_page)
        self.Bladearmor_button.setObjectName(u"Bladearmor_button")
        self.Bladearmor_button.setFont(font3)
        self.Bladearmor_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #D1FFD1;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #B3FFB3;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #90EE90;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.Bladearmor_button.setIcon(icon22)
        self.Bladearmor_button.setIconSize(QSize(40, 40))
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
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"background-color: rgb(245, 229, 255);")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.demonBoots_button = QPushButton(self.movement_page)
        self.demonBoots_button.setObjectName(u"demonBoots_button")
        self.demonBoots_button.setFont(font3)
        self.demonBoots_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD1DC;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFE4E1;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FFB6C1;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.demonBoots_button.setIcon(icon23)
        self.demonBoots_button.setIconSize(QSize(40, 40))
        self.demonBoots_button.setCheckable(True)
        self.demonBoots_button.setAutoExclusive(True)

        self.verticalLayout_17.addWidget(self.demonBoots_button)

        self.RapidBoots_button = QPushButton(self.movement_page)
        self.RapidBoots_button.setObjectName(u"RapidBoots_button")
        self.RapidBoots_button.setFont(font3)
        self.RapidBoots_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD1DC;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFE4E1;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FFB6C1;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.RapidBoots_button.setIcon(icon24)
        self.RapidBoots_button.setIconSize(QSize(40, 40))
        self.RapidBoots_button.setCheckable(True)
        self.RapidBoots_button.setAutoExclusive(True)

        self.verticalLayout_17.addWidget(self.RapidBoots_button)

        self.swiftboots_button = QPushButton(self.movement_page)
        self.swiftboots_button.setObjectName(u"swiftboots_button")
        self.swiftboots_button.setFont(font3)
        self.swiftboots_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD1DC;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFE4E1;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FFB6C1;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.swiftboots_button.setIcon(icon56)
        self.swiftboots_button.setIconSize(QSize(40, 40))
        self.swiftboots_button.setCheckable(True)
        self.swiftboots_button.setAutoExclusive(True)

        self.verticalLayout_17.addWidget(self.swiftboots_button)

        self.ArcaneBoots_button = QPushButton(self.movement_page)
        self.ArcaneBoots_button.setObjectName(u"ArcaneBoots_button")
        self.ArcaneBoots_button.setFont(font3)
        self.ArcaneBoots_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD1DC;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFE4E1;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FFB6C1;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.ArcaneBoots_button.setIcon(icon31)
        self.ArcaneBoots_button.setIconSize(QSize(40, 40))
        self.ArcaneBoots_button.setCheckable(True)
        self.ArcaneBoots_button.setAutoExclusive(True)

        self.verticalLayout_17.addWidget(self.ArcaneBoots_button)

        self.MagicBoots_button = QPushButton(self.movement_page)
        self.MagicBoots_button.setObjectName(u"MagicBoots_button")
        self.MagicBoots_button.setFont(font3)
        self.MagicBoots_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD1DC;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFE4E1;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FFB6C1;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.MagicBoots_button.setIcon(icon30)
        self.MagicBoots_button.setIconSize(QSize(40, 40))
        self.MagicBoots_button.setCheckable(True)
        self.MagicBoots_button.setAutoExclusive(True)

        self.verticalLayout_17.addWidget(self.MagicBoots_button)

        self.ToughBoots_button = QPushButton(self.movement_page)
        self.ToughBoots_button.setObjectName(u"ToughBoots_button")
        self.ToughBoots_button.setFont(font3)
        self.ToughBoots_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD1DC;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFE4E1;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FFB6C1;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.ToughBoots_button.setIcon(icon28)
        self.ToughBoots_button.setIconSize(QSize(40, 40))
        self.ToughBoots_button.setCheckable(True)
        self.ToughBoots_button.setAutoExclusive(True)

        self.verticalLayout_17.addWidget(self.ToughBoots_button)

        self.WarriorBoots_button = QPushButton(self.movement_page)
        self.WarriorBoots_button.setObjectName(u"WarriorBoots_button")
        self.WarriorBoots_button.setFont(font3)
        self.WarriorBoots_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD1DC;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFE4E1;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FFB6C1;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.WarriorBoots_button.setIcon(icon29)
        self.WarriorBoots_button.setIconSize(QSize(40, 40))
        self.WarriorBoots_button.setCheckable(True)
        self.WarriorBoots_button.setAutoExclusive(True)

        self.verticalLayout_17.addWidget(self.WarriorBoots_button)


        self.horizontalLayout_9.addLayout(self.verticalLayout_17)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.FlameRetri_button = QPushButton(self.movement_page)
        self.FlameRetri_button.setObjectName(u"FlameRetri_button")
        self.FlameRetri_button.setFont(font3)
        self.FlameRetri_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD1DC;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFE4E1;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FFB6C1;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.FlameRetri_button.setIcon(icon25)
        self.FlameRetri_button.setIconSize(QSize(40, 40))
        self.FlameRetri_button.setCheckable(True)
        self.FlameRetri_button.setAutoExclusive(True)

        self.verticalLayout_18.addWidget(self.FlameRetri_button)

        self.IceRetri_button = QPushButton(self.movement_page)
        self.IceRetri_button.setObjectName(u"IceRetri_button")
        self.IceRetri_button.setFont(font3)
        self.IceRetri_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD1DC;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFE4E1;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FFB6C1;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.IceRetri_button.setIcon(icon26)
        self.IceRetri_button.setIconSize(QSize(40, 40))
        self.IceRetri_button.setCheckable(True)
        self.IceRetri_button.setAutoExclusive(True)

        self.verticalLayout_18.addWidget(self.IceRetri_button)

        self.BloodyRetri_button = QPushButton(self.movement_page)
        self.BloodyRetri_button.setObjectName(u"BloodyRetri_button")
        self.BloodyRetri_button.setFont(font3)
        self.BloodyRetri_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD1DC;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFE4E1;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FFB6C1;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.BloodyRetri_button.setIcon(icon27)
        self.BloodyRetri_button.setIconSize(QSize(40, 40))
        self.BloodyRetri_button.setCheckable(True)
        self.BloodyRetri_button.setAutoExclusive(True)

        self.verticalLayout_18.addWidget(self.BloodyRetri_button)

        self.Conceal_button = QPushButton(self.movement_page)
        self.Conceal_button.setObjectName(u"Conceal_button")
        self.Conceal_button.setFont(font3)
        self.Conceal_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD1DC;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFE4E1;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FFB6C1;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.Conceal_button.setIcon(icon57)
        self.Conceal_button.setIconSize(QSize(40, 40))
        self.Conceal_button.setCheckable(True)
        self.Conceal_button.setAutoExclusive(True)

        self.verticalLayout_18.addWidget(self.Conceal_button)

        self.Encourage_button = QPushButton(self.movement_page)
        self.Encourage_button.setObjectName(u"Encourage_button")
        self.Encourage_button.setFont(font3)
        self.Encourage_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD1DC;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFE4E1;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FFB6C1;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.Encourage_button.setIcon(icon58)
        self.Encourage_button.setIconSize(QSize(40, 40))
        self.Encourage_button.setCheckable(True)
        self.Encourage_button.setAutoExclusive(True)

        self.verticalLayout_18.addWidget(self.Encourage_button)

        self.Favour_button = QPushButton(self.movement_page)
        self.Favour_button.setObjectName(u"Favour_button")
        self.Favour_button.setFont(font3)
        self.Favour_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD1DC;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFE4E1;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FFB6C1;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.Favour_button.setIcon(icon59)
        self.Favour_button.setIconSize(QSize(40, 40))
        self.Favour_button.setCheckable(True)
        self.Favour_button.setAutoExclusive(True)

        self.verticalLayout_18.addWidget(self.Favour_button)

        self.Dire_button = QPushButton(self.movement_page)
        self.Dire_button.setObjectName(u"Dire_button")
        self.Dire_button.setFont(font3)
        self.Dire_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD1DC;\n"
"    border: 2px solid #E0BAFF;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFE4E1;\n"
"    border: 2px solid #BAFFC9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FFB6C1;\n"
"    border: 2px solid #FFFFBA;\n"
"}\n"
"")
        self.Dire_button.setIcon(icon60)
        self.Dire_button.setIconSize(QSize(40, 40))
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
        font5 = QFont()
        font5.setPointSize(20)
        font5.setBold(True)
        self.ItemIMG.setFont(font5)
        self.ItemIMG.setStyleSheet(u"QLabel {\n"
"    background: qlineargradient(\n"
"        spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,\n"
"        stop: 0 #FFB3BA, stop: 0.2 #FFDFBA, stop: 0.4 #FFFFBA,\n"
"        stop: 0.6 #BAFFC9, stop: 0.8 #BAE1FF, stop: 1 #E0BAFF\n"
"    );\n"
"}\n"
"")
        self.ItemIMG.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.ItemIMG)

        self.ItemName = QLabel(self.page)
        self.ItemName.setObjectName(u"ItemName")
        font6 = QFont()
        font6.setPointSize(18)
        font6.setBold(True)
        font6.setItalic(False)
        font6.setUnderline(True)
        self.ItemName.setFont(font6)
        self.ItemName.setLayoutDirection(Qt.LeftToRight)
        self.ItemName.setStyleSheet(u"QLabel {\n"
"    background: qlineargradient(\n"
"        spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,\n"
"        stop: 0 #FFB3BA, stop: 0.2 #FFDFBA, stop: 0.4 #FFFFBA,\n"
"        stop: 0.6 #BAFFC9, stop: 0.8 #BAE1FF, stop: 1 #E0BAFF\n"
"    );\n"
"}\n"
"")
        self.ItemName.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.ItemName)

        self.ItemName_2 = QLabel(self.page)
        self.ItemName_2.setObjectName(u"ItemName_2")
        self.ItemName_2.setFont(font2)
        self.ItemName_2.setStyleSheet(u"background-color: rgb(210, 255, 206);")

        self.verticalLayout_8.addWidget(self.ItemName_2)

        self.ItemAttributes = QLabel(self.page)
        self.ItemAttributes.setObjectName(u"ItemAttributes")
        font7 = QFont()
        font7.setPointSize(16)
        font7.setBold(True)
        self.ItemAttributes.setFont(font7)
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
        font8 = QFont()
        font8.setPointSize(18)
        font8.setBold(False)
        self.ItemPassive.setFont(font8)
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
        font9 = QFont()
        font9.setPointSize(12)
        font9.setBold(True)
        self.label_3.setFont(font9)

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
        icon61 = QIcon()
        icon61.addFile(u":/images/home_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Homename.setIcon(icon61)
        self.Homename.setIconSize(QSize(30, 30))
        self.Homename.setCheckable(True)
        self.Homename.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Homename)

        self.AllItemsName = QPushButton(self.icon_name_widget)
        self.AllItemsName.setObjectName(u"AllItemsName")
        icon62 = QIcon()
        icon62.addFile(u":/images/all_items.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AllItemsName.setIcon(icon62)
        self.AllItemsName.setIconSize(QSize(30, 30))
        self.AllItemsName.setCheckable(True)
        self.AllItemsName.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.AllItemsName)

        self.physicalname = QPushButton(self.icon_name_widget)
        self.physicalname.setObjectName(u"physicalname")
        self.physicalname.setIcon(icon1)
        self.physicalname.setIconSize(QSize(30, 30))
        self.physicalname.setCheckable(True)
        self.physicalname.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.physicalname)

        self.magicname = QPushButton(self.icon_name_widget)
        self.magicname.setObjectName(u"magicname")
        self.magicname.setIcon(icon14)
        self.magicname.setIconSize(QSize(30, 30))
        self.magicname.setCheckable(True)
        self.magicname.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.magicname)

        self.defensename = QPushButton(self.icon_name_widget)
        self.defensename.setObjectName(u"defensename")
        self.defensename.setIcon(icon50)
        self.defensename.setIconSize(QSize(30, 30))
        self.defensename.setCheckable(True)
        self.defensename.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.defensename)

        self.bootsname = QPushButton(self.icon_name_widget)
        self.bootsname.setObjectName(u"bootsname")
        self.bootsname.setIcon(icon56)
        self.bootsname.setIconSize(QSize(30, 30))
        self.bootsname.setCheckable(True)
        self.bootsname.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.bootsname)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 341, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.exitname = QPushButton(self.icon_name_widget)
        self.exitname.setObjectName(u"exitname")
        icon63 = QIcon()
        icon63.addFile(u":/images/log_out.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exitname.setIcon(icon63)
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
        self.Homeicon.setIcon(icon61)
        self.Homeicon.setIconSize(QSize(30, 30))
        self.Homeicon.setCheckable(True)
        self.Homeicon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Homeicon)

        self.AllItemsIcon = QPushButton(self.icon_only_widget)
        self.AllItemsIcon.setObjectName(u"AllItemsIcon")
        self.AllItemsIcon.setIcon(icon62)
        self.AllItemsIcon.setIconSize(QSize(30, 30))
        self.AllItemsIcon.setCheckable(True)
        self.AllItemsIcon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.AllItemsIcon)

        self.physicalicon = QPushButton(self.icon_only_widget)
        self.physicalicon.setObjectName(u"physicalicon")
        self.physicalicon.setIcon(icon1)
        self.physicalicon.setIconSize(QSize(30, 30))
        self.physicalicon.setCheckable(True)
        self.physicalicon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.physicalicon)

        self.magicicon = QPushButton(self.icon_only_widget)
        self.magicicon.setObjectName(u"magicicon")
        self.magicicon.setIcon(icon14)
        self.magicicon.setIconSize(QSize(30, 30))
        self.magicicon.setCheckable(True)
        self.magicicon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.magicicon)

        self.defenseicon = QPushButton(self.icon_only_widget)
        self.defenseicon.setObjectName(u"defenseicon")
        self.defenseicon.setIcon(icon50)
        self.defenseicon.setIconSize(QSize(30, 30))
        self.defenseicon.setCheckable(True)
        self.defenseicon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.defenseicon)

        self.bootsicon = QPushButton(self.icon_only_widget)
        self.bootsicon.setObjectName(u"bootsicon")
        self.bootsicon.setIcon(icon56)
        self.bootsicon.setIconSize(QSize(30, 30))
        self.bootsicon.setCheckable(True)
        self.bootsicon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.bootsicon)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 336, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.exiticon = QPushButton(self.icon_only_widget)
        self.exiticon.setObjectName(u"exiticon")
        self.exiticon.setIcon(icon63)
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

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu.setText("")
        self.welcome_text.setText(QCoreApplication.translate("MainWindow", u"WELCOME TO THE ULTIMATE MLBB ITEMS GUIDE", None))
        self.WelcomeDescription.setText(QCoreApplication.translate("MainWindow", u"Are you ready to elevate your Mobile Legends gameplay? Whether you're a seasoned veteran or just starting your journey in the Land of Dawn, mastering the right items can make all the difference between victory and defeat. Our comprehensive items guide is designed to provide you with detailed insights to optimize your hero builds and dominate the battlefield. ", None))
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ALL ITEMS", None))
        self.BOD_button_2.setText(QCoreApplication.translate("MainWindow", u"Blade of Despair", None))
        self.Endless_button_2.setText(QCoreApplication.translate("MainWindow", u"Endless Battle", None))
        self.SeaHalbert_button_2.setText(QCoreApplication.translate("MainWindow", u"Sea Halbert", None))
        self.Heptaseas_button_2.setText(QCoreApplication.translate("MainWindow", u"Blade of Heptaseas", None))
        self.WON_button_2.setText(QCoreApplication.translate("MainWindow", u"Wind of Nature", None))
        self.DHS_button_2.setText(QCoreApplication.translate("MainWindow", u"Demon Hunter Sword", None))
        self.Corrosion_button_2.setText(QCoreApplication.translate("MainWindow", u"Corrosion Scythe", None))
        self.Windtalker_button_2.setText(QCoreApplication.translate("MainWindow", u"Windtalker", None))
        self.melefic_button_2.setText(QCoreApplication.translate("MainWindow", u"Melefic Roar", None))
        self.IceQueenWand_button_2.setText(QCoreApplication.translate("MainWindow", u"Ice Queen Wand", None))
        self.Holy_button_2.setText(QCoreApplication.translate("MainWindow", u"Holy Crystal", None))
        self.Divine_button_2.setText(QCoreApplication.translate("MainWindow", u"Divine Glaive", None))
        self.COD_button_2.setText(QCoreApplication.translate("MainWindow", u"Clock of Destiny", None))
        self.Genius_button_2.setText(QCoreApplication.translate("MainWindow", u"Genius Wand", None))
        self.Starlium_button_2.setText(QCoreApplication.translate("MainWindow", u"Starlium Scythe", None))
        self.Oracle_button_2.setText(QCoreApplication.translate("MainWindow", u"Oracle", None))
        self.radiant_button_2.setText(QCoreApplication.translate("MainWindow", u"Radiant Armor", None))
        self.queenswings_button_2.setText(QCoreApplication.translate("MainWindow", u"Queen's Wings", None))
        self.dominance_button_2.setText(QCoreApplication.translate("MainWindow", u"Dominance Ice", None))
        self.thunder_button_2.setText(QCoreApplication.translate("MainWindow", u"Thunder Belt", None))
        self.athena_button_2.setText(QCoreApplication.translate("MainWindow", u"AthenaSheild", None))
        self.Bladearmor_button_2.setText(QCoreApplication.translate("MainWindow", u"Blade Armor", None))
        self.demonBoots_button_2.setText(QCoreApplication.translate("MainWindow", u"Demon Boots", None))
        self.RapidBoots_button_2.setText(QCoreApplication.translate("MainWindow", u"Rapid Boots", None))
        self.FlameRetri_button_2.setText(QCoreApplication.translate("MainWindow", u"Flame Retribution", None))
        self.IceRetri_button_2.setText(QCoreApplication.translate("MainWindow", u"Ice Retribution", None))
        self.BloodyRetri_button_2.setText(QCoreApplication.translate("MainWindow", u"Bloody Retribution", None))
        self.ToughBoots_button_2.setText(QCoreApplication.translate("MainWindow", u"Tough Boots", None))
        self.WarriorBoots_button_2.setText(QCoreApplication.translate("MainWindow", u"Warrior Boots", None))
        self.MagicBoots_button_2.setText(QCoreApplication.translate("MainWindow", u"Magic Boots", None))
        self.ArcaneBoots_button_2.setText(QCoreApplication.translate("MainWindow", u"Arcane Boots", None))
        self.Berserker_button_2.setText(QCoreApplication.translate("MainWindow", u"Berserker's Fury", None))
        self.Haas_button_2.setText(QCoreApplication.translate("MainWindow", u"Hass's Claws", None))
        self.WarX_button_2.setText(QCoreApplication.translate("MainWindow", u"War Axe", None))
        self.Hunter_button_2.setText(QCoreApplication.translate("MainWindow", u"Hunter Strike", None))
        self.Golden_button_2.setText(QCoreApplication.translate("MainWindow", u"Golden Staff", None))
        self.RoseGold_button_2.setText(QCoreApplication.translate("MainWindow", u"Rose Gold Meteor", None))
        self.Bloodlust_button_2.setText(QCoreApplication.translate("MainWindow", u"Bloodlust Axe", None))
        self.GreatDragon_button_2.setText(QCoreApplication.translate("MainWindow", u"Great Dragon Spear", None))
        self.Flask_button_2.setText(QCoreApplication.translate("MainWindow", u"Flask of The Oasis", None))
        self.Concentrated_button_2.setText(QCoreApplication.translate("MainWindow", u"Concentrated Energy", None))
        self.lightning_button_2.setText(QCoreApplication.translate("MainWindow", u"Lightning Truncheon", None))
        self.fleeting_button_2.setText(QCoreApplication.translate("MainWindow", u"Fleeting Time", None))
        self.BloodWings_button_2.setText(QCoreApplication.translate("MainWindow", u"Blood Wings", None))
        self.NOD_button_2.setText(QCoreApplication.translate("MainWindow", u"Necklace of Durance", None))
        self.Feather_button_2.setText(QCoreApplication.translate("MainWindow", u"Feather of Heaven", None))
        self.Glowing_button_2.setText(QCoreApplication.translate("MainWindow", u"Glowing Wand", None))
        self.Winter_button_2.setText(QCoreApplication.translate("MainWindow", u"Winter Truncheon", None))
        self.Enchanted_button_2.setText(QCoreApplication.translate("MainWindow", u"Enchanted Tailsman", None))
        self.antique_button_2.setText(QCoreApplication.translate("MainWindow", u"Antique Cuirass", None))
        self.Guardian_button_2.setText(QCoreApplication.translate("MainWindow", u"Guardian Helmet", None))
        self.twilight_button_2.setText(QCoreApplication.translate("MainWindow", u"Twilight Armor", None))
        self.cursehelmet_button_2.setText(QCoreApplication.translate("MainWindow", u"Cursed Helmet", None))
        self.immo_button_2.setText(QCoreApplication.translate("MainWindow", u"Immortality", None))
        self.bruteforce_button_2.setText(QCoreApplication.translate("MainWindow", u"Brute Force Breastplate", None))
        self.swiftboots_button_2.setText(QCoreApplication.translate("MainWindow", u"Swift Boots", None))
        self.Conceal_button_2.setText(QCoreApplication.translate("MainWindow", u"Conceal", None))
        self.Encourage_button_2.setText(QCoreApplication.translate("MainWindow", u"Encourage", None))
        self.Favour_button_2.setText(QCoreApplication.translate("MainWindow", u"Favour", None))
        self.Dire_button_2.setText(QCoreApplication.translate("MainWindow", u"DireHit", None))
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
        self.AllItemsName.setText(QCoreApplication.translate("MainWindow", u"ALL ITEMS", None))
        self.physicalname.setText(QCoreApplication.translate("MainWindow", u"PHYSICAL", None))
        self.magicname.setText(QCoreApplication.translate("MainWindow", u"MAGIC", None))
        self.defensename.setText(QCoreApplication.translate("MainWindow", u"DEFENSE", None))
        self.bootsname.setText(QCoreApplication.translate("MainWindow", u"MOVEMENT", None))
        self.exitname.setText(QCoreApplication.translate("MainWindow", u"CLOSE", None))
        self.label.setText("")
        self.Homeicon.setText("")
        self.AllItemsIcon.setText("")
        self.physicalicon.setText("")
        self.magicicon.setText("")
        self.defenseicon.setText("")
        self.bootsicon.setText("")
        self.exiticon.setText("")
    # retranslateUi

