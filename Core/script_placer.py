from Utils.qt_utility import displayMessageBox

class ScriptPlacer:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow

        from Resources.UI.ui_main_window import Ui_MainWindow
        self.ui: Ui_MainWindow = self.mainWindow.ui