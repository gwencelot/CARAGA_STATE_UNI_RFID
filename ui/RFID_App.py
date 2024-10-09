# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RFID_App.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.RFID_scan = QtWidgets.QLineEdit(self.centralwidget)
        self.RFID_scan.setGeometry(QtCore.QRect(180, 80, 431, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.RFID_scan.setFont(font)
        self.RFID_scan.setObjectName("RFID_scan")
        self.Name = QtWidgets.QLineEdit(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(190, 260, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        self.Plate = QtWidgets.QLineEdit(self.centralwidget)
        self.Plate.setGeometry(QtCore.QRect(190, 340, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Plate.setFont(font)
        self.Plate.setObjectName("Plate")
        self.Time = QtWidgets.QLineEdit(self.centralwidget)
        self.Time.setGeometry(QtCore.QRect(190, 410, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Time.setFont(font)
        self.Time.setObjectName("Time")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 110, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 270, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 340, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 410, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "RFID"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "Plate No."))
        self.label_4.setText(_translate("MainWindow", "Time"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())