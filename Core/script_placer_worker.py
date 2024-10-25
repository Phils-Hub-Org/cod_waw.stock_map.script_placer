import os, shutil, logging, subprocess
from PySide6.QtCore import QThread, Signal
import Utils.py_utility as PyUtility
import Core.build_mod_ff as build_mod_ff
import Core.build_iwd as build_iwd

logger = logging.getLogger(__name__)

class FileCopyWorker(QThread):
    # signals
    show_console = Signal(bool)
    update_console = Signal(str)
    update_status_bar = Signal(str, int)
    finished = Signal(bool, str)

    def __init__(self, wawRootDir, src, dest, modName, mapName, mode, create_shortcut=False, build_mod=False, run_executable=False):
        super().__init__()
        self.wawRootDir = wawRootDir
        self.src = src
        self.dest = dest
        self.modName = modName
        self.mapName = mapName
        self.mode = mode
        self.create_shortcut = create_shortcut
        self.build_mod = build_mod
        self.run_executable = run_executable

    def run(self):
        try:
            self.copyFiles()
        
            if self.create_shortcut:
                self.createShortcut(self.wawRootDir)

            if self.build_mod:
                self.buildMod(printFunc=self.update_console.emit)
        
            if self.run_executable:
                # if self.create_shortcut:
                #     delay = 3000
                #     self.update_status_bar.emit('Running executable in 3 seconds', delay)
                #     QThread.msleep(delay)

                self.runExecutable()

            self.onFinished(True, f"Successfully created {self.modName} for {self.mapName} on {self.mode}")
        except subprocess.CalledProcessError as err:
            self.onFinished(False, f"An error occurred during the 'Build Mod' stage.\nError: {err}")
        except Exception as err:
            self.onFinished(False, f"An error occurred during the 'Build Mod' stage.\nError: {err}")
    
    def onFinished(self, result: bool, msg: str) -> None:
        logger.info(msg)
        self.finished.emit(result, msg)
    
    def copyFiles(self):
        shutil.copytree(self.src, self.dest, dirs_exist_ok=True)

    def createShortcut(self, wawRootDir):
        wawExeName = f'CoDWaW' if self.mode != 'mp' else 'CoDWaWmp'
        wawArgs = rf'+set fs_game mods/{self.modName} +devmap {self.mapName} +set r_fullscreen 0'
        wawPath = rf'"{wawRootDir}\{wawExeName}.exe"'  # root + exe requires to be wrapped in double quotes

        newShortcutPath = os.path.expanduser(rf'~\Desktop\{self.modName}.lnk')  # store on users desktop
        iconPath = rf'{wawRootDir}\{wawExeName}.ico'
        startInPath = wawRootDir  # "Start In" path (working directory)

        PyUtility.createShortcut(
            target=wawPath,  # this is the "Target" Path (exe > properties > shorcut tab > target path field)
            shortcut_dest=newShortcutPath,  # store shortcut on the user's desktop
            icon_path=iconPath,  # Set icon
            args=wawArgs,  # set the target path args
            start_in=startInPath  # set the "Start In" path
        )

    def buildMod(self, printFunc):
        self.show_console.emit(True)

        build_mod_ff.build(
            modDir=os.path.join(os.path.join(self.wawRootDir, 'mods'), self.modName),
            zoneSourceDir=os.path.join(self.wawRootDir, 'zone_source'),
            modName=self.modName,
            binDir=os.path.join(self.wawRootDir, 'bin'),
            zoneEnglishDir=os.path.join(self.wawRootDir, 'zone', 'english'),
            activisionModDir=os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Activision', 'CoDWaW', 'mods', self.modName),  # '~' = home dir
            printFunc=printFunc,
            addSpaceBetweenSteps=True
        )

        printFunc('\n')  # newline

        build_iwd.build(
            modName=self.modName,
            modDir=os.path.join(os.path.join(self.wawRootDir, 'mods'), self.modName),
            activisionModDir=os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Activision', 'CoDWaW', 'mods', self.modName),  # '~' = home dir
            foldersToIgnore=[
                # 'sound',  # temporary, cause theres quite a few of them, so its not ideal for debugging.
            ],
            filesToIgnore=[
                'mod.ff',
                f'{self.modName}.files',
                f'{self.modName}.iwd',
                'console.log',
            ],
            printFunc=printFunc,
            # addSpaceBetweenSteps=True
        )

    def runExecutable(self):
        dir = self.wawRootDir if not PyUtility.isExecutable() else os.getcwd()
        PyUtility.runExecutable(
            running_dir=dir,
            exe_path=os.path.join(dir, 'CoDWaW.exe'),
            exe_args=rf'+set fs_game mods/{self.modName} +devmap {self.mapName} +set r_fullscreen 0'
        )
