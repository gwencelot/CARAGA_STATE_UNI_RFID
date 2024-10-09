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
        MainWindow.resize(1200, 800)  # Increased size to fit table
        MainWindow.setStyleSheet("background-color: #f5f5f5;")  # Light gray background
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)

        # Create main layout for central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)  # Add margins for better spacing
        
        # Header Layout
        self.header_layout = QtWidgets.QVBoxLayout()
        
        # Title Label
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setText("RFID Vehicle Monitoring System")
        font = QtGui.QFont("Arial", 20, QtGui.QFont.Bold)  # Custom font
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel.setStyleSheet("color: #333333;")  # Dark gray text
        self.header_layout.addWidget(self.titleLabel)

        # School Logo
        self.logoLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoLabel.setPixmap(QtGui.QPixmap("csdu.jpg"))
        self.logoLabel.setScaledContents(True)
        self.logoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.logoLabel.setObjectName("logoLabel")
        self.header_layout.addWidget(self.logoLabel)
        
        # Add header layout to main layout
        self.main_layout.addLayout(self.header_layout)
        
        # Create TabWidget
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setStyleSheet("QTabWidget::pane { border: 1px solid #dddddd; } "
                                     "QTabBar::tab { background: #e6e6e6; padding: 10px; } "
                                     "QTabBar::tab:selected { background: #d4d4d4; }")  # Tab styles
        self.main_layout.addWidget(self.tabWidget)

        # Table Widget
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["RFID", "Name", "ID Number", "Plate", "Time"])
        self.tableWidget.setRowCount(10)  # Example row count
        self.tableWidget.setStyleSheet("QHeaderView::section { background-color: #f0f0f0; padding: 4px; border: 1px solid #dddddd; }")
        self.main_layout.addWidget(self.tableWidget)

        # RFID Viewer Tab
        self.RFID_Viewer = QtWidgets.QWidget()
        self.RFID_Viewer.setObjectName("RFID_Viewer")
        self.rfid_layout = QtWidgets.QGridLayout(self.RFID_Viewer)
        self.rfid_layout.setContentsMargins(10, 10, 10, 10)
        self.rfid_layout.setSpacing(15)

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
        font = QtGui.QFont("Arial", 14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.rfid_layout.addWidget(self.label, 0, 0)

        self.label_2 = ScalableLabel(self.RFID_Viewer)
        font = QtGui.QFont("Arial", 12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.rfid_layout.addWidget(self.label_2, 1, 0)

        self.label_idnumber = ScalableLabel(self.RFID_Viewer)
        font = QtGui.QFont("Arial", 12)
        self.label_idnumber.setFont(font)
        self.label_idnumber.setObjectName("label_idnumber")
        self.rfid_layout.addWidget(self.label_idnumber, 2, 0)

        self.label_3 = ScalableLabel(self.RFID_Viewer)
        font = QtGui.QFont("Arial", 12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.rfid_layout.addWidget(self.label_3, 3, 0)

        self.label_4 = ScalableLabel(self.RFID_Viewer)
        font = QtGui.QFont("Arial", 12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.rfid_layout.addWidget(self.label_4, 4, 0)

        self.tabWidget.addTab(self.RFID_Viewer, "RFID Viewer")

        # Register Tab
        self.Register = QtWidgets.QWidget()
        self.Register.setObjectName("Register")
        self.register_layout = QtWidgets.QGridLayout(self.Register)
        self.register_layout.setContentsMargins(10, 10, 10, 10)
        self.register_layout.setSpacing(15)

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
        font = QtGui.QFont("Arial", 14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.register_layout.addWidget(self.label_7, 0, 0)

        self.label_8 = ScalableLabel(self.Register)
        font = QtGui.QFont("Arial", 12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.register_layout.addWidget(self.label_8, 1, 0)

        self.label_9 = ScalableLabel(self.Register)
        font = QtGui.QFont("Arial", 12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.register_layout.addWidget(self.label_9, 2, 0)

        self.label_10 = ScalableLabel(self.Register)
        font = QtGui.QFont("Arial", 12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.register_layout.addWidget(self.label_10, 3, 0)

        self.label_11 = ScalableLabel(self.Register)
        font = QtGui.QFont("Arial", 12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.register_layout.addWidget(self.label_11, 4, 0)

        self.register_button = QtWidgets.QPushButton(self.Register)
        self.register_button.setText("Register")
        self.register_button.setObjectName("register_button")
        self.register_button.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; border-radius: 10px; padding: 10px 20px; }"
                                           "QPushButton:hover { background-color: #45a049; }")  # Green button
        self.register_layout.addWidget(self.register_button, 5, 0, 1, 2)

        self.tabWidget.addTab(self.Register, "Register")
        
        # Set central widget
        MainWindow.setCentralWidget(self.centralwidget)

        # Set window title
        MainWindow.setWindowTitle("RFID Vehicle Monitoring System")

        # Add labels to each ScalableLabel for their respective text
        self.label.setText("RFID:")
        self.label_2.setText("Name:")
        self.label_idnumber.setText("ID Number:")
        self.label_3.setText("Plate:")
        self.label_4.setText("Time:")

        self.label_7.setText("RFID:")
        self.label_8.setText("Name:")
        self.label_9.setText("ID Number:")
        self.label_10.setText("Plate:")
        self.label_11.setText("Password:")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
