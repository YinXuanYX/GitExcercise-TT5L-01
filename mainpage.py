# Form implementation generated from reading ui file 'Mainpage.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(507, 298)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.overallbtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.overallbtn.setGeometry(QtCore.QRect(160, 30, 161, 41))
        self.overallbtn.setObjectName("overallbtn")
        self.GRbtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.GRbtn.setGeometry(QtCore.QRect(160, 190, 161, 41))
        self.GRbtn.setObjectName("GRbtn")
        self.herobtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.herobtn.setGeometry(QtCore.QRect(160, 110, 161, 41))
        self.herobtn.setObjectName("herobtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 507, 18))
        self.menubar.setObjectName("menubar")
        self.menuWinrate = QtWidgets.QMenu(parent=self.menubar)
        self.menuWinrate.setObjectName("menuWinrate")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuWinrate.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.overallbtn.setText(_translate("MainWindow", "Overall"))
        self.GRbtn.setText(_translate("MainWindow", "Games Required"))
        self.herobtn.setText(_translate("MainWindow", "Hero"))
        self.menuWinrate.setTitle(_translate("MainWindow", "Winrate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
