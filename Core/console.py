from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from Resources.UI.ui_console import Ui_ConsoleWidget

class Console(QWidget):

    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = Ui_ConsoleWidget()
        self.ui.setupUi(self)
        