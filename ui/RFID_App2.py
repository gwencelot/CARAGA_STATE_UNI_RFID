# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class ScalableLineEdit(QtWidgets.QLineEdit):
    def __init__(self, *args, **kwargs):
        super(ScalableLineEdit, self).__init__(*args, **kwargs)
        self.updateFontSize()

    def resizeEvent(self, event):
        super(ScalableLineEdit, self).resizeEvent(event)
        self.updateFontSize()

    def updateFontSize(self):
        height = self.height()
        font = self.font()
        font.setPointSize(max(int(height / 4), 10))  # Minimum font size of 10 for readability
        self.setFont(font)

class ScalableLabel(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        super(ScalableLabel, self).__init__(*args, **kwargs)
        self.updateFontSize()

    def resizeEvent(self, event):
        super(ScalableLabel, self).resizeEvent(event)
        self.updateFontSize()

    def updateFontSize(self):
        height = self.height()
        font = self.font()
        font.setPointSize(max(int(height / 3), 12))  # Minimum font size of 12 for readability
        self.setFont(font)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 609)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        
        # Central widget and main layout
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_layout = QtWidgets.QVBoxLayout(self.centralwidget)

        # Create TabWidget
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.main_layout.addWidget(self.tabWidget)

        # RFID Viewer Tab
        self.RFID_Viewer = QtWidgets.QWidget()
        self.RFID_Viewer.setObjectName("RFID_Viewer")
        self.rfid_layout = QtWidgets.QGridLayout(self.RFID_Viewer)

        # RFID Viewer Widgets
        self.vrfid = ScalableLineEdit(self.RFID_Viewer)
        self.vrfid.setObjectName("vrfid")
        self.rfid_layout.addWidget(self.vrfid, 0, 1)

        self.vname = ScalableLineEdit(self.RFID_Viewer)
        self.vname.setObjectName("vname")
        self.rfid_layout.addWidget(self.vname, 1, 1)

        self.vidnumber = ScalableLineEdit(self.RFID_Viewer)
        self.vidnumber.setObjectName("vidnumber")
        self.rfid_layout.addWidget(self.vidnumber, 2, 1)

        self.vplate = ScalableLineEdit(self.RFID_Viewer)
        self.vplate.setObjectName("vplate")
        self.rfid_layout.addWidget(self.vplate, 3, 1)

        self.vtime = ScalableLineEdit(self.RFID_Viewer)
        self.vtime.setObjectName("vtime")
        self.rfid_layout.addWidget(self.vtime, 4, 1)

        self.label = ScalableLabel(self.RFID_Viewer)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.rfid_layout.addWidget(self.label, 0, 0)

        self.label_2 = ScalableLabel(self.RFID_Viewer)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.rfid_layout.addWidget(self.label_2, 1, 0)

        self.label_idnumber = ScalableLabel(self.RFID_Viewer)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_idnumber.setFont(font)
        self.label_idnumber.setObjectName("label_idnumber")
        self.rfid_layout.addWidget(self.label_idnumber, 2, 0)

        self.label_3 = ScalableLabel(self.RFID_Viewer)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.rfid_layout.addWidget(self.label_3, 3, 0)

        self.label_4 = ScalableLabel(self.RFID_Viewer)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.rfid_layout.addWidget(self.label_4, 4, 0)

        self.tabWidget.addTab(self.RFID_Viewer, "")

        # Register Tab
        self.Register = QtWidgets.QWidget()
        self.Register.setObjectName("Register")
        self.register_layout = QtWidgets.QGridLayout(self.Register)

        # Register Widgets
        self.rrfid = ScalableLineEdit(self.Register)
        self.rrfid.setObjectName("rrfid")
        self.register_layout.addWidget(self.rrfid, 0, 1)

        self.rname_2 = ScalableLineEdit(self.Register)
        self.rname_2.setObjectName("rname_2")
        self.register_layout.addWidget(self.rname_2, 1, 1)

        self.ridnumber = ScalableLineEdit(self.Register)
        self.ridnumber.setObjectName("ridnumber")
        self.register_layout.addWidget(self.ridnumber, 2, 1)

        self.rplate = ScalableLineEdit(self.Register)
        self.rplate.setObjectName("rplate")
        self.register_layout.addWidget(self.rplate, 3, 1)

        self.password = ScalableLineEdit(self.Register)
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)  # Set echo mode to Password
        self.register_layout.addWidget(self.password, 4, 1)

        self.label_7 = ScalableLabel(self.Register)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.register_layout.addWidget(self.label_7, 0, 0)

        self.rname = ScalableLabel(self.Register)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rname.setFont(font)
        self.rname.setObjectName("rname")
        self.register_layout.addWidget(self.rname, 1, 0)

        self.label_idnumber_reg = ScalableLabel(self.Register)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_idnumber_reg.setFont(font)
        self.label_idnumber_reg.setObjectName("label_idnumber_reg")
        self.register_layout.addWidget(self.label_idnumber_reg, 2, 0)

        self.label_6 = ScalableLabel(self.Register)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.register_layout.addWidget(self.label_6, 3, 0)

        self.label_8 = ScalableLabel(self.Register)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.register_layout.addWidget(self.label_8, 4, 0)

        self.pushButton = QtWidgets.QPushButton(self.Register)
        self.pushButton.setObjectName("pushButton")
        self.register_layout.addWidget(self.pushButton, 5, 1)

        self.tabWidget.addTab(self.Register, "")

        # Header Labels
        self.header_layout = QtWidgets.QVBoxLayout()
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("csdu.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.header_layout.addWidget(self.label_5)

        self.label_9 = ScalableLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.header_layout.addWidget(self.label_9)

        self.label_10 = ScalableLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.header_layout.addWidget(self.label_10)

        self.main_layout.insertLayout(0, self.header_layout)

        # Set size policy for the scalable line edits and labels
        self.vrfid.setSizePolicy(sizePolicy)
        self.vname.setSizePolicy(sizePolicy)
        self.vplate.setSizePolicy(sizePolicy)
        self.vtime.setSizePolicy(sizePolicy)
        self.vidnumber.setSizePolicy(sizePolicy)
        self.rrfid.setSizePolicy(sizePolicy)
        self.rname_2.setSizePolicy(sizePolicy)
        self.rplate.setSizePolicy(sizePolicy)
        self.password.setSizePolicy(sizePolicy)
        self.ridnumber.setSizePolicy(sizePolicy)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "RFID"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "Plate"))
        self.label_4.setText(_translate("MainWindow", "Time"))
        self.label_idnumber.setText(_translate("MainWindow", "ID Number"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RFID_Viewer), _translate("MainWindow", "RFID Viewer"))
        self.label_7.setText(_translate("MainWindow", "RFID"))
        self.label_6.setText(_translate("MainWindow", "Plate"))
        self.rname.setText(_translate("MainWindow", "Name"))
        self.label_8.setText(_translate("MainWindow", "Password"))
        self.label_idnumber_reg.setText(_translate("MainWindow", "ID Number"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Register), _translate("MainWindow", "Register"))
        self.label_9.setText(_translate("MainWindow", "Caraga State University"))
        self.label_10.setText(_translate("MainWindow", "Ampayon, Butuan City"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
