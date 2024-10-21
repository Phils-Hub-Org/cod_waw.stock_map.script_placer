from PySide6.QtWidgets import QApplication
from Core.main_window import MainWindow
from Core.script_placer import ScriptPlacer

class Entry:

    @classmethod
    def init(cls):
        
        # Initialize main window
        cls.mainWindow = MainWindow()

        # Initialize script placer
        cls.scriptPlacer = ScriptPlacer(cls.mainWindow)

        # Show main window
        cls.mainWindow.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    entry = Entry()
    entry.init()
    sys.exit(app.exec())