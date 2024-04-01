# Form implementation generated from reading ui file 'c:\Users\kryst\Desktop\app_vsc\interface.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 600))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.body = QtWidgets.QWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy)
        self.body.setObjectName("body")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.body)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(parent=self.body)
        self.widget.setMinimumSize(QtCore.QSize(0, 60))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnChangeMenu = QtWidgets.QPushButton(parent=self.widget)
        self.btnChangeMenu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/align-justify.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnChangeMenu.setIcon(icon)
        self.btnChangeMenu.setIconSize(QtCore.QSize(30, 30))
        self.btnChangeMenu.setCheckable(True)
        self.btnChangeMenu.setAutoExclusive(False)
        self.btnChangeMenu.setObjectName("btnChangeMenu")
        self.horizontalLayout_4.addWidget(self.btnChangeMenu)
        spacerItem = QtWidgets.QSpacerItem(237, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leSearch = QtWidgets.QLineEdit(parent=self.widget)
        self.leSearch.setObjectName("leSearch")
        self.horizontalLayout.addWidget(self.leSearch)
        self.btnSearch = QtWidgets.QPushButton(parent=self.widget)
        self.btnSearch.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/search.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnSearch.setIcon(icon1)
        self.btnSearch.setIconSize(QtCore.QSize(30, 30))
        self.btnSearch.setCheckable(True)
        self.btnSearch.setAutoExclusive(True)
        self.btnSearch.setObjectName("btnSearch")
        self.horizontalLayout.addWidget(self.btnSearch)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(237, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.btnSettings = QtWidgets.QPushButton(parent=self.widget)
        self.btnSettings.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/settings.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnSettings.setIcon(icon2)
        self.btnSettings.setIconSize(QtCore.QSize(30, 30))
        self.btnSettings.setCheckable(True)
        self.btnSettings.setAutoExclusive(True)
        self.btnSettings.setObjectName("btnSettings")
        self.horizontalLayout_4.addWidget(self.btnSettings)
        self.verticalLayout_5.addWidget(self.widget)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.body)
        self.stackedWidget.setObjectName("stackedWidget")
        self.homePage = QtWidgets.QWidget()
        self.homePage.setObjectName("homePage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.homePage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(parent=self.homePage)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_7.addWidget(self.label_4, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(parent=self.frame)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_6.addWidget(self.label_10)
        self.gridLayout_7.addWidget(self.groupBox, 0, 0, 2, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.frame)
        self.groupBox_2.setObjectName("groupBox_2")
        self.widget1 = QtWidgets.QWidget(parent=self.groupBox_2)
        self.widget1.setGeometry(QtCore.QRect(20, 60, 171, 101))
        self.widget1.setObjectName("widget1")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_9 = QtWidgets.QLabel(parent=self.widget1)
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_8.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(parent=self.widget1)
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_8.addWidget(self.label_11, 1, 0, 1, 1)
        self.btnChangeSettings = QtWidgets.QPushButton(parent=self.widget1)
        self.btnChangeSettings.setObjectName("btnChangeSettings")
        self.gridLayout_8.addWidget(self.btnChangeSettings, 2, 1, 1, 1)
        self.lAdressIP = QtWidgets.QLabel(parent=self.widget1)
        self.lAdressIP.setText("")
        self.lAdressIP.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lAdressIP.setObjectName("lAdressIP")
        self.gridLayout_8.addWidget(self.lAdressIP, 0, 1, 1, 1)
        self.lPort = QtWidgets.QLabel(parent=self.widget1)
        self.lPort.setText("")
        self.lPort.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lPort.setObjectName("lPort")
        self.gridLayout_8.addWidget(self.lPort, 1, 1, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_2, 0, 2, 2, 1)
        self.lRasberryPiImage = QtWidgets.QLabel(parent=self.frame)
        self.lRasberryPiImage.setMinimumSize(QtCore.QSize(430, 320))
        self.lRasberryPiImage.setMaximumSize(QtCore.QSize(430, 320))
        self.lRasberryPiImage.setSizeIncrement(QtCore.QSize(30, 15))
        self.lRasberryPiImage.setText("")
        self.lRasberryPiImage.setPixmap(QtGui.QPixmap("images/rasberry.png"))
        self.lRasberryPiImage.setScaledContents(True)
        self.lRasberryPiImage.setObjectName("lRasberryPiImage")
        self.gridLayout_7.addWidget(self.lRasberryPiImage, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.homePage)
        self.dashBoardPage = QtWidgets.QWidget()
        self.dashBoardPage.setObjectName("dashBoardPage")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.dashBoardPage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(parent=self.dashBoardPage)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.dashBoardPage)
        self.sensorPage = QtWidgets.QWidget()
        self.sensorPage.setObjectName("sensorPage")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.sensorPage)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_6 = QtWidgets.QLabel(parent=self.sensorPage)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.sensorPage)
        self.statisticsPage = QtWidgets.QWidget()
        self.statisticsPage.setObjectName("statisticsPage")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.statisticsPage)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_7 = QtWidgets.QLabel(parent=self.statisticsPage)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.statisticsPage)
        self.logsPage = QtWidgets.QWidget()
        self.logsPage.setObjectName("logsPage")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.logsPage)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_8 = QtWidgets.QLabel(parent=self.logsPage)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.logsPage)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.body, 0, 2, 1, 1)
        self.full_menu_widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.full_menu_widget.setMinimumSize(QtCore.QSize(230, 0))
        self.full_menu_widget.setMaximumSize(QtCore.QSize(230, 16777215))
        self.full_menu_widget.setObjectName("full_menu_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(parent=self.full_menu_widget)
        self.label_2.setMinimumSize(QtCore.QSize(50, 50))
        self.label_2.setMaximumSize(QtCore.QSize(50, 50))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("icons/layers.svg"))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.full_menu_widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnHome2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/home.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnHome2.setIcon(icon3)
        self.btnHome2.setIconSize(QtCore.QSize(30, 30))
        self.btnHome2.setCheckable(True)
        self.btnHome2.setAutoExclusive(True)
        self.btnHome2.setObjectName("btnHome2")
        self.verticalLayout_2.addWidget(self.btnHome2)
        self.btnDashboard2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/youtube.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnDashboard2.setIcon(icon4)
        self.btnDashboard2.setIconSize(QtCore.QSize(30, 30))
        self.btnDashboard2.setCheckable(True)
        self.btnDashboard2.setAutoExclusive(True)
        self.btnDashboard2.setObjectName("btnDashboard2")
        self.verticalLayout_2.addWidget(self.btnDashboard2)
        self.btnSensors2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/message-square.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnSensors2.setIcon(icon5)
        self.btnSensors2.setIconSize(QtCore.QSize(30, 30))
        self.btnSensors2.setCheckable(True)
        self.btnSensors2.setAutoExclusive(True)
        self.btnSensors2.setObjectName("btnSensors2")
        self.verticalLayout_2.addWidget(self.btnSensors2)
        self.btnStatistics2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/camera.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnStatistics2.setIcon(icon6)
        self.btnStatistics2.setIconSize(QtCore.QSize(30, 30))
        self.btnStatistics2.setCheckable(True)
        self.btnStatistics2.setAutoExclusive(True)
        self.btnStatistics2.setObjectName("btnStatistics2")
        self.verticalLayout_2.addWidget(self.btnStatistics2)
        self.btnLogs2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/alert-octagon.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnLogs2.setIcon(icon7)
        self.btnLogs2.setIconSize(QtCore.QSize(30, 30))
        self.btnLogs2.setCheckable(True)
        self.btnLogs2.setAutoExclusive(True)
        self.btnLogs2.setObjectName("btnLogs2")
        self.verticalLayout_2.addWidget(self.btnLogs2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 418, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.btnExit2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/x-square.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnExit2.setIcon(icon8)
        self.btnExit2.setIconSize(QtCore.QSize(30, 30))
        self.btnExit2.setCheckable(True)
        self.btnExit2.setAutoExclusive(True)
        self.btnExit2.setObjectName("btnExit2")
        self.verticalLayout_4.addWidget(self.btnExit2)
        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 1, 1)
        self.icon_only_widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.icon_only_widget.setMaximumSize(QtCore.QSize(80, 16777215))
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label = QtWidgets.QLabel(parent=self.icon_only_widget)
        self.label.setMinimumSize(QtCore.QSize(50, 50))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icons/layers.svg"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnHome1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.btnHome1.setText("")
        self.btnHome1.setIcon(icon3)
        self.btnHome1.setIconSize(QtCore.QSize(30, 30))
        self.btnHome1.setCheckable(True)
        self.btnHome1.setAutoExclusive(True)
        self.btnHome1.setObjectName("btnHome1")
        self.verticalLayout.addWidget(self.btnHome1)
        self.btnDashBoard1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.btnDashBoard1.setText("")
        self.btnDashBoard1.setIcon(icon4)
        self.btnDashBoard1.setIconSize(QtCore.QSize(30, 30))
        self.btnDashBoard1.setCheckable(True)
        self.btnDashBoard1.setAutoExclusive(True)
        self.btnDashBoard1.setObjectName("btnDashBoard1")
        self.verticalLayout.addWidget(self.btnDashBoard1)
        self.btnSensors1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.btnSensors1.setText("")
        self.btnSensors1.setIcon(icon5)
        self.btnSensors1.setIconSize(QtCore.QSize(30, 30))
        self.btnSensors1.setCheckable(True)
        self.btnSensors1.setAutoExclusive(True)
        self.btnSensors1.setObjectName("btnSensors1")
        self.verticalLayout.addWidget(self.btnSensors1)
        self.btnStatistics1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.btnStatistics1.setText("")
        self.btnStatistics1.setIcon(icon6)
        self.btnStatistics1.setIconSize(QtCore.QSize(30, 30))
        self.btnStatistics1.setCheckable(True)
        self.btnStatistics1.setAutoExclusive(True)
        self.btnStatistics1.setObjectName("btnStatistics1")
        self.verticalLayout.addWidget(self.btnStatistics1)
        self.btnLogs1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.btnLogs1.setText("")
        self.btnLogs1.setIcon(icon7)
        self.btnLogs1.setIconSize(QtCore.QSize(30, 30))
        self.btnLogs1.setCheckable(True)
        self.btnLogs1.setAutoExclusive(True)
        self.btnLogs1.setObjectName("btnLogs1")
        self.verticalLayout.addWidget(self.btnLogs1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 418, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.btnExit1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.btnExit1.setText("")
        self.btnExit1.setIcon(icon8)
        self.btnExit1.setIconSize(QtCore.QSize(30, 30))
        self.btnExit1.setCheckable(True)
        self.btnExit1.setAutoExclusive(True)
        self.btnExit1.setObjectName("btnExit1")
        self.verticalLayout_3.addWidget(self.btnExit1)
        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.btnChangeMenu.toggled['bool'].connect(self.icon_only_widget.setVisible) # type: ignore
        self.btnChangeMenu.toggled['bool'].connect(self.full_menu_widget.setHidden) # type: ignore
        self.btnHome1.toggled['bool'].connect(self.btnHome2.setChecked) # type: ignore
        self.btnDashBoard1.toggled['bool'].connect(self.btnDashboard2.setChecked) # type: ignore
        self.btnSensors1.toggled['bool'].connect(self.btnSensors2.setChecked) # type: ignore
        self.btnStatistics1.toggled['bool'].connect(self.btnStatistics2.setChecked) # type: ignore
        self.btnLogs1.toggled['bool'].connect(self.btnLogs2.setChecked) # type: ignore
        self.btnExit1.toggled['bool'].connect(self.btnExit2.setChecked) # type: ignore
        self.btnHome2.toggled['bool'].connect(self.btnHome1.setChecked) # type: ignore
        self.btnDashboard2.toggled['bool'].connect(self.btnDashBoard1.setChecked) # type: ignore
        self.btnSensors2.toggled['bool'].connect(self.btnSensors1.setChecked) # type: ignore
        self.btnStatistics2.toggled['bool'].connect(self.btnStatistics1.setChecked) # type: ignore
        self.btnLogs2.toggled['bool'].connect(self.btnLogs1.setChecked) # type: ignore
        self.btnExit2.toggled['bool'].connect(self.btnExit1.setChecked) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Catepillar Robot app"))
        self.leSearch.setPlaceholderText(_translate("MainWindow", "Wyszukaj..."))
        self.label_4.setText(_translate("MainWindow", "Rasberry Pi 4B"))
        self.groupBox.setTitle(_translate("MainWindow", "Informacje"))
        self.label_10.setText(_translate("MainWindow", "Tutaj będzie info"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Obecne ustawienia"))
        self.label_9.setText(_translate("MainWindow", "Adres IP"))
        self.label_11.setText(_translate("MainWindow", "Port"))
        self.btnChangeSettings.setText(_translate("MainWindow", "Zmień"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "Sensors"))
        self.label_7.setText(_translate("MainWindow", "Statistics"))
        self.label_8.setText(_translate("MainWindow", "Logi"))
        self.label_3.setText(_translate("MainWindow", "App"))
        self.btnHome2.setText(_translate("MainWindow", "Home"))
        self.btnDashboard2.setText(_translate("MainWindow", "Dashboard"))
        self.btnSensors2.setText(_translate("MainWindow", "Sensors"))
        self.btnStatistics2.setText(_translate("MainWindow", "Statistics"))
        self.btnLogs2.setText(_translate("MainWindow", "Logs"))
        self.btnExit2.setText(_translate("MainWindow", "Exit"))