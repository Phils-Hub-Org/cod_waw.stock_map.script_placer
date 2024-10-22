import os, sys

def printProjectStructure(root_dir: str=os.getcwd(), files_to_ignore: list=[], folders_to_ignore: list=[], indent: int=0) -> None:
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path):
            if any(folder in item for folder in folders_to_ignore):
                continue
            print("  " * indent + f"📁 {item}")
            printProjectStructure(item_path, files_to_ignore, folders_to_ignore, indent + 1)
        else:
            if any(file_name in item for file_name in files_to_ignore):
                continue
            print("  " * indent + f"📄 {item}")

def isExecutable():
    return getattr(sys, 'frozen', False)

def getTempUnpackPath():
    # When running as an executable, PyInstaller unpacks embedded files into a temporary directory
    unpack_path = os.path.join(sys._MEIPASS)

    return unpack_path

if __name__ == "__main__":
    printProjectStructure(
        files_to_ignore=[
            '.gitattributes',
            'LICENSE',
            'README.md'
        ],
        folders_to_ignore=[
            '.git',
            '.vscode',
            'output',
            '__pycache_',
            '--archived',
            '--misc',
            'Phils-Hub',
            'Tests'
        ]
    )