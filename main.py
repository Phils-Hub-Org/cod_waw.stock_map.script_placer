import os, sys, logging
from logging.handlers import RotatingFileHandler
from PySide6.QtWidgets import QApplication
from Core.main_window import MainWindow
from Core.script_placer import ScriptPlacer
from Utils.py_utility import isExecutable
from Utils.qt_utility import displayMessageBox

ENV = 'PROD' if isExecutable() else 'DEV'

def setupLogging():
    # Set up the log file path
    log_file_path = os.path.join(os.getcwd(), 'Phils-Hub', 'Logs', 'stock-map script-placer.log')

    # Create the log directory if it doesn't exist
    if not os.path.exists(os.path.dirname(log_file_path)):
        os.makedirs(os.path.dirname(log_file_path))

    # Configure logging
    logging.basicConfig(
        level=logging.DEBUG if ENV == 'DEV' else logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            # non-rotating | will keep storing the logs forever
            # logging.FileHandler(log_file_path),

            # rotating | is set to keep storing the logs in the same file with a maximum size of 5MB
            # RotatingFileHandler(log_file_path, maxBytes=5*1024*1024, backupCount=5),

            # non-rotating / rotating, based on environment
            logging.FileHandler(log_file_path) if ENV == 'DEV' else RotatingFileHandler(log_file_path, maxBytes=5*1024*1024, backupCount=1),
            logging.StreamHandler()
        ]
    )

class Entry:

    @classmethod
    def init(cls):
        
        # Initialize main window
        cls.mainWindow = MainWindow()

        # Display environment status
        logging.info(f'Running in {ENV} mode')

        # if running via exe, then ensure program is in the correct (waw) directory
        if isExecutable():
            if not r'SteamLibrary\steamapps\common\Call of Duty World at War' in os.getcwd():
                displayMessageBox("Error, Please run this program from the Call of Duty: World at War steam directory")
                sys.exit(0)

        # Initialize script placer
        cls.scriptPlacer = ScriptPlacer(cls.mainWindow)

        # Show main window
        cls.mainWindow.show()

if __name__ == "__main__":
    try:
        setupLogging()
        app = QApplication(sys.argv)
        entry = Entry()
        entry.init()
        sys.exit(app.exec())
    except Exception as e:
        logging.exception(e)