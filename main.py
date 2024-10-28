import os, sys, logging
from logging.handlers import RotatingFileHandler
from PySide6.QtWidgets import QApplication
import Utils.py_utility as PyUtility
import Utils.qt_utility as QtUtility

ENV = 'PROD' if PyUtility.isExecutable() else 'DEV'

# Dynamically determine where the Phils-Hub folder should be created.
if PyUtility.isExecutable():
    # if not exe, then the template files are in cwd (vscode proj dir), and obv the dest for said files is still waw dir.
    # so place the Stock Base Files folder in your working dir, run program, try to create a mod, it will inform you of missing dir, but it will create a Phils-Hub dir in the working dir, so then navigate to Stock-Map Script-Placer and place the Stock Base Files folder in there. now you can create a mod.
    currentWorkingDir = os.getcwd()
    wawRootDir = currentWorkingDir
else:
    # when pkg'd into an exe, run exe, it prompts u of dir, it creates phils-hub dir, you place folder, done. same as above reli, we just switch between where the phils-hub dir is created. this is for automatic dev/prod env changes ofc.
    currentWorkingDir = os.getcwd()
    # set YOUR waw root directory here
    wawRootDir = r'D:\SteamLibrary\steamapps\common\Call of Duty World at War'

def setupLogging() -> None:
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
    def init(cls) -> None:
        
        # Initialize main window
        from Core.main_window import MainWindow
        cls.mainWindow = MainWindow()

        # Display environment status
        logging.info(f'Running in {ENV} mode')

        # if running via exe, then ensure program is in the correct (waw) directory
        if PyUtility.isExecutable():
            if not r'SteamLibrary\steamapps\common\Call of Duty World at War' in os.getcwd():
                QtUtility.displayMessageBox("Error, Please run this program from the Call of Duty: World at War steam directory")
                sys.exit(0)

        # Initialize script placer
        from Core.script_placer import ScriptPlacer
        cls.scriptPlacer = ScriptPlacer(cls.mainWindow, currentWorkingDir, wawRootDir)

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
        logging.exception(f"An error occurred: {e}")
