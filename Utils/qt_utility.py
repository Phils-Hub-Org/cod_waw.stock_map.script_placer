from PySide6.QtWidgets import QApplication, QMessageBox

def displayMessageBox(message: str, x: int = 100, y: int = None) -> None:
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setWindowTitle("Information")
    msgBox.setText(message)
    msgBox.setStandardButtons(QMessageBox.Ok)
    
    if y is None:
        # Get screen geometry and center vertically
        _, screenHeight = getScreenDimms()
        msgBox_height = msgBox.sizeHint().height()
        y = (screenHeight - msgBox_height) // 2  # Vertically center
    
    msgBox.move(x, y)  # Set position
    
    msgBox.exec()

def displayYesNoMessageBox(message: str) -> bool:
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Question)
    msgBox.setWindowTitle("Confirmation")
    msgBox.setText(message)
    msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    msgBox.setDefaultButton(QMessageBox.No)
    result = msgBox.exec()
    return result == QMessageBox.Yes

def getScreenDimms() -> tuple[int, int]:
    screen = QApplication.primaryScreen()
    screenGeometry = screen.geometry()

    screenWidth = screenGeometry.width()
    screenHeight = screenGeometry.height()

    return screenWidth, screenHeight