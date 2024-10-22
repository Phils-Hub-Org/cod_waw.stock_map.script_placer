# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowspiOVe.ui'
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
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)
import Resources.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(449, 349)
        MainWindow.setMinimumSize(QSize(449, 349))
        MainWindow.setMaximumSize(QSize(449, 349))
        icon = QIcon()
        icon.addFile(u":/ico/Icons/ico/phils-hub.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"/* QToolTip */\n"
"QToolTip {\n"
"    background-color: #2e2e2e;   /* Dark gray background */\n"
"    color: #ffffff;              /* White text */\n"
"    border: 1px solid #5b5e60;   /* Light gray border */\n"
"    padding: 4px;                /* Padding for the tooltip */\n"
"    border-radius: 4px;          /* Rounded corners */\n"
"    opacity: 200;                /* Slight transparency */\n"
"    font-size: 12px;             /* Slightly smaller font size for readability */\n"
"}\n"
"\n"
"/* QMenuBar */\n"
"QMenuBar {\n"
"    background-color: #2e2e2e;    /* Dark gray background */\n"
"    color: #ffffff;               /* White text */\n"
"    border-bottom: 1px solid #5b5e60;  /* Light gray border for separation */\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background-color: transparent; /* Transparent background */\n"
"    padding: 6px 6px;             /* Padding for menu items */\n"
"    color: #ffffff;                /* White text */\n"
"}\n"
"\n"
"QMenuBar::item:selected {          /* Hovered menu item "
                        "*/\n"
"    background-color: #4a90e2;     /* Light blue on hover */\n"
"    color: #ffffff;                /* Ensure text remains white */\n"
"}\n"
"\n"
"QMenuBar::item:pressed {           /* Pressed menu item */\n"
"    background-color: #3d78b2;     /* Darker blue on press */\n"
"    color: #ffffff;                /* Ensure text remains white */\n"
"}\n"
"\n"
"/* QMenu */\n"
"QMenu {\n"
"    background-color: #2e2e2e;     /* Dark gray background for menus */\n"
"    border: 1px solid #5b5e60;     /* Light gray border */\n"
"}\n"
"\n"
"QMenu::item {\n"
"    background-color: transparent; /* Transparent background for menu items */\n"
"    color: #ffffff;                /* White text */\n"
"	padding: 6px;\n"
"    margin-left: 6px;             /* Padding for each menu item */\n"
"}\n"
"\n"
"QMenu::item:selected {             /* Hovered menu item */\n"
"    background-color: #4a90e2;     /* Light blue background on hover */\n"
"    color: #ffffff;                /* Ensure text remains white */\n"
"}\n"
"\n"
"QMe"
                        "nu::item:pressed {              /* Pressed menu item */\n"
"    background-color: #3d78b2;     /* Darker blue background on press */\n"
"    color: #ffffff;                /* Ensure text remains white */\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"    background-color: #5b5e60;     /* Light gray separator between items */\n"
"}\n"
"\n"
"/* QMenu::indicator (checkboxes and radio buttons in menus) */\n"
"QMenu::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    background-color: #2e2e2e;     /* Dark gray background for indicators */\n"
"    border: 1px solid #5b5e60;     /* Light gray border */\n"
"    border-radius: 2px;            /* Slightly rounded corners */\n"
"}\n"
"\n"
"QMenu::indicator:checked {\n"
"    background-color: #4a90e2;     /* Light blue when checked */\n"
"    border-color: #3d78b2;         /* Darker blue border when checked */\n"
"}\n"
"\n"
"QMenu::indicator:unchecked {\n"
"    background-color: #2e2e2e;     /* Keep the dark gray when unchecked */\n"
"    border-co"
                        "lor: #5b5e60;         /* Light gray border when unchecked */\n"
"}\n"
"\n"
"/* QToolBar */\n"
"QToolBar {\n"
"    background-color: #2e2e2e;      /* Dark gray background */\n"
"    border: 1px solid #5b5e60;      /* Light gray border */\n"
"    padding: 4px;                   /* Padding inside the toolbar */\n"
"    spacing: 4px;                   /* Spacing between toolbar buttons */\n"
"}\n"
"\n"
"QToolBar::handle {\n"
"    background-color: #5b5e60;      /* Light gray handle for draggable toolbars */\n"
"    width: 10px;                    /* Width of the handle */\n"
"	height: 10px;\n"
"    margin: 4px;                    /* Margin around the handle */\n"
"}\n"
"\n"
"QToolBar::separator {\n"
"    background-color: #5b5e60;      /* Light gray for separators */\n"
"    width: 1px;                     /* Thickness of the separator */\n"
"    height: 24px;                   /* Height of the separator */\n"
"    margin: 6px;                    /* Space around the separator */\n"
"}\n"
"\n"
"QToolBar::item {\n"
""
                        "    padding: 4px;                   /* Padding for individual toolbar items */\n"
"}\n"
"\n"
"/* QStatusBar */\n"
"QStatusBar {\n"
"    background-color: #2e2e2e;   /* Dark gray background */\n"
"    border-top: 1px solid #5b5e60; /* Light gray top border for separation */\n"
"    color: #ffffff;              /* White text */\n"
"    font-size: 13px;             /* Slightly smaller font for the status bar */\n"
"    padding: 6px;                /* Padding inside the status bar */\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    border: none;                /* No border around individual status items */\n"
"    padding: 0px 5px;            /* Padding between status bar items */\n"
"}\n"
"\n"
"QStatusBar QLabel {\n"
"    color: #ffffff;              /* White text for any QLabel inside the status bar */\n"
"    background-color: transparent; /* Ensure QLabel in status bar matches the bar's background */\n"
"}\n"
"\n"
"QStatusBar::indicator {\n"
"    background-color: #4a90e2;   /* Optional indicator styling, e.g., for i"
                        "cons or status signals */\n"
"    border-radius: 4px;          /* Rounded corners for any indicator elements */\n"
"}\n"
"\n"
"/* Scroll Area Styling (optional) */\n"
"QScrollArea {\n"
"    background-color: transparent; /* Transparent to match the central widget */\n"
"    border: none;                  /* No border */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background-color: #3c3f41;    /* Darker gray for scroll bar background */\n"
"    width: 12px;                  /* Scroll bar width */\n"
"    margin: 22px 0 22px 0;        /* Top and bottom margins */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #5b5e60;    /* Slightly lighter gray for scroll handle */\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none;             /* Remove arrows */\n"
"}\n"
"\n"
"/* QGroupBox */\n"
"QGroupBox {\n"
"    background-color: #2e2e2e;        /* Dark gray background */\n"
"    border: 1px solid #5b5e60;        /* Ligh"
                        "t gray border */\n"
"    border-radius: 4px;               /* Rounded corners */\n"
"    margin-top: 15px;                 /* Space above the group box */\n"
"    padding-top: 0px;                    /* Padding inside the group box */\n"
"    color: #ffffff;                   /* White text for the title */\n"
"    font-weight: bold;                /* Bold title text */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;    /* Position the title at the top left */\n"
"    background-color: transparent;    /* Transparent background for the title */\n"
"    padding: 0 5px;                   /* Padding around the title */\n"
"    color: #ffffff;                   /* White text for the title */\n"
"}\n"
"\n"
"QGroupBox::title:hover {\n"
"    color: #4a90e2;                   /* Light blue title on hover */\n"
"}\n"
"\n"
"QGroupBox:flat {\n"
"    border: none;                     /* No border when the group box is flat */\n"
"}\n"
"\n"
"QGroupBox:disabled {\n"
""
                        "    color: #777777;                   /* Lighter gray text for disabled group box */\n"
"    border-color: #5b5e60;            /* Keep the light gray border */\n"
"}\n"
"\n"
"/* QGraphicsView */\n"
"QGraphicsView {\n"
"    background-color: #2e2e2e;  /* Dark gray background */\n"
"    border: 1px solid #5b5e60;  /* Light gray border */\n"
"    border-radius: 4px;         /* Rounded corners */\n"
"}\n"
"\n"
"QGraphicsView:focus {\n"
"    border-color: #4a90e2;      /* Light blue border when focused */\n"
"    background-color: #333333;  /* Slightly lighter gray background on focus */\n"
"}\n"
"\n"
"QGraphicsView:disabled {\n"
"    background-color: #2e2e2e;  /* Dark gray background when disabled */\n"
"    border-color: #5b5e60;      /* Light gray border for disabled state */\n"
"    color: #777777;             /* Lighter gray for disabled text or content */\n"
"}\n"
"\n"
"QGraphicsView::viewport {\n"
"    background-color: #2e2e2e;  /* Dark gray background for the viewport */\n"
"}\n"
"\n"
"/* QLabel */\n"
"QL"
                        "abel {\n"
"    color: #ffffff;             /* White text */\n"
"}\n"
"\n"
"/* QFrame */\n"
"QFrame {\n"
"    background-color: #2e2e2e;  /* Dark gray for frames */\n"
"}\n"
"\n"
"/* QLineEdit */\n"
"QLineEdit {\n"
"    background-color: #2e2e2e;  /* Dark gray background for input fields */\n"
"    color: #ffffff;             /* White text */\n"
"    border: 1px solid #5b5e60;  /* Light gray border */\n"
"    border-radius: 4px;         /* Rounded corners */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #4a90e2;      /* Light blue border when focused */\n"
"    background-color: #333333;  /* Slightly lighter gray on focus */\n"
"}\n"
"\n"
"/* QListWidget */\n"
"QListWidget {\n"
"    background-color: #2e2e2e;      /* Dark gray background */\n"
"    color: #ffffff;                 /* White text */\n"
"    border: 1px solid #5b5e60;      /* Light gray border */\n"
"    padding: 4px;                   /* Padding around the list */\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    background-color: transparent;  "
                        "/* Transparent background for items */\n"
"    color: #ffffff;                 /* White text for list items */\n"
"    border: none;                   /* No border for list items */\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #4a90e2;      /* Light blue background when selected */\n"
"    color: #ffffff;                 /* Ensure text remains white when selected */\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: #3d78b2;      /* Darker blue on hover */\n"
"    color: #ffffff;                 /* Ensure text remains white when hovered */\n"
"}\n"
"\n"
"QListWidget::item:focus {\n"
"    border: 1px solid #4a90e2;      /* Light blue border on focus */\n"
"}\n"
"\n"
"/* QPlainTextEdit */\n"
"QPlainTextEdit {\n"
"    background-color: #2b2b2b;  /* Darker gray background for text area */\n"
"    color: #ffffff;             /* White text */\n"
"    border: 1px solid #5b5e60;  /* Light gray border */\n"
"    border-radius: 0px;         /* No rounded corners */\n"
"    paddin"
                        "g: 10px;              /* Comfortable padding for text input */\n"
"    font-size: 13px;            /* Slightly smaller font */\n"
"    line-height: 1.4;           /* Adjust line spacing for readability */\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border-color: #4a90e2;      /* Light blue border on focus */\n"
"    background-color: #3a3a3a;  /* Slightly lighter gray on focus */\n"
"}\n"
"\n"
"/* QTabWidget */\n"
"QTabWidget::pane {\n"
"    background-color: #2e2e2e;      /* Dark gray background */\n"
"    border: 1px solid #5b5e60;      /* Light gray border around the pane */\n"
"    padding: 4px;                   /* Padding inside the pane */\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0px;                      /* Space from the left */\n"
"}\n"
"\n"
"/* QTabBar::tab */\n"
"QTabBar::tab {\n"
"    background-color: #3c3f41;      /* Dark gray background for tabs */\n"
"    color: #ffffff;                 /* White text for tabs */\n"
"    border-left: 1px solid #5b5e60;      /* Light gray border arou"
                        "nd tabs */\n"
"    border-top: 1px solid #5b5e60;\n"
"    border-right: 1px solid #5b5e60;\n"
"    padding: 4px 8px;              /* Padding for each tab */\n"
"    margin-left: 2px;                    /* Slight margin between tabs */\n"
"    margin-right: 2px;\n"
"    border-top-left-radius: 4px;    /* Rounded top corners */\n"
"    border-top-right-radius: 4px;   /* Rounded top corners */\n"
"}\n"
"\n"
"/* Selected tab */\n"
"QTabBar::tab:selected {\n"
"    background-color: #4a90e2;      /* Light blue background for selected tab */\n"
"    color: #ffffff;                 /* White text for selected tab */\n"
"    border-color: #4a90e2;          /* Blue border for selected tab */\n"
"}\n"
"\n"
"/* Hovered tab */\n"
"QTabBar::tab:hover {\n"
"    background-color: #3d78b2;      /* Darker blue on hover */\n"
"    color: #ffffff;                 /* White text */\n"
"}\n"
"\n"
"/* Disabled tab */\n"
"QTabBar::tab:disabled {\n"
"    background-color: #2e2e2e;      /* Dark gray for disabled tab */\n"
"    color: #77"
                        "7777;                 /* Light gray text for disabled tabs */\n"
"}\n"
"\n"
"/* Focused tab */\n"
"QTabBar::tab:focus {\n"
"    border: 1px solid #4a90e2;      /* Blue border when tab is focused */\n"
"}\n"
"\n"
"/* Tab close button (optional) */\n"
"QTabBar::close-button {\n"
"    /* image: url(close-icon.png);     Replace with your close icon path */\n"
"    subcontrol-position: right;     /* Position the close button on the right */\n"
"    margin: 0 8px 0 0;              /* Spacing for the close button */\n"
"}\n"
"/*\n"
"QTabBar::close-button:hover {\n"
"    image: url(close-icon-hover.png);   Change icon on hover \n"
"}*/\n"
"\n"
"/* QComboBox */\n"
"QComboBox {\n"
"    background-color: #2e2e2e;       /* Dark gray background */\n"
"    color: #ffffff;                  /* White text */\n"
"    border: 1px solid #5b5e60;       /* Light gray border */\n"
"    border-radius: 4px;              /* Rounded corners */\n"
"    padding-left: 2px;                    /* Padding inside the combo box */\n"
"}\n"
"\n"
""
                        "QComboBox:hover {\n"
"    background-color: #3a3a3a;       /* Slightly lighter gray on hover */\n"
"    border-color: #4a90e2;           /* Light blue border on hover */\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    background-color: #333333;       /* Lighter gray on focus */\n"
"    border-color: #4a90e2;           /* Light blue border on focus */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px;                      /* Width of the drop-down button */\n"
"    background-color: #2e2e2e;        /* Dark gray background for drop-down */\n"
"    border-left: 1px solid #5b5e60;   /* Light gray separator between drop-down button and combo box */\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/888EAC-20px/ICONS/888EAC-20px/arrow-down.svg);  /*Replace with your down arrow icon */\n"
"    width: 12px;                         /* Width of the arrow */\n"
"    height: 12px;                        /* Height of the arrow */\n"
"}\n"
""
                        "\n"
"QComboBox::down-arrow:hover {\n"
"    image: url(:/888EAC-20px/ICONS/888EAC-20px/arrow-down.svg); /* Optional: different icon on hover */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #2e2e2e;        /* Dark gray background for drop-down list */\n"
"    color: #ffffff;                   /* White text */\n"
"    border: 1px solid #5b5e60;        /* Light gray border around the list */\n"
"    selection-background-color: #4a90e2;  /* Light blue background for selected item */\n"
"    selection-color: #ffffff;         /* White text for selected item */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    background-color: transparent;    /* Transparent background for list items */\n"
"    padding: 6px;                     /* Padding for each item in the list */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: #4a90e2;        /* Light blue when an item is selected */\n"
"    color: #ffffff;                   /* White text for selected item */"
                        "\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #3d78b2;        /* Darker blue on hover */\n"
"    color: #ffffff;                   /* White text when hovered */\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color: #2e2e2e;        /* Dark gray background when disabled */\n"
"    color: #777777;                   /* Lighter gray text when disabled */\n"
"    border-color: #5b5e60;            /* Keep the light gray border */\n"
"}\n"
"\n"
"/* QPushButton */\n"
"QPushButton {\n"
"    background-color: #3c3f41;  /* Dark gray background */\n"
"    color: #ffffff;             /* White text */\n"
"    border: 1px solid #5b5e60;  /* Light gray border */\n"
"    border-radius: 4px;         /* Rounded corners */\n"
"	padding: 0px 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4a90e2;  /* Light blue on hover */\n"
"    border-color: #3d78b2;      /* Darker blue border */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3d78b2;  /* Darker blu"
                        "e on press */\n"
"    border-color: #2a5f92;      /* Even darker border when pressed */\n"
"}\n"
"\n"
"/* QCheckBox */\n"
"QCheckBox {\n"
"    color: #ffffff;                 /* White text for checkbox label */\n"
"    spacing: 6px;                   /* Space between checkbox and label */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 14px;                    /* Set the size of the checkbox */\n"
"    height: 14px;\n"
"    background-color: #2e2e2e;      /* Dark gray background for the checkbox */\n"
"    border: 1px solid #5b5e60;      /* Light gray border */\n"
"    border-radius: 2px;             /* Slight rounding for modern look */\n"
"}\n"
"\n"
"/* Hovered checkbox */\n"
"QCheckBox::indicator:hover {\n"
"    background-color: #3b73b4;      /* Light blue on hover */\n"
"    border-color: #ff050d;          /* Darker blue border on hover */\n"
"}\n"
"\n"
"/*\n"
"red: ff050d\n"
"green: 0dce1d\n"
"*/\n"
"\n"
"/* Checked checkbox */\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #4a90e2;   "
                        "   /* Light blue when checked */\n"
"    border-color: #3d78b2;          /* Darker blue border when checked */\n"
"/*    image: url(:/checked-icon.png);  Replace with your checkmark icon if needed */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border-color: #0dce1d;\n"
"}\n"
"\n"
"/* Indeterminate checkbox (for tri-state checkboxes) */\n"
"QCheckBox::indicator:indeterminate {\n"
"    background-color: #4a90e2;      /* Light blue when in indeterminate state */\n"
"    border-color: #3d78b2;          /* Darker blue border */\n"
"/*    image: url(:/indeterminate-icon.png);  Replace with your indeterminate icon */\n"
"}\n"
"\n"
"/* Pressed checkbox */\n"
"QCheckBox::indicator:pressed {\n"
"    background-color: #3d78b2;      /* Darker blue on press */\n"
"    border-color: #2a5f92;          /* Even darker border when pressed */\n"
"}\n"
"\n"
"/* Disabled checkbox */\n"
"QCheckBox::indicator:disabled {\n"
"    background-color: #2e2e2e;      /* Dark gray when disabled */\n"
"    border-color: #5b5e6"
                        "0;          /* Light gray border */\n"
"    color: #777777;                 /* Light gray label when disabled */\n"
"}\n"
"\n"
"/* QRadioButton */\n"
"QRadioButton {\n"
"    color: #ffffff;              /* White text */\n"
"    spacing: 5px;                /* Space between radio button and label */\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 14px;                 /* Size of the radio button */\n"
"    height: 14px;\n"
"    background-color: #2e2e2e;   /* Dark gray background for the indicator */\n"
"    border: 1px solid #5b5e60;   /* Light gray border */\n"
"    border-radius: 8px;          /* Circular radio button */\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    background-color: #4a90e2;   /* Light blue on hover */\n"
"    border-color: #3d78b2;       /* Darker blue border on hover */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #4a90e2;   /* Light blue when checked */\n"
"    border-color: #3d78b2;       /* Darker blue border when checked */\n"
"}\n"
"\n"
""
                        "QRadioButton::indicator:pressed {\n"
"    background-color: #3d78b2;   /* Darker blue on press */\n"
"    border-color: #2a5f92;       /* Even darker border on press */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:pressed {\n"
"    background-color: #3d78b2;   /* Darker blue when checked and pressed */\n"
"    border-color: #2a5f92;       /* Even darker border when checked and pressed */\n"
"}\n"
"\n"
"/* QToolButton */\n"
"QToolButton {\n"
"    background-color: #3c3f41;    /* Dark gray background */\n"
"    color: #ffffff;               /* White text/icon */\n"
"    border: 1px solid #5b5e60;    /* Light gray border */\n"
"    border-radius: 4px;           /* Rounded corners */\n"
"    padding: 0px 0px;            /* Padding for comfortable button size */\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #4a90e2;    /* Light blue background on hover */\n"
"    border-color: #3d78b2;        /* Darker blue border on hover */\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #3d78b2;  "
                        "  /* Darker blue background on press */\n"
"    border-color: #2a5f92;        /* Even darker border when pressed */\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"    background-color: #3d78b2;    /* Darker blue when checked */\n"
"    border-color: #2a5f92;        /* Border color when checked */\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color: #2e2e2e;    /* Dark gray when disabled */\n"
"    color: #777777;               /* Lighter gray text/icon for disabled state */\n"
"    border-color: #5b5e60;        /* Keep the border color same as normal state */\n"
"}\n"
"\n"
"/* QToolButton::menu-button */\n"
"QToolButton::menu-button {\n"
"    background-color: #3c3f41;      /* Dark gray background for menu button */\n"
"    border: 1px solid #5b5e60;      /* Light gray border for menu button */\n"
"    padding: 4px;                   /* Padding for the menu button */\n"
"}\n"
"\n"
"QToolButton::menu-button:hover {\n"
"    background-color: #4a90e2;      /* Light blue on hover */\n"
"    border-color: #3d7"
                        "8b2;          /* Darker blue border on hover */\n"
"}\n"
"\n"
"QToolButton::menu-button:pressed {\n"
"    background-color: #3d78b2;      /* Darker blue on press */\n"
"    border-color: #2a5f92;          /* Even darker border on press */\n"
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
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mod_name_input = QLineEdit(self.frame_5)
        self.mod_name_input.setObjectName(u"mod_name_input")
        self.mod_name_input.setMinimumSize(QSize(0, 28))
        self.mod_name_input.setStyleSheet(u"QLineEdit {padding: 3px;}")
        self.mod_name_input.setMaxLength(35)

        self.horizontalLayout_2.addWidget(self.mod_name_input)

        self.submit_btn = QPushButton(self.frame_5)
        self.submit_btn.setObjectName(u"submit_btn")
        self.submit_btn.setStyleSheet(u"QPushButton {padding: 5px;}")

        self.horizontalLayout_2.addWidget(self.submit_btn)


        self.verticalLayout_6.addWidget(self.frame_5)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"QLabel {color: #888eac; padding-left: 3px;}")

        self.verticalLayout_6.addWidget(self.label_3)

        self.groupBox = QGroupBox(self.frame_4)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.verticalLayout_6.addWidget(self.groupBox)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 111))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
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

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.frame_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 45))
        self.groupBox_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setCheckable(False)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 3)
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_7.addWidget(self.groupBox_3)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setSizeGripEnabled(False)
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 449, 29))
        self.menuBar.setDefaultUp(False)
        self.menuBar.setNativeMenuBar(True)
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionAbout)

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
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ModName Example: nazi_zombie_prototype | prototype.", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"SP", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Maybe in future...", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"ZM", None))
        self.zm_prototype_cbox.setText(QCoreApplication.translate("MainWindow", u"Nacht der Untoten (nazi_zombie_prototype)", None))
        self.zm_asylum_cbox.setText(QCoreApplication.translate("MainWindow", u"Verr\u00fcckt (nazi_zombie_asylum)", None))
        self.zm_sumpf_cbox.setText(QCoreApplication.translate("MainWindow", u"Shi No Numa (nazi_zombie_sumpf)", None))
        self.zm_factory_cbox.setText(QCoreApplication.translate("MainWindow", u"Der Riese (nazi_zombie_factory)", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"MP", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Maybe in future...", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

