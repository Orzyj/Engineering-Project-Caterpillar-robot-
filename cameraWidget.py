from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import Qt

class CameraWidget(QWidget):
    def __init__(self):
        self.__webEngineView: QWebEngineView = QWebEngineView()
        self.__source: str = None
        layout: QVBoxLayout = QVBoxLayout()

        layout.addWidget(self.__webEngineView)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)
    