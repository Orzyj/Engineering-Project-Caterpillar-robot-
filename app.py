from PyQt6.QtGui import QCloseEvent
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QPushButton, QDialog
from PyQt6.QtCore import Qt, QFile, QTextStream
from overrides import override
from interface_ui import *
from CameraLayout import *
from settingsDialog import SettingsDialog
import sys
import json
import threading
import socket
import json

class DataSenderThread(threading.Thread):
    def __init__(self, json_data, address, port):
        super().__init__()
        self.json_data = json_data
        self.address = address
        self.port = port

    @override()
    def run(self) -> None:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((self.address, self.port))
                json_string = json.dumps(self.json_data)
                sock.sendall(json_string.encode("utf-8"))
                print(f"Wysłano\n{json_string}")
        except Exception as e:
            print("Error:", e)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__address_ip_rasberry: str = "192.168.1.39"
        self.__port: int = 5000
        self.__json_data: json = json.load(open("resources/settings.json", 'r'))
        self.__pressed_keys: set = set()
        self.__sender_thread: DataSenderThread = DataSenderThread(self.__json_data, self.__address_ip_rasberry, 6000)

        self.ui: Ui_MainWindow = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__initBaseConfigurationLayout()
        self.__initCameraLayout()
        self.__settingConnections()

    @override()
    def keyPressEvent(self, event) -> None:
        key: Qt.Key = event.key()
        
        if key == Qt.Key.Key_W:
            self.__pressed_keys.add(Qt.Key.Key_W)
        elif key == Qt.Key.Key_S:
            self.__pressed_keys.add(Qt.Key.Key_S)
        elif key == Qt.Key.Key_D:
            self.__pressed_keys.add(Qt.Key.Key_D)
        elif key == Qt.Key.Key_A:
            self.__pressed_keys.add(Qt.Key.Key_A)
        elif key == Qt.Key.Key_Tab:
            self.ui.icon_only_widget.setVisible(not self.ui.icon_only_widget.isVisible())
            self.ui.full_menu_widget.setHidden(not self.ui.full_menu_widget.isHidden())

        self.update_movements()

    @override()
    def keyReleaseEvent(self, event) -> None:
        key: Qt.Key = event.key()

        if key in self.__pressed_keys:
            self.__pressed_keys.remove(key)

        self.update_movements() 

    @override()
    def closeEvent(self, a0: QCloseEvent | None) -> None:
        return super().closeEvent(a0)

    def send_data_to_server(self):
        if not self.__sender_thread.is_alive():
            self.__sender_thread = DataSenderThread(self.__json_data, self.__address_ip_rasberry, 6000)
            self.__sender_thread.start()

    def update_movements(self) -> None:
        for key in self.__pressed_keys:
            self.__json_data["movements"]["UP"] = (True if key == Qt.Key.Key_W else False) 
            self.__json_data["movements"]["DOWN"] = (True if key == Qt.Key.Key_S else False) 
            self.__json_data["movements"]["RIGHT"] = (True if key == Qt.Key.Key_D else False) 
            self.__json_data["movements"]["LEFT"] = (True if key == Qt.Key.Key_A else False) 

        if not any(self.__pressed_keys):
            self.__json_data["movements"]["UP"] = False 
            self.__json_data["movements"]["DOWN"] = False
            self.__json_data["movements"]["RIGHT"] = False
            self.__json_data["movements"]["LEFT"] = False

        self.send_data_to_server() 

    def __toggleCameraPowerState(self) -> None:
        state: bool = self.ui.chkBoxCameraEnable.isChecked()
        self.__json_data["camera"]["POWER"] = state

    def __initCameraLayout(self) -> None:
        cameraLayout: CameraLayout = CameraLayout(self.__address_ip_rasberry, self.__port)
        self.ui.cameraGroupBox.setLayout(cameraLayout)

    def __onChangePowerConsumtion(self) -> None:
        value: int = self.ui.hsEnginePowerConsumtion.value()
        self.__json_data["movements"]["POWER"] = value

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
        self.ui.btnExit1.clicked.connect(QApplication.quit)
        self.ui.btnExit2.clicked.connect(QApplication.quit)
        self.ui.btnSearch.clicked.connect(self.__onSearchButtonClicked)
        self.ui.btnChangeSettings.clicked.connect(self.__onChangeSettings)
        self.ui.btnSettings.clicked.connect(self.__onChangeSettings)

        self.ui.btnForward.pressed.connect(self.__onChangeDirection)
        self.ui.btnRight.pressed.connect(self.__onChangeDirection)
        self.ui.btnBackward.pressed.connect(self.__onChangeDirection)
        self.ui.btnLeft.pressed.connect(self.__onChangeDirection)
        self.ui.btnForward.released.connect(self.__stopMovement)
        self.ui.btnRight.released.connect(self.__stopMovement)
        self.ui.btnBackward.released.connect(self.__stopMovement)
        self.ui.btnLeft.released.connect(self.__stopMovement)
        self.ui.chkBoxCameraEnable.stateChanged.connect(self.__toggleCameraPowerState)
        self.ui.hsEnginePowerConsumtion.valueChanged.connect(self.__onChangePowerConsumtion)

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

    def __onChangeDirection(self) -> None:
        button: QPushButton = self.sender()

        if button is self.ui.btnForward:
            self.__json_data["movements"]["UP"] = True
        elif button is self.ui.btnBackward:
            self.__json_data["movements"]["DOWN"] = True
        elif button is self.ui.btnRight:
            self.__json_data["movements"]["RIGHT"] = True
        elif button is self.ui.btnLeft:
            self.__json_data["movements"]["LEFT"] = True

        print(f"{self.__json_data}")
        self.send_data_to_server()

    def __stopMovement(self) -> None:
        self.__json_data["movements"]["UP"] = False
        self.__json_data["movements"]["DOWN"] = False
        self.__json_data["movements"]["LEFT"] = False
        self.__json_data["movements"]["RIGHT"] = False
    

if __name__ == "__main__":
    application: QApplication = QApplication(sys.argv)
    styleFile: QFile = QFile("layouts/mainLayout.qss")

    if styleFile.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):
        styleStream: QTextStream = QTextStream(styleFile)
        application.setStyleSheet(styleStream.readAll())

    application_window: MainWindow = MainWindow()
    application_window.show()
    sys.exit(application.exec())