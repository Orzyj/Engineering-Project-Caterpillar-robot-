from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QPushButton, QDialog, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt, QFile, QTextStream,QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView
from overrides import override
from interface_ui import *
from urlDialog import urlDialog
from settingsDialog import SettingsDialog
import sys
import json

class CameraLayout(QVBoxLayout):
    def __init__(self, ip: str, port: int):
        super().__init__()
        self.__ip: str = ip
        self.__port: int = port
        buttonLayout: QHBoxLayout = QHBoxLayout()
        self.__btnReload: QPushButton = QPushButton("Odśwież")
        self.__btnChangeUrl: QPushButton = QPushButton("Zmień źródło")
        self.__urlText: str = "http://" + self.__ip + ":" + str(self.__port) + "/video_feed"
        self.__url: QUrl = QUrl(self.__urlText)
        self.__urlLabel: QLabel = QLabel(self.__urlText)

        buttonLayout.addWidget(self.__btnReload)
        buttonLayout.addWidget(self.__btnChangeUrl)
        buttonLayout.addWidget(self.__urlLabel)
        buttonLayout.addStretch()

        webEngineLayout = QVBoxLayout()
        self.__webEngineView: QWebEngineView = QWebEngineView()
        webEngineLayout.addWidget(self.__webEngineView)
        webEngineLayout.setContentsMargins(0, 0, 0, 0) 

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(buttonLayout)
        mainLayout.addLayout(webEngineLayout)
        mainLayout.setContentsMargins(0, 0, 0, 0) 

        self.addLayout(mainLayout)
        self.setAlignment(Qt.AlignmentFlag.AlignTop) 
        self.__initBaseConfiguration()

        self.__loadUrl()

    def __loadUrl(self) -> None:
        self.__webEngineView.load(self.__url)

    def __reloadView(self) -> None:
        self.__webEngineView.reload()

    def __initBaseConfiguration(self) -> None:
        self.__btnReload.clicked.connect(lambda: self.__reloadView())
        self.__btnChangeUrl.clicked.connect(lambda: self.__setUrl())

    def __setUrl(self) -> None:
        dialog: urlDialog = urlDialog(self.__urlText)
        result: QDialog.DialogCode = dialog.exec()
        status: bool = dialog.getStatus()

        if result == QDialog.DialogCode.Accepted:
            if status:
                self.__url = dialog.getUrl()
                self.__urlText = dialog.getTextUrl()
                self.__urlLabel.setText(self.__urlText)
                self.__loadUrl()
                self.__reloadView()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__address_ip_rasberry: str = "192.168.1.39"
        self.__port: int = 5000
        self.__json_data: json = json.load(open("resources/settings.json", 'r'))

        self.ui: Ui_MainWindow = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__initBaseConfigurationLayout()
        self.__initCameraLayout()
        self.__settingConnections()

    @override()
    def keyPressEvent(self, event):
        key = event.key()
        
        if key == Qt.Key.Key_W:
            self.__json_data["movements"]["UP"] = True
        elif key == Qt.Key.Key_S:
            self.__json_data["movements"]["DOWN"] = True
        elif key == Qt.Key.Key_D:
            self.__json_data["movements"]["RIGHT"] = True
        elif key == Qt.Key.Key_A:
            self.__json_data["movements"]["LEFT"] = True
        elif key == Qt.Key.Key_Tab:
            self.ui.icon_only_widget.setVisible(not self.ui.icon_only_widget.isVisible())
            self.ui.full_menu_widget.setHidden(not self.ui.full_menu_widget.isHidden())

    @override()
    def keyReleaseEvent(self, event):
        key = event.key()
        
        if key == Qt.Key.Key_W:
            self.__json_data["movements"]["UP"] = False
        elif key == Qt.Key.Key_S:
            self.__json_data["movements"]["DOWN"] = False
        elif key == Qt.Key.Key_D:
            self.__json_data["movements"]["RIGHT"] = False
        elif key == Qt.Key.Key_A:
            self.__json_data["movements"]["LEFT"] = False

    def __initCameraLayout(self) -> None:
        cameraLayout: CameraLayout = CameraLayout(self.__address_ip_rasberry, self.__port)
        self.ui.cameraGroupBox.setLayout(cameraLayout)

    def __onSearchButtonClicked(self) -> None :
        raise NotImplemented("Not implemented code")

    def __onChangePages(self) -> None:
        sender: QPushButton = self.sender()
        index: int = sender.property("index")
        self.ui.stackedWidget.setCurrentIndex(index)

    def __onChangeSettings(self) -> None:
        dialog: SettingsDialog = SettingsDialog(self.__address_ip_rasberry, self.__port)
        result: QDialog.DialogCode = dialog.exec()
        status: bool = dialog.getStatus()

        if result == QDialog.DialogCode.Accepted:
            if status:    
                self.__address_ip_rasberry = dialog.getIpAddress()
                self.__port = dialog.getPort()
                self.__onSettingsChange()
                QMessageBox.information(self, "Powiadomienie", "Dane pomyślnie zaktualizowane")
            else:
                QMessageBox.warning(self, "Powiadomienie", "Wystąpił błąd, danych nie zaktualizowano")

    def __onSettingsChange(self) -> None:
        self.ui.lAdressIP.setText(self.__address_ip_rasberry)
        self.ui.lPort.setText(str(self.__port))

    def __settingConnections(self) -> None:
        self.ui.btnExit1.clicked.connect(lambda: QApplication.quit())
        self.ui.btnExit2.clicked.connect(lambda: QApplication.quit())
        self.ui.btnSearch.clicked.connect(lambda: self.__onSearchButtonClicked())
        self.ui.btnChangeSettings.clicked.connect(lambda: self.__onChangeSettings())
        self.ui.btnSettings.clicked.connect(lambda: self.__onChangeSettings())

        listOfButtons: list[QPushButton] = self.ui.icon_only_widget.findChildren(QPushButton)
        listOfButtonsLongMenu: list[QPushButton] = self.ui.full_menu_widget.findChildren(QPushButton)
        
        #connecting buttons on short menu and gave them a ID
        for i, button in enumerate(listOfButtons[:-1]):
            button.clicked.connect(self.__onChangePages)
            button.setProperty("index", i)

        #connecting button on long menu and gave them a ID
        for i, button in enumerate(listOfButtonsLongMenu[:-1]):
            button.clicked.connect(self.__onChangePages)
            button.setProperty("index", i)

    def __initBaseConfigurationLayout(self) -> None:
        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.btnHome2.setChecked(True)
        self.ui.lAdressIP.setText(self.__address_ip_rasberry)
        self.ui.lPort.setText(str(self.__port))

    

if __name__ == "__main__":
    application: QApplication = QApplication(sys.argv)
    styleFile: QFile = QFile("layouts/mainLayout.qss")

    if styleFile.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):
        styleStream: QTextStream = QTextStream(styleFile)
        application.setStyleSheet(styleStream.readAll())

    application_window: MainWindow = MainWindow()
    application_window.show()
    sys.exit(application.exec())