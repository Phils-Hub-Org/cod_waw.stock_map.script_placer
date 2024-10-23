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
            'sp': {
                "ber1": self.ui.sp_ber1_cbox,
                "ber2": self.ui.sp_ber2_cbox,
                "ber3": self.ui.sp_ber3_cbox,
                "ber3b": self.ui.sp_ber3b_cbox,
                "mak": self.ui.sp_mak_cbox,
                "oki2": self.ui.sp_oki2_cbox,
                "oki3": self.ui.sp_oki3_cbox,
                "pby_fly": self.ui.sp_pby_fly_cbox,
                "pel1": self.ui.sp_pel1_cbox,
                "pel1a": self.ui.sp_pel1a_cbox,  # ff extractor has failed to extract the files
                "pel1b": self.ui.sp_pel1b_cbox,
                "pel2": self.ui.sp_pel2_cbox,
                "see1": self.ui.sp_see1_cbox,
                "see2": self.ui.sp_see2_cbox,
                "sniper": self.ui.sp_sniper_cbox
            },
            'mp': {
                "mp_airfield": self.ui.mp_airfield_cbox,
                "mp_asylum": self.ui.mp_asylum_cbox,
                "mp_bgate": self.ui.mp_bgate_cbox,
                "mp_castle": self.ui.mp_castle_cbox,
                "mp_courtyard": self.ui.mp_courtyard_cbox,
                "mp_docks": self.ui.mp_docks_cbox,
                "mp_dome": self.ui.mp_dome_cbox,
                "mp_downfall": self.ui.mp_downfall_cbox,
                "mp_drum": self.ui.mp_drum_cbox,
                "mp_hangar": self.ui.mp_hangar_cbox,
                "mp_kneedeep": self.ui.mp_kneedeep_cbox,
                "mp_kwai": self.ui.mp_kwai_cbox,
                "mp_makin": self.ui.mp_makin_cbox,
                "mp_makin_day": self.ui.mp_makin_day_cbox,
                "mp_nachtfeuer": self.ui.mp_nachtfeuer_cbox,
                "mp_outskirts": self.ui.mp_outskirts_cbox,
                "mp_roundhouse": self.ui.mp_roundhouse_cbox,
                "mp_seelow": self.ui.mp_seelow_cbox,
                "mp_shrine": self.ui.mp_shrine_cbox,
                "mp_stalingrad": self.ui.mp_stalingrad_cbox,
                "mp_suburban": self.ui.mp_suburban_cbox,
                "mp_subway": self.ui.mp_subway_cbox,
                "mp_vodka": self.ui.mp_vodka_cbox
            },
            'zm': {
                "prototype": self.ui.zm_prototype_cbox,
                "asylum": self.ui.zm_asylum_cbox,
                "sumpf": self.ui.zm_sumpf_cbox,
                "factory": self.ui.zm_factory_cbox
            }
        }

        self.ui.submit_btn.clicked.connect(self.createMod)

    def createMod(self):
        modName = self.ui.mod_name_input.text()
        if modName == "":
            displayMessageBox("Error, Please enter a mod name")
            return
                    
        # check if at least one option is selected
        if not self.isAnyCheckboxChecked():
            displayMessageBox(f"Error, Please select at least one map")
            return

        
        # ensure only one option is selected
        if not self.isOnlyOneCheckboxChecked():
            displayMessageBox(f"Error, Please select only one map")
            return

        # get the selected mode
        mode = self.getSelectedCheckboxMode()
        if mode is None:
            displayMessageBox(f"Error, You should never see this message")
            return

        # get the selected map
        mapName = self.getSelectedCheckboxMap()
        if mapName is None:
            displayMessageBox(f"Error, You should never see this message")
            return

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
    
    def isAnyCheckboxChecked(self):
        # Iterate over all checkboxes in the nested dictionaries
        for category in self.optionsWidgets.values():
            for checkbox in category.values():
                if checkbox.isChecked():
                    return True
        return False
    
    def isOnlyOneCheckboxChecked(self):
        checked_cboxes = []
        
        # Iterate over all checkboxes in the nested dictionaries
        for category in self.optionsWidgets.values():
            for checkbox in category.values():
                if checkbox.isChecked():
                    checked_cboxes.append(checkbox)
                if len(checked_cboxes) > 1:
                    return False  # More than one checkbox is checked
        
        if len(checked_cboxes) == 1:
            return True  # True if exactly one checkbox is checked, otherwise False
        return False  # No checkbox is checked
    
    def getSelectedCheckboxMode(self):
        # Iterate over all checkboxes to find the checked one
        for mode, category in self.optionsWidgets.items():
            for checkbox_name, checkbox in category.items():
                if checkbox.isChecked():
                    return mode  # Return the mode of the checked checkbox

        return None  # Fallback, should not be reached if the previous check is correct
    
    def getSelectedCheckboxMap(self):
        # Iterate over all checkboxes to find the checked one
        for category in self.optionsWidgets.values():
            for checkbox_name, checkbox in category.items():
                if checkbox.isChecked():
                    return checkbox_name  # Return the name of the checked checkbox

        return None  # Fallback, should not be reached if the previous check is correct

    def copyFiles(self, waw_root, modName, mapName, mode):
        # get the template files directory
        template_files_root = os.path.join(os.getcwd(), 'Phils-Hub',  'Stock-Map Script-Placer')

        logger.debug(f'template_files_root: {template_files_root}')

        # if the template files directory doesn't exist, create it
        if not os.path.exists(template_files_root):
            os.makedirs(template_files_root, exist_ok=True)
        
        # join the template files root directory with the assets directory
        template_files_dir = os.path.join(template_files_root, 'Stock Base Files', mode, mapName)

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
