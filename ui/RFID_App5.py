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
        MainWindow.setStyleSheet("background-color: #626F47;")  # Light gray background
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)

        # Create main layout for central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)  # Add margins for better spacing
        
       # Header Layout (Change to QHBoxLayout for horizontal alignment)
        self.header_layout = QtWidgets.QHBoxLayout()

        # School Logo
        self.logoLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoLabel.setPixmap(QtGui.QPixmap(r"C:\Python\RFID\ui\imresizer-1728450264830.jpg"))

        # Set a smaller size for the logo
        self.logoLabel.setMinimumSize(100, 100)  # Adjust the size as needed (smaller logo)
        self.logoLabel.setMaximumSize(150, 150)  # Ensure it doesn't get too big

        # Align to the upper-left corner and keep proportions
        self.logoLabel.setScaledContents(True)
        self.logoLabel.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)  # Align horizontally left and vertically centered
        self.logoLabel.setObjectName("logoLabel")

        # Add the logo to the header layout
        self.header_layout.addWidget(self.logoLabel)

        # Title Label
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setText("RFID Vehicle Monitoring System")
        font = QtGui.QFont("Arial", 20, QtGui.QFont.Bold)  # Custom font
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)  # Align left and vertically centered
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel.setStyleSheet("color: #FEFAE0;")  # Dark gray text

        # Add the title label to the header layout
        self.header_layout.addWidget(self.titleLabel)

        # Add the header layout to the main layout
        self.main_layout.addLayout(self.header_layout)

        
        # Create TabWidget
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setStyleSheet("""
                                        QTabWidget::pane {
                                            border: 1px solid #dddddd;
                                        }

                                        QTabBar::tab {
                                            background-color: #347928;  /* Green when not selected */
                                            padding: 10px;
                                            color: white;  /* White text on green background */
                                            font-weight: bold;
                                            border-top-left-radius: 8px;
                                            border-top-right-radius: 8px;
                                            min-width: 100px;  /* Optional: Adjust for minimum tab width */
                                        }

                                        QTabBar::tab:selected {
                                            background-color: #ffffff;  /* White background when selected */
                                            color: #333333;  /* Dark gray text when selected */
                                            border: 1px solid #dddddd;
                                            border-bottom: none;  /* Make sure the selected tab blends into the pane */
                                        }

                                        QTabBar::tab:hover {
                                            background-color: #66A182;  /* Lighter green on hover */
                                            color: white;  /* Ensure text is white when hovered over green */
                                        }
                                    """)

        self.main_layout.addWidget(self.tabWidget)

        # Table Widget
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["RFID", "Name", "ID Number", "Plate", "Time"])
        self.tableWidget.setRowCount(10)  # Example row count

        # Stretch the last column to fill remaining space
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)  # Makes columns stretch to fill the available space
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)  # Ensure last column ("Time") stretches to fill remaining space

        # Adjust the scroll policy to avoid unnecessary scrolling
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)  # Show scrollbars only when necessary
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)

        # Add the improved style for the table
        self.tableWidget.setStyleSheet("""
                                        QHeaderView::section {
                                            background-color: #FFFBE6;  /* Dirty white background for header */
                                            padding: 8px;  /* Increased padding for better spacing */
                                            border: 1px solid #dddddd;  /* Subtle border for clarity */
                                            color: #333333;  /* Dark gray text for readability */
                                            font-weight: bold;  /* Bold text for emphasis */
                                        }
                                        QTableWidget::item {
                                            background-color: #ffffff;  /* White background for rows */
                                            padding: 8px;  /* Padding for table cells */
                                            border: 1px solid #dddddd;  /* Subtle border around rows */
                                            color: #333333;  /* Dark gray text for readability */
                                        }
                                        QTableWidget::item:selected {
                                            background-color: #e0f7fa;  /* Light teal background when a row is selected */
                                            color: #333333;  /* Ensure selected text is still dark gray */
                                        }
                                        QTableWidget::item:hover {
                                            background-color: #f5f5f5;  /* Light gray background on hover */
                                        }
                                    """)

        self.main_layout.addWidget(self.tableWidget)

        # RFID Viewer Tab
        self.RFID_Viewer = QtWidgets.QWidget()
        self.RFID_Viewer.setObjectName("RFID_Viewer")
        self.RFID_Viewer.setStyleSheet("background-color: white;")
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
        self.Register.setStyleSheet("background-color: white;")  # White background for the tab
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
