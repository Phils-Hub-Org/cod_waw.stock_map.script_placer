# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'consoleJJgdxD.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPlainTextEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_ConsoleWidget(object):
    def setupUi(self, ConsoleWidget):
        if not ConsoleWidget.objectName():
            ConsoleWidget.setObjectName(u"ConsoleWidget")
        ConsoleWidget.resize(915, 394)
        ConsoleWidget.setStyleSheet(u"QToolTip {\n"
"    background-color: #2e2e2e;\n"
"    color: #ffffff;\n"
"    border: 1px solid #5b5e60;\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"    opacity: 200;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QFrame {\n"
"    background-color: #2e2e2e;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    color: #fff;\n"
"    border: 1px solid #5b5e60;\n"
"    border-radius: 4px;\n"
"    padding: 6px;\n"
"    font-size: 11px;\n"
"    line-height: 1.4;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border-color: #4a90e2;\n"
"    background-color: #3a3a3a;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #3c3f41;\n"
"    color: #fff;\n"
"    border: 1px solid #5b5e60;\n"
"    border-radius: 4px;\n"
"    padding: 0px 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-color: #4a90e2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3d78b2;\n"
"    border-color: #2a5f92;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #4a90e2;\n"
"    border-color: #3d78b"
                        "2;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: #111;\n"
"    width: 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #61657B;\n"
"    min-height: 15px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #ff6b27;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    border: none;\n"
"    width: 0;\n"
"    height: 0;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.verticalLayout = QVBoxLayout(ConsoleWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.frame = QFrame(ConsoleWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.console = QPlainTextEdit(self.frame)
        self.console.setObjectName(u"console")
        font = QFont()
        self.console.setFont(font)
        self.console.setStyleSheet(u"QPlainTextEdit {\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"}")
        self.console.setFrameShape(QFrame.Shape.NoFrame)
        self.console.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.console.setReadOnly(True)
        self.console.setTabStopDistance(16.000000000000000)

        self.verticalLayout_2.addWidget(self.console)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame {\n"
"	background: transparent;\n"
"	border-bottom-left-radius: 9px;\n"
"	border-bottom-right-radius: 9px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.close_console_btn = QPushButton(self.frame_2)
        self.close_console_btn.setObjectName(u"close_console_btn")
        self.close_console_btn.setMinimumSize(QSize(0, 0))
        self.close_console_btn.setStyleSheet(u"QPushButton {\n"
"	border-bottom-right-radius: 0px;\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.close_console_btn)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(ConsoleWidget)

        QMetaObject.connectSlotsByName(ConsoleWidget)
    # setupUi

    def retranslateUi(self, ConsoleWidget):
        ConsoleWidget.setWindowTitle(QCoreApplication.translate("ConsoleWidget", u"ConsoleWidget", None))
        self.console.setPlaceholderText(QCoreApplication.translate("ConsoleWidget", u"Console...", None))
        self.close_console_btn.setText(QCoreApplication.translate("ConsoleWidget", u"Close", None))
    # retranslateUi

