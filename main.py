import os, sys
from PySide6.QtWidgets import QApplication
from Core.main_window import MainWindow
from Core.script_placer import ScriptPlacer
from Utils.qt_utility import displayMessageBox

class Entry:

    @classmethod
    def init(cls):
        
        # Initialize main window
        cls.mainWindow = MainWindow()

        # if running via exe, then sure program is in the correct (waw) directory
        # check if running via exe
        is_executable = getattr(sys, 'frozen', False)
        if is_executable:
            if not r'SteamLibrary\steamapps\common\Call of Duty World at War' in os.getcwd():
                displayMessageBox("Error, Please run this program from the Call of Duty: World at War steam directory")
                sys.exit(0)

        # Initialize script placer
        cls.scriptPlacer = ScriptPlacer(cls.mainWindow)

        # Show main window
        cls.mainWindow.show()

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        entry = Entry()
        entry.init()
        sys.exit(app.exec())
    except Exception as e:
        print(e)