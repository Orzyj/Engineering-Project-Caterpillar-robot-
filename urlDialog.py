from PyQt6.QtWidgets import QDialog
from PyQt6.QtCore import QUrl
from urlDialog_ui import Ui_DialogURL


class urlDialog(QDialog):
    def __init__(self, url: str = ""):
        super().__init__()
        self.ui: Ui_DialogURL = Ui_DialogURL()
        self.ui.setupUi(self)
        self.__url: str = url
        self.__status: bool = None

        self.__initBaseConfiguration()
        self.ui.buttonBox.accepted.connect(lambda: self.__handlingInput())
        self.ui.buttonBox.rejected.connect(lambda: self.reject())

    def __initBaseConfiguration(self) -> None:
        self.ui.leAdress.setText(self.__url)

    def __handlingInput(self) -> None:
        ulr: str = self.ui.leAdress.text()

        if ulr.strip() != "":
            self.__status = True
            self.__url = ulr
        else:
            self.__status = False

        self.accept()

    def getUrl(self) -> QUrl:
        return QUrl(self.__url)
    
    def getTextUrl(self) -> str:
        return self.ui.leAdress.text()
    
    def getStatus(self) -> bool:
        return self.__status
