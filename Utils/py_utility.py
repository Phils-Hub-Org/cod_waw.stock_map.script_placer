import os, sys, subprocess
from win32com.client import Dispatch
from typing import Union

def isExecutable() -> bool:
    return getattr(sys, 'frozen', False)

def createShortcut(target: str, shortcut_dest: str, icon_path: str = None, args: str = None, start_in: str = None) -> None:
    """Create a shortcut to a target file with optional arguments and start-in path."""
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_dest)
    shortcut.TargetPath = target
    if args:
        shortcut.Arguments = args
    if icon_path:
        shortcut.IconLocation = icon_path
    if start_in:
        shortcut.WorkingDirectory = start_in  # Set the "Start In" directory
    shortcut.save()

def runExecutable(running_dir: str, exe_path: str, exe_args: str) -> Union[bool, str]:
    """
    Runs the given executable with no arguments.
    exe_path: Path to the executable file
    """

    os.chdir(running_dir)  # required

    try:
        subprocess.Popen(
            [exe_path, exe_args],
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
        return True, f"Successfully ran {exe_path}"
    except subprocess.CalledProcessError as e:
        return False, f"Error occurred while running {exe_path}: {e}"
    except FileNotFoundError:
        return False, f"Executable not found: {exe_path}"

if __name__ == "__main__":
    print(isExecutable())