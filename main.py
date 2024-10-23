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
    log_file_path = os.path.join(os.getcwd(), 'Phils-Hub', 'Logs', 'code waw stock map script placer.log')  # the file handler does not like hyphens, forward slashes, etc.

    # Create the log directory if it doesn't exist
    if not os.path.exists(os.path.dirname(log_file_path)):
        os.makedirs(os.path.dirname(log_file_path))

    # Configure logging
    logging.basicConfig(
        level=logging.DEBUG if ENV == 'DEV' else logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            # set file handler based on environment
            # FileHandler | keeps storing the logs forever
            # RotatingFileHandler | keeps up to 5 logs of size 5MB
            logging.FileHandler(log_file_path) if ENV == 'DEV' else RotatingFileHandler(log_file_path, maxBytes=5*1024*1024, backupCount=1),
            # The StreamHandler is used to output log messages to a specific output stream.
            # By default, it outputs to sys.stderr, but you can direct it to other streams, like sys.stdout, or even to custom file-like objects.
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
    except KeyboardInterrupt:
        logging.info("Application closed by user.")
    except Exception as e:
        logging.exception("An error occurred: %s", e)
