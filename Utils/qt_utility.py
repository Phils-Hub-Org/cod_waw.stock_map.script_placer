from PySide6.QtWidgets import QApplication, QMessageBox

def displayMessageBox(message: str, x: int = None, y: int = None) -> None:
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setWindowTitle("Information")
    msgBox.setText(message)
    msgBox.setStandardButtons(QMessageBox.Ok)
    
    if x is None or y is None:
        screenWidth, screenHeight = getScreenDimms()

        if x is None:
            # Get screen geometry and center horizontally
            msgBox_width = msgBox.sizeHint().width()
            x = (screenWidth - msgBox_width) // 2

        if y is None:
            # Get screen geometry and center vertically
            msgBox_height = msgBox.sizeHint().height()
            y = (screenHeight - msgBox_height) // 2  # Vertically center
    
    msgBox.move(x, y)  # Set position
    msgBox.exec()

def getScreenDimms() -> tuple[int, int]:
    screen = QApplication.primaryScreen()
    screenGeometry = screen.geometry()

    screenWidth = screenGeometry.width()
    screenHeight = screenGeometry.height()

    return screenWidth, screenHeight

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)

    displayMessageBox("Screen size: " + str(getScreenDimms()))

    sys.exit(app.exec())