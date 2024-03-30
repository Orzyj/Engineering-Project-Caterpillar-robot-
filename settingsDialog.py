from PyQt6.QtWidgets import QDialog
from settingsDialog_ui import * 

class SettingsDialog(QDialog):
    def __init__(self, ip: str, port: int):
        super().__init__()
        self.ui: Ui_Dialog = Ui_Dialog()
        self.ui.setupUi(self)
        self._ip: str = ip
        self._port: int = port
        self._status: bool = False

        self._initBaseConfiguration()
        self.ui.buttonBox.accepted.connect(lambda: self._validateInput())

    def _initBaseConfiguration(self) -> None:
        self.ui.leIP.setText(self._ip)
        self.ui.lePort.setText(str(self._port))

    def _validateInput(self) -> None:
        ip = self.ui.leIP.text()
        port = self.ui.lePort.text()
        
        if ip.strip() == "" or port.strip() == "":
            self._status = False
        else:
            self._ip = self.ui.leIP.text()
            self._port = int(self.ui.lePort.text())
            self._status = True
            self.accept() 

    def getIpAddress(self) -> str:
        return self._ip
    
    def getPort(self) -> int:
        return self._port
    
    def getStatus(self) -> bool:
        return self._status