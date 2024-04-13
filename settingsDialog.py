from PyQt6.QtWidgets import QDialog
from settingsDialog_ui import * 
import re

class SettingsDialog(QDialog):
    def __init__(self, ip: str, port: int):
        super().__init__()
        self.ui: Ui_Dialog = Ui_Dialog()
        self.ui.setupUi(self)
        self.__ip: str = ip
        self.__port: int = port
        self.__status: bool = False

        self.__initBaseConfiguration()
        self.ui.buttonBox.accepted.connect(lambda: self.__validateInput())
        self.ui.buttonBox.rejected.connect(lambda: self.reject())

    def __checkIP(self, ip: str) -> bool:
        pattern: str = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
        return True if re.match(pattern, ip) else False
    
    def __chekPort(self, port: str) -> bool:
        try:
            portNumber: int = int(port)
            return True if isinstance(portNumber, int) and 0 < portNumber <= 65535 else False
        except ValueError:
            return False
        
    def __initBaseConfiguration(self) -> None:
        self.ui.leIP.setText(self.__ip)
        self.ui.lePort.setText(str(self.__port))

    def __validateInput(self) -> None:
        ip: str = self.ui.leIP.text()
        port: int = self.ui.lePort.text()
        
        if ip.strip() == "" or port.strip() == "":
            self.__status = False

        if self.__checkIP(ip) and self.__chekPort(port):
            self.__ip = ip
            self.__port = int(port)
            self.__status = True
        else: 
            self.__status = False
            
        self.accept() 

    def getIpAddress(self) -> str:
        return self.__ip
    
    def getPort(self) -> int:
        return self.__port
    
    def getStatus(self) -> bool:
        return self.__status