import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QIcon
from items_ui import Ui_MainWindow


class CentralMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Central Application")
        self.setWindowIcon(QIcon("images/mlbb.jpg"))
        self.setGeometry(100, 100, 800, 600)

        # Create the main stacked widget
        self.stackedWidget = QStackedWidget()
        self.setCentralWidget(self.stackedWidget)

        # Initialize the UI components from teammates
        self.itemsWindow = QMainWindow()
        self.itemsUI = Ui_MainWindow()
        self.itemsUI.setupUi(self.itemsWindow)



        # Add each main window to the stacked widget
        self.stackedWidget.addWidget(self.itemsWindow)

        # Create navigation buttons
        self.createNavigation()

    def createNavigation(self):
        # Create a layout for navigation buttons
        navLayout = QVBoxLayout()

        # Create buttons
        self.itemsButton = QPushButton("Items")
        self.heroButton = QPushButton("Hero")
        self.winrateButton = QPushButton("Win Rate Calculator")

        # Connect buttons to methods to change the stacked widget index
        self.itemsButton.clicked.connect(self.showItems)

        # Add buttons to the layout
        navLayout.addWidget(self.itemsButton)
        navLayout.addWidget(self.heroButton)
        navLayout.addWidget(self.winrateButton)

        # Create a navigation widget and set its layout
        navWidget = QWidget()
        navWidget.setLayout(navLayout)

        # Create a horizontal layout to hold the navigation and main content
        mainLayout = QHBoxLayout()
        mainLayout.addWidget(navWidget)
        mainLayout.addWidget(self.stackedWidget)

        # Set the main layout to a central widget
        centralWidget = QWidget()
        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)

    def showItems(self):
        self.stackedWidget.setCurrentWidget(self.itemsWindow)

  
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainApp = CentralMainWindow()
    mainApp.show()
    sys.exit(app.exec())
