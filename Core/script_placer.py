import os, shutil, logging
from PySide6.QtCore import QThread, Signal, QTimer
from Utils.py_utility import isExecutable, getTempUnpackPath
from Utils.qt_utility import displayMessageBox

logger = logging.getLogger(__name__)

class FileCopyWorker(QThread):
    # Define a signal that emits when copying is done
    finished = Signal(str)

    def __init__(self, src, dest, modName, mapName, mode):
        super().__init__()
        self.src = src
        self.dest = dest
        self.modName = modName
        self.mapName = mapName
        self.mode = mode

    def run(self):
        try:
            shutil.copytree(self.src, self.dest, dirs_exist_ok=True)
            self.finished.emit(f"Successfully created {self.modName} for {self.mapName} on {self.mode}")
        except Exception as err:
            self.finished.emit(f"Error occurred. Check error_log.txt for more details.")
            with open(os.path.join(os.getcwd(), 'error_log.txt'), 'a') as f:
                f.write(f"Error creating {self.modName} for {self.mapName} on {self.mode}:\nError: {err}\n")

class ScriptPlacer:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow

        from Resources.UI.ui_main_window import Ui_MainWindow
        self.ui: Ui_MainWindow = self.mainWindow.ui

        self.optionsWidgets = {
            "prototype": self.ui.zm_prototype_cbox,
            "asylum": self.ui.zm_asylum_cbox,
            "sumpf": self.ui.zm_sumpf_cbox,
            "factory": self.ui.zm_factory_cbox
        }

        self.ui.submit_btn.clicked.connect(self.createMod)
    
    def createMod(self):
        modName = self.ui.mod_name_input.text()
        if modName == "":
            displayMessageBox("Error, Please enter a mod name")
            return
                    
        # check if at least one option is selected
        if not any(cboxWidget.isChecked() for cboxWidget in self.optionsWidgets.values()):
            displayMessageBox(f"Error, Please select at least one map")
            return
        
        # ensure only one option is selected
        selectedOptions = [mapName for mapName, cboxWidget in self.optionsWidgets.items() if cboxWidget.isChecked()]
        if len(selectedOptions) > 1:
            displayMessageBox(f"Error, Please select only one map")
            return

        # get the selected map
        mapName = selectedOptions[0]

        # get the selected mode
        # zm is the only mode available atm
        mode = "zm"

        # check if the mod already exists
        # get the waw root directory
        # so if dev, e.g. vscode, then we'll explicitly set the base path
        # if not, then we'll use the current working directory since in main.py we ensure that we're in the correct directory when running via exe
        if isExecutable():
            waw_root = os.getcwd()
        else:
            # set YOUR waw root directory here
            waw_root = r'D:\SteamLibrary\steamapps\common\Call of Duty World at War'
        
        logger.debug(f'waw_root: {waw_root}')
        
        if not os.path.exists(waw_root):
            logger.debug(f'waw_root: {waw_root} does not exist')
            return

        # check if the mod already exists
        if os.path.exists(os.path.join(waw_root, "mods", modName)):
            displayMessageBox(f"Error, {modName} already exists")
            return
        
        # copy the files
        self.copyFiles(waw_root, modName, mapName, mode)
    
    def copyFiles(self, waw_root, modName, mapName, mode):
        # get the template files directory
        template_files_root = os.path.join(os.getcwd(), 'Phils-Hub',  'Stock-Map Script-Placer')

        logger.debug(f'template_files_root: {template_files_root}')

        # if the template files directory doesn't exist, create it
        if not os.path.exists(template_files_root):
            os.makedirs(template_files_root, exist_ok=True)
        
        # join the template files root directory with the assets directory
        template_files_dir = os.path.join(template_files_root, 'Stock Base Files', mapName)

        logger.debug(f'template_files_dir: {template_files_dir}')
        
        # Check if the template files directory exists
        # If you see this, then 
        if not os.path.exists(template_files_dir):
            displayMessageBox(f"Error, The template files directory\n{template_files_dir}\ndoes not exist")
            return

        # Define the destination root
        destination_root = os.path.join(waw_root, 'mods')
        if not os.path.exists(destination_root):
            os.makedirs(destination_root, exist_ok=True)

        # Define the destination directory
        destination_dir = os.path.join(destination_root, modName)
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir, exist_ok=True)

        # Copy the entire directory
        try:
            # disable the submit button
            self.ui.submit_btn.setEnabled(False)

            # Use shutil.copytree to copy the folder and its contents
            # Create and start the worker thread
            self.copy_worker = FileCopyWorker(template_files_dir, destination_dir, modName, mapName, mode)
            self.copy_worker.finished.connect(self.updateStatusMessage)  # Connect signal to the slot
            self.copy_worker.start()
        except Exception as e:
            displayMessageBox(f"Error copying directory: {e}")
    
    def updateStatusMessage(self, message):
        delay = 5000

        # Update the status bar
        self.ui.statusBar.showMessage(message, delay)
        
        # enable the submit button
        QTimer.singleShot(delay, lambda: self.ui.submit_btn.setEnabled(True))
