import os, logging
from PySide6.QtCore import QTimer, Slot
import Utils.qt_utility as QtUtility
from Core.script_placer_worker import FileCopyWorker

logger = logging.getLogger(__name__)

class ScriptPlacer:
    def __init__(self, mainWindow, currentWorkingDir, wawRootDir) -> None:
        self.mainWindow = mainWindow
        self.currentWorkingDir = currentWorkingDir
        self.wawRootDir = wawRootDir

        self.warningOrErrorOccuredDuringBuild = False
        self.warningOrErrorLogs = []

        from Resources.UI.ui_main_window import Ui_MainWindow
        self.ui: Ui_MainWindow = self.mainWindow.ui

        from Core.console import Console
        self.console = Console()
        self.console.ui.close_console_btn.hide()  # only show when an error
        self.console.ui.close_console_btn.clicked.connect(self.hideConsole)

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
                "nazi_zombie_prototype": self.ui.zm_prototype_cbox,
                "nazi_zombie_asylum": self.ui.zm_asylum_cbox,
                "nazi_zombie_sumpf": self.ui.zm_sumpf_cbox,
                "nazi_zombie_factory": self.ui.zm_factory_cbox
            }
        }

        self.ui.submit_btn.clicked.connect(self.createMod)

    def createMod(self):
        # ensure wawRootDir is valid
        if not os.path.exists(self.wawRootDir):
            logger.debug(f"wawRootDir: '{self.wawRootDir}' does not exist")
            return        
        
        try:
            modName, mapName, mode = self.verifyInputs()
        except Exception:
            return
        
        # get the template files directory
        templateFilesRoot = os.path.join(self.currentWorkingDir, 'Phils-Hub',  'Stock-Map Script-Placer')
        if not os.path.exists(templateFilesRoot):
            os.makedirs(templateFilesRoot)
        
        # join the template files root directory with the assets directory
        templateFilesDir = os.path.join(templateFilesRoot, 'Stock Base Files', mode, mapName)
        if not os.path.exists(templateFilesDir):
            QtUtility.displayMessageBox(f"Error, The template files directory\n{templateFilesDir}\ndoes not exist")
            return

        modDir = os.path.join(self.wawRootDir, 'mods', modName)
        if not os.path.exists(modDir):
            os.makedirs(modDir)

        # disable the submit button
        self.ui.submit_btn.setEnabled(False)

        # in-case user didn't prev close the console (only possible if there was an error)
        self.warningOrErrorOccuredDuringBuild = False
        self.warningOrErrorLogs.clear()
        self.console.ui.console.clear()
        self.console.ui.close_console_btn.hide()

        self.initWorker(templateFilesDir, modDir, modName, mapName, mode)
    
    def verifyInputs(self):
        modName = self.ui.mod_name_input.text()
        if modName == "":
            self.updateStatusBar('Warning, Please enter a mod name')
            raise Exception
        
        if os.path.exists(os.path.join(self.wawRootDir, "mods", modName)):
            self.updateStatusBar(f'Warning, {modName} already exists')
            raise Exception
                    
        if not self.isAnyCheckboxChecked():
            self.updateStatusBar('Warning, Please select at least one map')
            raise Exception

        if not self.isOnlyOneCheckboxChecked():
            self.updateStatusBar('Warning, Please select only one map')
            raise Exception

        mode = self.getSelectedCheckboxMode()
        if mode is None:
            logger.error(f"Error, You should never see this message [getSelectedCheckboxMode]")
            QtUtility.displayMessageBox(f"Error, You should never see this message [getSelectedCheckboxMode]")
            raise Exception

        # get the selected map
        mapName = self.getSelectedCheckboxMap()
        if mapName is None:
            logger.error(f"Error, You should never see this message [getSelectedCheckboxMap]")
            QtUtility.displayMessageBox(f"Error, You should never see this message [getSelectedCheckboxMap]")
            raise Exception
        
        return modName, mapName, mode
    
    def isAnyCheckboxChecked(self) -> bool:
        # Iterate over all checkboxes in the nested dictionaries
        for category in self.optionsWidgets.values():
            for checkbox in category.values():
                if checkbox.isChecked():
                    return True
        return False
    
    def isOnlyOneCheckboxChecked(self) -> bool:
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
    
    def getSelectedCheckboxMode(self) -> str:
        # Iterate over all checkboxes to find the checked one
        for mode, category in self.optionsWidgets.items():
            for _, checkbox in category.items():
                if checkbox.isChecked():
                    return mode  # Return the mode of the checked checkbox

        return None  # Fallback, should not be reached if the previous check is correct
    
    def getSelectedCheckboxMap(self) -> str:
        # Iterate over all checkboxes to find the checked one
        for category in self.optionsWidgets.values():
            for checkbox_name, checkbox in category.items():
                if checkbox.isChecked():
                    return checkbox_name  # Return the name of the checked checkbox

        return None  # Fallback, should not be reached if the previous check is correct

    def initWorker(self, templateFilesDir, modDir, modName, mapName, mode):
        # get this check out of the way now to preven multiple builds
        self.createShortcut = self.ui.shortcut_cbox.isChecked()
        self.runExecutable = self.ui.run_map_cbox.isChecked()
        self.insertIngamePrintMsg = self.ui.insert_ingame_print_msg_cbox.isChecked()

        # Use shutil.copytree to copy the folder and its contents
        # Create and start the worker thread
        self.copy_worker = FileCopyWorker(
            wawRootDir=self.wawRootDir,
            src=templateFilesDir, dest=modDir,
            modName=modName, mapName=mapName, mode=mode,
            create_shortcut=self.createShortcut,
            insert_ingame_print_msg=self.insertIngamePrintMsg,
            build_mod=self.ui.build_mod_cbox.isChecked(),
            run_executable=self.runExecutable
        
        )
        # Connect signals and slots
        self.copy_worker.show_console.connect(self.showConsole)
        self.copy_worker.update_status_bar.connect(self.updateStatusBar)
        self.copy_worker.send_display_message_box_message.connect(self.sendDisplayMessageBoxMessage)
        self.copy_worker.finished.connect(self.onWorkerFinished)

        # mod.ff & iwd
        self.copy_worker.build_output_handle.connect(self.buildOutputHandleSlot)
        # self.copy_worker.build_interrupted_handle.connect(self.buildInterruptedHandleSlot)  # this feature is not required for this app.
        
        # mod.ff
        self.copy_worker.build_output_warning_handle.connect(self.buildModFFWarningOutputHandleSlot)
        self.copy_worker.build_output_error_handle.connect(self.buildModFFErrorOutputHandleSlot)
        self.copy_worker.build_modff_success_handle.connect(self.buildModFFSuccessHandleSlot)
        self.copy_worker.build_modff_failure_handle.connect(self.buildModFFFailureHandleSlot)
        
        # iwd
        self.copy_worker.build_iwd_success_handle.connect(self.buildIWDSuccessHandleSlot)
        self.copy_worker.build_iwd_failure_handle.connect(self.buildIWDFailureHandleSlot)

        self.copy_worker.start()

    @Slot(bool)
    def showConsole(self) -> None:
        self.console.show()
    
    @Slot()
    def hideConsole(self) -> None:
        self.console.ui.console.clear()
        self.console.hide()
        self.warningOrErrorOccuredDuringBuild = False
        self.warningOrErrorLogs.clear()
    
    @Slot(str, int)
    def updateStatusBar(self, message, delay=3000) -> None:
        self.ui.statusBar.showMessage(message, delay)
    
    @Slot(str)
    def sendDisplayMessageBoxMessage(self, message: str) -> None:
        QtUtility.displayMessageBox(message)

    # mod.ff & iwd
    @Slot(str)
    def buildOutputHandleSlot(self, message: str) -> None:
        self.console.ui.console.appendPlainText(message)
    
    # @Slot(str)
    # def buildInterruptedHandleSlot(self, message: str) -> None:
    #     print(f'On process interrupted: {message}')
    
    # mod.ff
    @Slot(str)
    def buildModFFWarningOutputHandleSlot(self, message: str) -> None:
        self.updateStatusBar('WARNING occured during modff build')
        self.warningOrErrorOccuredDuringBuild = True
        self.warningOrErrorLogs.append(message)
    
    @Slot(str)
    def buildModFFErrorOutputHandleSlot(self, message: str) -> None:
        self.updateStatusBar('ERROR occured during modff build')
        self.warningOrErrorOccuredDuringBuild = True
        self.warningOrErrorLogs.append(message)
    
    @Slot(str)
    def buildModFFSuccessHandleSlot(self, message: str) -> None:
        # self.updateStatusBar(message, 25)
        logger.debug(f'On build modff success: {message}')  # 'All steps completed successfully'
    
    @Slot(str)
    def buildModFFFailureHandleSlot(self, message: str) -> None:
        logger.info(f'On build modff failure: {message}')
    
    # iwd
    @Slot(str)
    def buildIWDSuccessHandleSlot(self, message: str) -> None:
        # self.updateStatusBar(message, 25)
        logger.debug(f'On build iwd success: {message}')  # 'All steps completed successfully'
    
    @Slot(str)
    def buildIWDFailureHandleSlot(self, message: str) -> None:
        logger.info(f'On build iwd failure: {message}')

    @Slot(bool, str)
    def onWorkerFinished(self, result, message) -> None:
        delay = 5000

        if result:
            self.updateStatusBar(message, delay)
            
            if self.warningOrErrorOccuredDuringBuild:
                self.console.ui.console.appendPlainText('\n/************** Here is the list of warnings/errors. *****************/')
                self.console.ui.console.appendPlainText('\n'.join(self.warningOrErrorLogs))
                self.console.ui.close_console_btn.show()
            else:
                self.console.ui.console.clear()
                self.console.hide()

            # scroll to the bottom, sometimes it doesnt do it fully automatically
            self.console.ui.console.verticalScrollBar().setValue(self.console.ui.console.verticalScrollBar().maximum() + 100)
        else:
            QtUtility.displayMessageBox(message)
        
        # if failure, the displayMessageBox is blocking, so have the mod creation delay start after the messageBox has been closed.
        QTimer.singleShot(delay, lambda: self.ui.submit_btn.setEnabled(True))
