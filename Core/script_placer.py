import os, sys, shutil
from PySide6.QtCore import QThread, Signal, QTimer
from Utils.py_utility import getBasePath
from Utils.qt_utility import displayMessageBox

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
            with open("error_log.txt", "a") as f:
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
        # zm is the only mode available
        mode = "zm"

        # get base path (for executable or script)
        base_path = getBasePath()

        # check if the mod already exists
        if os.path.exists(os.path.join(base_path, "mods", modName)):
            displayMessageBox(f"Error, {modName} already exists")
            return
        
        # copy the files
        self.copyFiles(base_path, modName, mapName, mode)
    
    def copyFiles(self, base_path, modName, mapName, mode):
        # Specify your directory relative to the base path
        template_files_dir = os.path.join(base_path, "stock_base_files", mapName)
        print(template_files_dir)
        
        # Check if the source directory exists
        if not os.path.exists(template_files_dir):
            displayMessageBox(f"Source directory does not exist: {template_files_dir}")
            return

        # Define the destination directory
        destination_dir = os.path.join(base_path, "mods", modName)
        
        # Create the destination directory if it doesn't exist
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
