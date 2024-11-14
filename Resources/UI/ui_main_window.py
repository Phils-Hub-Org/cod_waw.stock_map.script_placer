# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowRUYRnc.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)
import Resources.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(449, 634)
        MainWindow.setMinimumSize(QSize(449, 634))
        MainWindow.setMaximumSize(QSize(449, 720))
        icon = QIcon()
        icon.addFile(u":/ico/Icons/ico/phils-hub.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"QToolTip {\n"
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
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #2e2e2e;\n"
"    color: #ffffff;\n"
"    border: 1px solid #5b5e60;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #4a90e2;\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #3c3f41;\n"
"    color: #ffffff;\n"
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
"    border-color: #3d78b2;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: #"
                        "ffffff;\n"
"    spacing: 6px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    background-color: #2e2e2e;\n"
"    border: 1px solid #5b5e60;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"    background-color: #3b73b4;\n"
"    border-color: #0dce1d;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #4a90e2;\n"
"    border-color: #3d78b2;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border-color: #ff050d;\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate {\n"
"    background-color: #4a90e2;\n"
"    border-color: #3d78b2;\n"
"}\n"
"\n"
"QCheckBox::indicator:pressed {\n"
"    background-color: #3d78b2;\n"
"    border-color: #2a5f92;\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled {\n"
"    background-color: #2e2e2e;\n"
"    border-color: #5b5e60;\n"
"    color: #777777;\n"
"}\n"
"\n"
"QScrollArea {\n"
"    background-color: #2e2e2e;\n"
"    border: 1px solid #5b5e60;\n"
"    border-radius: 4px;\n"
"    padding: "
                        "5px;\n"
"}\n"
"\n"
"QScrollArea QWidget {\n"
"    background-color: #2e2e2e;\n"
"}\n"
"\n"
"QScrollArea > QWidget {\n"
"    background-color: #2e2e2e;\n"
"}\n"
"\n"
"QScrollArea::corner {\n"
"    background-color: #2e2e2e;\n"
"}\n"
"\n"
"QStatusBar {\n"
"    background-color: #2e2e2e;\n"
"    border-top: 1px solid #5b5e60;\n"
"    color: #ffffff;\n"
"    font-size: 13px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    border: none;\n"
"    padding: 0px 5px;\n"
"}\n"
"\n"
"QStatusBar QLabel {\n"
"    color: #ffffff;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QStatusBar::indicator {\n"
"    background-color: #4a90e2;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    background-color: #2e2e2e;\n"
"    border: 1px solid #5b5e60;\n"
"    border-radius: 4px;\n"
"    margin-top: 15px;\n"
"    padding-top: 0px;\n"
"    color: #ffffff;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    bac"
                        "kground-color: transparent;\n"
"    padding: 0 5px;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QGroupBox::title:hover {\n"
"    color: #4a90e2;\n"
"}\n"
"\n"
"QGroupBox:flat {\n"
"    border: none;\n"
"}\n"
"\n"
"QGroupBox:disabled {\n"
"    color: #777777;\n"
"    border-color: #5b5e60;\n"
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
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"/* Central Widget */\n"
"#centralwidget {\n"
"    background-color: #1e1e1e;  /* Dark gray background */\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet(u"QFrame {margin: 6px;}")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setStyleSheet(u"QFrame {margin: 0px;}")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mod_name_input = QLineEdit(self.frame_5)
        self.mod_name_input.setObjectName(u"mod_name_input")
        self.mod_name_input.setMinimumSize(QSize(0, 28))
        self.mod_name_input.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.mod_name_input.setStyleSheet(u"QLineEdit {padding: 3px;}")
        self.mod_name_input.setMaxLength(35)

        self.horizontalLayout_2.addWidget(self.mod_name_input)

        self.submit_btn = QPushButton(self.frame_5)
        self.submit_btn.setObjectName(u"submit_btn")
        self.submit_btn.setStyleSheet(u"QPushButton {padding: 5px;}")

        self.horizontalLayout_2.addWidget(self.submit_btn)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"QLabel {color: #888eac; padding-left: 3px;}")

        self.verticalLayout_2.addWidget(self.label_3)

        self.shortcut_cbox = QCheckBox(self.frame)
        self.shortcut_cbox.setObjectName(u"shortcut_cbox")
        self.shortcut_cbox.setStyleSheet(u"QCheckBox {padding-left: 5px;}")

        self.verticalLayout_2.addWidget(self.shortcut_cbox)

        self.insert_ingame_print_msg_cbox = QCheckBox(self.frame)
        self.insert_ingame_print_msg_cbox.setObjectName(u"insert_ingame_print_msg_cbox")
        self.insert_ingame_print_msg_cbox.setStyleSheet(u"QCheckBox {padding-left: 5px;}")

        self.verticalLayout_2.addWidget(self.insert_ingame_print_msg_cbox)

        self.build_mod_cbox = QCheckBox(self.frame)
        self.build_mod_cbox.setObjectName(u"build_mod_cbox")
        self.build_mod_cbox.setStyleSheet(u"QCheckBox {padding-left: 5px;}")

        self.verticalLayout_2.addWidget(self.build_mod_cbox)

        self.run_map_cbox = QCheckBox(self.frame)
        self.run_map_cbox.setObjectName(u"run_map_cbox")
        self.run_map_cbox.setStyleSheet(u"QCheckBox {padding-left: 5px;}")

        self.verticalLayout_2.addWidget(self.run_map_cbox)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.groupBox.setMinimumSize(QSize(0, 158))
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.groupBox)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 397, 330))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(3, 3, 3, 3)
        self.sp_ber1_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_ber1_cbox.setObjectName(u"sp_ber1_cbox")

        self.verticalLayout_9.addWidget(self.sp_ber1_cbox)

        self.sp_ber2_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_ber2_cbox.setObjectName(u"sp_ber2_cbox")

        self.verticalLayout_9.addWidget(self.sp_ber2_cbox)

        self.sp_ber3_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_ber3_cbox.setObjectName(u"sp_ber3_cbox")

        self.verticalLayout_9.addWidget(self.sp_ber3_cbox)

        self.sp_ber3b_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_ber3b_cbox.setObjectName(u"sp_ber3b_cbox")

        self.verticalLayout_9.addWidget(self.sp_ber3b_cbox)

        self.sp_mak_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_mak_cbox.setObjectName(u"sp_mak_cbox")

        self.verticalLayout_9.addWidget(self.sp_mak_cbox)

        self.sp_oki2_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_oki2_cbox.setObjectName(u"sp_oki2_cbox")

        self.verticalLayout_9.addWidget(self.sp_oki2_cbox)

        self.sp_oki3_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_oki3_cbox.setObjectName(u"sp_oki3_cbox")

        self.verticalLayout_9.addWidget(self.sp_oki3_cbox)

        self.sp_pby_fly_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_pby_fly_cbox.setObjectName(u"sp_pby_fly_cbox")

        self.verticalLayout_9.addWidget(self.sp_pby_fly_cbox)

        self.sp_pel1_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_pel1_cbox.setObjectName(u"sp_pel1_cbox")

        self.verticalLayout_9.addWidget(self.sp_pel1_cbox)

        self.sp_pel1a_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_pel1a_cbox.setObjectName(u"sp_pel1a_cbox")

        self.verticalLayout_9.addWidget(self.sp_pel1a_cbox)

        self.sp_pel1b_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_pel1b_cbox.setObjectName(u"sp_pel1b_cbox")

        self.verticalLayout_9.addWidget(self.sp_pel1b_cbox)

        self.sp_pel2_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_pel2_cbox.setObjectName(u"sp_pel2_cbox")

        self.verticalLayout_9.addWidget(self.sp_pel2_cbox)

        self.sp_see1_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_see1_cbox.setObjectName(u"sp_see1_cbox")

        self.verticalLayout_9.addWidget(self.sp_see1_cbox)

        self.sp_see2_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_see2_cbox.setObjectName(u"sp_see2_cbox")

        self.verticalLayout_9.addWidget(self.sp_see2_cbox)

        self.sp_sniper_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_sniper_cbox.setObjectName(u"sp_sniper_cbox")

        self.verticalLayout_9.addWidget(self.sp_sniper_cbox)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_3.addWidget(self.scrollArea_2)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_4 = QGroupBox(self.frame)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy2.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy2)
        self.groupBox_4.setMinimumSize(QSize(0, 158))
        self.groupBox_4.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_4.setStyleSheet(u"QGroupBox {border: none;}")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.groupBox_4)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setStyleSheet(u"QScrollBar::handle:vertical {\n"
"    min-height: 40px;\n"
"}")
        self.scrollArea_3.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_3.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 397, 506))
        self.scrollAreaWidgetContents_3.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(3, 3, 3, 3)
        self.mp_airfield_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_airfield_cbox.setObjectName(u"mp_airfield_cbox")

        self.verticalLayout_11.addWidget(self.mp_airfield_cbox)

        self.mp_asylum_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_asylum_cbox.setObjectName(u"mp_asylum_cbox")

        self.verticalLayout_11.addWidget(self.mp_asylum_cbox)

        self.mp_kwai_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_kwai_cbox.setObjectName(u"mp_kwai_cbox")

        self.verticalLayout_11.addWidget(self.mp_kwai_cbox)

        self.mp_drum_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_drum_cbox.setObjectName(u"mp_drum_cbox")

        self.verticalLayout_11.addWidget(self.mp_drum_cbox)

        self.mp_bgate_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_bgate_cbox.setObjectName(u"mp_bgate_cbox")

        self.verticalLayout_11.addWidget(self.mp_bgate_cbox)

        self.mp_castle_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_castle_cbox.setObjectName(u"mp_castle_cbox")

        self.verticalLayout_11.addWidget(self.mp_castle_cbox)

        self.mp_shrine_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_shrine_cbox.setObjectName(u"mp_shrine_cbox")

        self.verticalLayout_11.addWidget(self.mp_shrine_cbox)

        self.mp_stalingrad_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_stalingrad_cbox.setObjectName(u"mp_stalingrad_cbox")

        self.verticalLayout_11.addWidget(self.mp_stalingrad_cbox)

        self.mp_courtyard_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_courtyard_cbox.setObjectName(u"mp_courtyard_cbox")

        self.verticalLayout_11.addWidget(self.mp_courtyard_cbox)

        self.mp_dome_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_dome_cbox.setObjectName(u"mp_dome_cbox")

        self.verticalLayout_11.addWidget(self.mp_dome_cbox)

        self.mp_downfall_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_downfall_cbox.setObjectName(u"mp_downfall_cbox")

        self.verticalLayout_11.addWidget(self.mp_downfall_cbox)

        self.mp_hangar_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_hangar_cbox.setObjectName(u"mp_hangar_cbox")

        self.verticalLayout_11.addWidget(self.mp_hangar_cbox)

        self.mp_kneedeep_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_kneedeep_cbox.setObjectName(u"mp_kneedeep_cbox")

        self.verticalLayout_11.addWidget(self.mp_kneedeep_cbox)

        self.mp_makin_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_makin_cbox.setObjectName(u"mp_makin_cbox")

        self.verticalLayout_11.addWidget(self.mp_makin_cbox)

        self.mp_makin_day_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_makin_day_cbox.setObjectName(u"mp_makin_day_cbox")

        self.verticalLayout_11.addWidget(self.mp_makin_day_cbox)

        self.mp_nachtfeuer_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_nachtfeuer_cbox.setObjectName(u"mp_nachtfeuer_cbox")

        self.verticalLayout_11.addWidget(self.mp_nachtfeuer_cbox)

        self.mp_outskirts_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_outskirts_cbox.setObjectName(u"mp_outskirts_cbox")

        self.verticalLayout_11.addWidget(self.mp_outskirts_cbox)

        self.mp_vodka_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_vodka_cbox.setObjectName(u"mp_vodka_cbox")

        self.verticalLayout_11.addWidget(self.mp_vodka_cbox)

        self.mp_roundhouse_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_roundhouse_cbox.setObjectName(u"mp_roundhouse_cbox")

        self.verticalLayout_11.addWidget(self.mp_roundhouse_cbox)

        self.mp_seelow_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_seelow_cbox.setObjectName(u"mp_seelow_cbox")

        self.verticalLayout_11.addWidget(self.mp_seelow_cbox)

        self.mp_subway_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_subway_cbox.setObjectName(u"mp_subway_cbox")

        self.verticalLayout_11.addWidget(self.mp_subway_cbox)

        self.mp_docks_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_docks_cbox.setObjectName(u"mp_docks_cbox")

        self.verticalLayout_11.addWidget(self.mp_docks_cbox)

        self.mp_suburban_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_suburban_cbox.setObjectName(u"mp_suburban_cbox")

        self.verticalLayout_11.addWidget(self.mp_suburban_cbox)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_10.addWidget(self.scrollArea_3)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 111))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.zm_prototype_cbox = QCheckBox(self.groupBox_2)
        self.zm_prototype_cbox.setObjectName(u"zm_prototype_cbox")

        self.verticalLayout_4.addWidget(self.zm_prototype_cbox)

        self.zm_asylum_cbox = QCheckBox(self.groupBox_2)
        self.zm_asylum_cbox.setObjectName(u"zm_asylum_cbox")

        self.verticalLayout_4.addWidget(self.zm_asylum_cbox)

        self.zm_sumpf_cbox = QCheckBox(self.groupBox_2)
        self.zm_sumpf_cbox.setObjectName(u"zm_sumpf_cbox")

        self.verticalLayout_4.addWidget(self.zm_sumpf_cbox)

        self.zm_factory_cbox = QCheckBox(self.groupBox_2)
        self.zm_factory_cbox.setObjectName(u"zm_factory_cbox")

        self.verticalLayout_4.addWidget(self.zm_factory_cbox)


        self.verticalLayout_2.addWidget(self.groupBox_2)


        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Phils-Hub - CoD: WaW - Stock-Map Script-Placer", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
#if QT_CONFIG(tooltip)
        self.mod_name_input.setToolTip(QCoreApplication.translate("MainWindow", u"35 char limit", None))
#endif // QT_CONFIG(tooltip)
        self.mod_name_input.setText("")
        self.mod_name_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter ModName", None))
        self.submit_btn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ModName Example: nazi_zombie_prototype | nacht | myTestMap1", None))
#if QT_CONFIG(tooltip)
        self.shortcut_cbox.setToolTip(QCoreApplication.translate("MainWindow", u"e.g.\n"
"'+set fs_game mods/{self.modName} +devmap {self.mapName} +set r_fullscreen 0'", None))
#endif // QT_CONFIG(tooltip)
        self.shortcut_cbox.setText(QCoreApplication.translate("MainWindow", u"Add shortcut to desktop (w/ args) ..for quick map loading ?", None))
#if QT_CONFIG(tooltip)
        self.insert_ingame_print_msg_cbox.setToolTip(QCoreApplication.translate("MainWindow", u"Example of in-game print message:\n"
"'zm_test1 built successfully!'\n"
"\n"
"Currently only available for mode: zm", None))
#endif // QT_CONFIG(tooltip)
        self.insert_ingame_print_msg_cbox.setText(QCoreApplication.translate("MainWindow", u"Insert an in-game print message to confirm build ?", None))
        self.build_mod_cbox.setText(QCoreApplication.translate("MainWindow", u"Build Mod ?", None))
        self.run_map_cbox.setText(QCoreApplication.translate("MainWindow", u"Run Map ?", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"SP", None))
        self.sp_ber1_cbox.setText(QCoreApplication.translate("MainWindow", u"Ring of Steel (ber1)", None))
        self.sp_ber2_cbox.setText(QCoreApplication.translate("MainWindow", u"Eviction (ber2)", None))
        self.sp_ber3_cbox.setText(QCoreApplication.translate("MainWindow", u"Heart of the Reich (ber3)", None))
        self.sp_ber3b_cbox.setText(QCoreApplication.translate("MainWindow", u"Downfall (ber3b)", None))
        self.sp_mak_cbox.setText(QCoreApplication.translate("MainWindow", u"Semper Fi (mak)", None))
        self.sp_oki2_cbox.setText(QCoreApplication.translate("MainWindow", u"Blowtorch & Corkscrew (oki2)", None))
        self.sp_oki3_cbox.setText(QCoreApplication.translate("MainWindow", u"Breaking Point (oki3)", None))
        self.sp_pby_fly_cbox.setText(QCoreApplication.translate("MainWindow", u"Black Cats (pby_fly)", None))
        self.sp_pel1_cbox.setText(QCoreApplication.translate("MainWindow", u"Little Resistance (pel1)", None))
        self.sp_pel1a_cbox.setText(QCoreApplication.translate("MainWindow", u"Burn 'Em Out (pel1a)", None))
        self.sp_pel1b_cbox.setText(QCoreApplication.translate("MainWindow", u"Relentless (pel1b)", None))
        self.sp_pel2_cbox.setText(QCoreApplication.translate("MainWindow", u"Hard Landing (pel2)", None))
        self.sp_see1_cbox.setText(QCoreApplication.translate("MainWindow", u"Their Land, Their Blood (see1)", None))
        self.sp_see2_cbox.setText(QCoreApplication.translate("MainWindow", u"Blood and Iron (see2)", None))
        self.sp_sniper_cbox.setText(QCoreApplication.translate("MainWindow", u"Vendetta (sniper)", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"MP", None))
        self.mp_airfield_cbox.setText(QCoreApplication.translate("MainWindow", u"Airfield (mp_airfield)", None))
        self.mp_asylum_cbox.setText(QCoreApplication.translate("MainWindow", u"Asylum (mp_asylum)", None))
        self.mp_kwai_cbox.setText(QCoreApplication.translate("MainWindow", u"Banzai (mp_kwai)", None))
        self.mp_drum_cbox.setText(QCoreApplication.translate("MainWindow", u"Battery (mp_drum)", None))
        self.mp_bgate_cbox.setText(QCoreApplication.translate("MainWindow", u"Breach (mp_bgate)", None))
        self.mp_castle_cbox.setText(QCoreApplication.translate("MainWindow", u"Castle (mp_castle)", None))
        self.mp_shrine_cbox.setText(QCoreApplication.translate("MainWindow", u"Cliffside (mp_shrine)", None))
        self.mp_stalingrad_cbox.setText(QCoreApplication.translate("MainWindow", u"Corrosion (mp_stalingrad)", None))
        self.mp_courtyard_cbox.setText(QCoreApplication.translate("MainWindow", u"Courtyard (mp_courtyard)", None))
        self.mp_dome_cbox.setText(QCoreApplication.translate("MainWindow", u"Dome (mp_dome)", None))
        self.mp_downfall_cbox.setText(QCoreApplication.translate("MainWindow", u"Downfall (mp_downfall)", None))
        self.mp_hangar_cbox.setText(QCoreApplication.translate("MainWindow", u"Hangar (mp_hangar)", None))
        self.mp_kneedeep_cbox.setText(QCoreApplication.translate("MainWindow", u"Knee Deep (mp_kneedeep)", None))
        self.mp_makin_cbox.setText(QCoreApplication.translate("MainWindow", u"Makin (mp_makin)", None))
        self.mp_makin_day_cbox.setText(QCoreApplication.translate("MainWindow", u"Makin Day (mp_makin_day)", None))
        self.mp_nachtfeuer_cbox.setText(QCoreApplication.translate("MainWindow", u"Nightfire (mp_nachtfeuer)", None))
        self.mp_outskirts_cbox.setText(QCoreApplication.translate("MainWindow", u"Outskirts (mp_outskirts)", None))
        self.mp_vodka_cbox.setText(QCoreApplication.translate("MainWindow", u"Revolution (mp_vodka)", None))
        self.mp_roundhouse_cbox.setText(QCoreApplication.translate("MainWindow", u"Roundhouse (mp_roundhouse)", None))
        self.mp_seelow_cbox.setText(QCoreApplication.translate("MainWindow", u"Seelow (mp_seelow)", None))
        self.mp_subway_cbox.setText(QCoreApplication.translate("MainWindow", u"Station (mp_subway)", None))
        self.mp_docks_cbox.setText(QCoreApplication.translate("MainWindow", u"Sub Pens (mp_docks)", None))
        self.mp_suburban_cbox.setText(QCoreApplication.translate("MainWindow", u"Upheaval (mp_suburban)", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"ZM", None))
        self.zm_prototype_cbox.setText(QCoreApplication.translate("MainWindow", u"Nacht der Untoten (nazi_zombie_prototype)", None))
        self.zm_asylum_cbox.setText(QCoreApplication.translate("MainWindow", u"Verr\u00fcckt (nazi_zombie_asylum)", None))
        self.zm_sumpf_cbox.setText(QCoreApplication.translate("MainWindow", u"Shi No Numa (nazi_zombie_sumpf)", None))
        self.zm_factory_cbox.setText(QCoreApplication.translate("MainWindow", u"Der Riese (nazi_zombie_factory)", None))
    # retranslateUi

