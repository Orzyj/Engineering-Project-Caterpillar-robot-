from PyQt6.QtWidgets import QPushButton, QDialog, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView
from urlDialog import urlDialog


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

        webEngineLayout: QVBoxLayout = QVBoxLayout()
        self.__webEngineView: QWebEngineView = QWebEngineView()
        webEngineLayout.addWidget(self.__webEngineView)
        webEngineLayout.setContentsMargins(0, 0, 0, 0) 

        mainLayout: QVBoxLayout = QVBoxLayout()
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