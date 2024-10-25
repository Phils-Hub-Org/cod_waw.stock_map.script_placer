from PySide6.QtWidgets import QApplication, QMessageBox

def displayMessageBox(message: str, x: int = 100, y: int = None) -> None:
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setWindowTitle("Information")
    msg_box.setText(message)
    msg_box.setStandardButtons(QMessageBox.Ok)
    
    if y is None:
        # Get screen geometry and center vertically
        _, screenHeight = getScreenDimms()
        msg_box_height = msg_box.sizeHint().height()
        y = (screenHeight - msg_box_height) // 2  # Vertically center
    
    msg_box.move(x, y)  # Set position
    
    msg_box.exec()

def displayYesNoMessageBox(message: str) -> bool:
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Question)
    msg_box.setWindowTitle("Confirmation")
    msg_box.setText(message)
    msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    msg_box.setDefaultButton(QMessageBox.No)
    result = msg_box.exec()
    return result == QMessageBox.Yes

def getScreenDimms() -> tuple[int, int]:
    screen = QApplication.primaryScreen()
    screen_geometry = screen.geometry()

    screen_width = screen_geometry.width()
    screen_height = screen_geometry.height()

    return screen_width, screen_height