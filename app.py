from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QPushButton, QDialog
from PyQt6.QtCore import Qt, QFile, QTextStream
from overrides import override
from interface_ui import *
from settingsDialog import SettingsDialog
import sys
import json

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__address_ip_rasberry: str = "192.168.1.39"
        self.__port: int = 30000
        self.__json_data: json = json.load(open("resources/settings.json", 'r'))

        self.ui: Ui_MainWindow = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__initBaseConfigurationLayout()
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

    def __onSearchButtonClicked(self) -> None :
        self.ui.stackedWidget.setCurrentIndex(5)
        searchText: str = self.ui.leSearch.text().strip()

        if searchText:
            for index in range(self.ui.stackedWidget.count()):
                currentWidget = self.ui.stackedWidget.widget(index)
                pass  #dokończyć wyszukiwanie

        if len(searchText) == 0:
            msgBox: QMessageBox = QMessageBox()
            style: QFile = QFile("layouts/msgBoxLayout.qss")
            streamStyle: QTextStream = None

            msgBox.setWindowTitle("Informacja")
            msgBox.setText("Brak tekstu w polu wyszukiwania!")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            
            if style.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):
                streamStyle: QTextStream = QTextStream(style)
                msgBox.setStyleSheet(streamStyle.readAll())

            msgBox.exec()

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