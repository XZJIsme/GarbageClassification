# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)
from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1180, 777)
        MainWindow.setMinimumSize(QSize(1180, 766))
        palette = QPalette()
        brush = QBrush(QColor(228, 228, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush)
        brush1 = QBrush(QColor(245, 245, 245, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.NoRole, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        brush3 = QBrush(QColor(255, 0, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.NoRole, brush4)
        brush5 = QBrush(QColor(0, 0, 0, 128))
        brush5.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.NoRole, brush6)
        brush7 = QBrush(QColor(0, 0, 0, 128))
        brush7.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        MainWindow.setPalette(palette)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setEnabled(True)
        font = QFont()
        font.setFamilies([u"\u7b49\u8ddd\u66f4\u7eb1\u9ed1\u4f53 SC"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
" \n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"# BY: WANDERSON M.PIMENTA\n"
"# PROJECT MADE WITH: Qt Designer and PySide6\n"
"# V: 1.0.0\n"
"#\n"
"# This project can be used freely for all uses, as long as they maintain the\n"
"# respective credits only in the Python scripts, any information in the visual\n"
"# interface (GUI) can be modified without any implication.\n"
"#\n"
"# There are limitations on Qt licenses if you want to use your products\n"
"# commercially, I recommend reading them on the official website:\n"
"# https://doc.qt.io/qtforpython/licenses.html\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: #4d5d5d;\n"
"	font: 12pt \"\u7b49\u8ddd\u66f4\u7eb1\u9ed1\u4f53 SC\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////"
                        "////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #4d5d5d;\n"
"	background-color: #f8f8f2;\n"
"	border: 1px solid #CCC;\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid #9ac9c3;\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-color: #f8f8f2;\n"
"	border: 1px solid #CCC;\n"
"    color: #44475a;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: #fafafa;\n"
"}\n"
"#topLogo {\n"
"	background-color: #fafafa;\n"
"	background-image: url(:/images/images/images/garbage-classification.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe U"
                        "I Semibold\"; color: #f8f8f2; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: #bd93f9; }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #4d5d5d;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: #ddeeec;\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: #d5ebe7;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #4d5d5d;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: #ddeeec;\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: #d5ebe7;\n"
"	color: "
                        "rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid #ecf1f1;\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: #5b6996;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: #f8f8f2;\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: #ddeeec;\n"
"}\n"
"#toggleButton:pressed {	\n"
"	background-color: #d5ebe7;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: #495474;\n"
"    color: #f8f8f2;\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: "
                        "url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid #fafafa;\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: #e9f5f3;\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-co"
                        "lor: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: #fafafa;\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid #ecf1f1;\n"
"	border-left: 2px solid #ecf1f1;\n"
"}\n"
"#titleRightInfo{\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: #ddeeec; border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: #d5ebe7; border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: #495474; }\n"
"#themeSettingsTopDetail { background-color: #fafafa; }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: #495474 }\n"
"#bottomBar QLabel { font-size: 11px; color: #f8f8f2;"
                        " padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: #5d6c99;\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: #9faeda;\n"
"    outline: none;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: #9faeda;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: #9faeda;\n"
""
                        "}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"    color: #f8f8f2;\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: #fafafa;\n"
"	max-width: 30px;\n"
"	border: none;\n"
"	border-style: none;\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: #fafafa;\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid #fafafa;\n"
"	background-color: #fafafa;\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    color: #f8f8f2;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid #fafafa;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: #fafafa;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #fafafa;\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(32, 41, 61);\n"
"	selection-background-color: #c3dfdb;\n"
"    color: #4d5d5d;\n"
"}\n"
"QLineEdit:hover {\n"
"	border"
                        ": 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #7495a5;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: #fafafa;\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(63, 38, 207);\n"
"    color: #f8f8f2;\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid #7495a5;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #fafafa;\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QSc"
                        "rollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: #fafafa;\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: #fafafa;\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background-color: #fafafa;\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
""
                        " }\n"
" QScrollBar::handle:vertical {	\n"
"	background: #ddeeec;\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: #fafafa;\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: #fafafa;\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: #d5ebe7;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"   "
                        " border: 3px solid #8ca09a;\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: #fafafa;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(119, 136, 187);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid #b9d6d3;\n"
"	border: 3px solid #565a5e;	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid #fafafa;\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: #fafafa;\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(119, 136, 187);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid #bd93f9;\n"
"	border: 3px solid #bd93f9;	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboB"
                        "ox{\n"
"	background-color: #fafafa;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #fafafa;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid #7284b9;\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: #fafafa;\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"\n"
"	background-color: #fafafa;\n"
"	padding: 10px;\n"
"	selection-background-color: #fafafa;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: #faf"
                        "afa;\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: #fafafa;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: #ddeeec;\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: #d5ebe7;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: #fafafa;\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: #fafafa;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color:  #ddeeec;\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: #d5ebe7;\n"
"}\n"
"\n"
"/"
                        "* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"#pagesContainer QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"    border: 2px solid #ff79c6;\n"
"    color: #ff79c6;\n"
"}\n"
"#pagesContainer QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: #fafafa;\n"
"}\n"
"#pagesContainer QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: #586796;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid #fafafa;\n"
"	border-radius: 5px;	\n"
"	background-color: #fafafa;\n"
"    color: #4d5d5d;\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: #546391;\n"
"	border: 2px"
                        " solid #d5ebe7;\n"
"}\n"
"\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setMinimumSize(QSize(1083, 695))
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setLayoutDirection(Qt.LeftToRight)
        self.topLogo.setAutoFillBackground(False)
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        self.titleLeftApp.setFont(font)
        self.titleLeftApp.setStyleSheet(u"color: #4d5d5d;\n"
"font: 12pt \"\u7b49\u8ddd\u66f4\u7eb1\u9ed1\u4f53 SC\";")
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font1 = QFont()
        font1.setFamilies([u"\u7b49\u8ddd\u66f4\u7eb1\u9ed1\u4f53 SC"])
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftDescription.setFont(font1)
        self.titleLeftDescription.setStyleSheet(u"color: #8cccc8;\n"
"font: 11pt \"\u7b49\u8ddd\u66f4\u7eb1\u9ed1\u4f53 SC\";")
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background: #fafafa;\n"
"background-image: url(:/icons/images/icons/icon_menu.png);\n"
"background-position: left;\n"
"background-repeat: no-reperat;\n"
"color: #4d5d5d;")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_pro_switch = QPushButton(self.topMenu)
        self.btn_pro_switch.setObjectName(u"btn_pro_switch")
        sizePolicy.setHeightForWidth(self.btn_pro_switch.sizePolicy().hasHeightForWidth())
        self.btn_pro_switch.setSizePolicy(sizePolicy)
        self.btn_pro_switch.setMinimumSize(QSize(0, 45))
        self.btn_pro_switch.setFont(font)
        self.btn_pro_switch.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pro_switch.setLayoutDirection(Qt.LeftToRight)
        self.btn_pro_switch.setStyleSheet(u"background-image: url(:/icons/images/icons/icon-pro.png);")
        self.btn_pro_switch.setIconSize(QSize(16, 16))

        self.verticalLayout_8.addWidget(self.btn_pro_switch)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_settings = QPushButton(self.bottomMenu)
        self.btn_settings.setObjectName(u"btn_settings")
        sizePolicy.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy)
        self.btn_settings.setMinimumSize(QSize(0, 45))
        self.btn_settings.setFont(font)
        self.btn_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_settings.setLayoutDirection(Qt.LeftToRight)
        self.btn_settings.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.btn_settings)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font2 = QFont()
        font2.setFamilies([u"\u7b49\u8ddd\u66f4\u7eb1\u9ed1\u4f53 SC"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font2)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_welcome = QWidget()
        self.page_welcome.setObjectName(u"page_welcome")
        self.page_welcome.setStyleSheet(u"\n"
"background-image: url(:/images/images/images/\u6b22\u8fce\u9875\u80cc\u666f\u56fe.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.stackedWidget.addWidget(self.page_welcome)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.checkBox_GPU = QCheckBox(self.page_settings)
        self.checkBox_GPU.setObjectName(u"checkBox_GPU")
        self.checkBox_GPU.setGeometry(QRect(110, 100, 171, 21))
        self.comboBox_setting_default_net_choooser = QComboBox(self.page_settings)
        self.comboBox_setting_default_net_choooser.setObjectName(u"comboBox_setting_default_net_choooser")
        self.comboBox_setting_default_net_choooser.setEnabled(True)
        self.comboBox_setting_default_net_choooser.setGeometry(QRect(210, 140, 211, 38))
        self.comboBox_setting_default_net_choooser.setMinimumSize(QSize(211, 0))
        self.comboBox_setting_default_net_choooser.setStyleSheet(u"background-color: #ecf1f1;")
        self.label_default_model = QLabel(self.page_settings)
        self.label_default_model.setObjectName(u"label_default_model")
        self.label_default_model.setGeometry(QRect(110, 150, 81, 16))
        self.label_default_model.setFont(font)
        self.label_default_model.setStyleSheet(u"")
        self.stackedWidget.addWidget(self.page_settings)
        self.home_basic = QWidget()
        self.home_basic.setObjectName(u"home_basic")
        self.home_basic.setEnabled(True)
        self.home_basic.setStyleSheet(u"background-position: center;\n"
"background-repeat: no-repeat;")
        self.layoutWidget = QWidget(self.home_basic)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(31, 51, 1014, 530))
        self.gridLayout_8 = QGridLayout(self.layoutWidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.btn_basic_garbage_classification = QPushButton(self.layoutWidget)
        self.btn_basic_garbage_classification.setObjectName(u"btn_basic_garbage_classification")
        self.btn_basic_garbage_classification.setEnabled(True)
        self.btn_basic_garbage_classification.setMinimumSize(QSize(131, 41))
        self.btn_basic_garbage_classification.setStyleSheet(u"background-color: #ecf1f1;")

        self.gridLayout_5.addWidget(self.btn_basic_garbage_classification, 1, 1, 1, 1)

        self.btn_basic_choose_pic = QPushButton(self.layoutWidget)
        self.btn_basic_choose_pic.setObjectName(u"btn_basic_choose_pic")
        self.btn_basic_choose_pic.setMinimumSize(QSize(131, 41))
        self.btn_basic_choose_pic.setStyleSheet(u"background-color: #ecf1f1;")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_basic_choose_pic.setIcon(icon3)

        self.gridLayout_5.addWidget(self.btn_basic_choose_pic, 0, 0, 1, 1)

        self.lineEdit_basic_pic_addr = QLineEdit(self.layoutWidget)
        self.lineEdit_basic_pic_addr.setObjectName(u"lineEdit_basic_pic_addr")
        self.lineEdit_basic_pic_addr.setMinimumSize(QSize(0, 41))
        self.lineEdit_basic_pic_addr.setToolTipDuration(0)
        self.lineEdit_basic_pic_addr.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_basic_pic_addr.setStyleSheet(u"background-color: #ecf1f1;")
        self.lineEdit_basic_pic_addr.setAlignment(Qt.AlignCenter)
        self.lineEdit_basic_pic_addr.setReadOnly(True)

        self.gridLayout_5.addWidget(self.lineEdit_basic_pic_addr, 0, 1, 1, 1)

        self.btn_basic_crop = QPushButton(self.layoutWidget)
        self.btn_basic_crop.setObjectName(u"btn_basic_crop")
        self.btn_basic_crop.setMinimumSize(QSize(131, 41))
        self.btn_basic_crop.setStyleSheet(u"background-color: #ecf1f1;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/crop_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_basic_crop.setIcon(icon4)

        self.gridLayout_5.addWidget(self.btn_basic_crop, 1, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.btn_basic_feedback = QPushButton(self.layoutWidget)
        self.btn_basic_feedback.setObjectName(u"btn_basic_feedback")
        self.btn_basic_feedback.setEnabled(True)
        self.btn_basic_feedback.setMinimumSize(QSize(481, 41))
        self.btn_basic_feedback.setStyleSheet(u"background-color: #ecf1f1;")

        self.gridLayout_6.addWidget(self.btn_basic_feedback, 1, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_6, 2, 0, 1, 1)

        self.basicpicturelabel = QLabel(self.layoutWidget)
        self.basicpicturelabel.setObjectName(u"basicpicturelabel")
        self.basicpicturelabel.setMinimumSize(QSize(519, 381))
        self.basicpicturelabel.setMaximumSize(QSize(519, 381))
        self.basicpicturelabel.setStyleSheet(u"background-image: url(:/images/images/images/label_default_pic.png); ")

        self.gridLayout_7.addWidget(self.basicpicturelabel, 1, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.lineEdit_basic_dir_addr = QLineEdit(self.layoutWidget)
        self.lineEdit_basic_dir_addr.setObjectName(u"lineEdit_basic_dir_addr")
        self.lineEdit_basic_dir_addr.setMinimumSize(QSize(0, 41))
        self.lineEdit_basic_dir_addr.setToolTipDuration(0)
        self.lineEdit_basic_dir_addr.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_basic_dir_addr.setStyleSheet(u"background-color: #ecf1f1;")
        self.lineEdit_basic_dir_addr.setAlignment(Qt.AlignCenter)
        self.lineEdit_basic_dir_addr.setReadOnly(True)

        self.gridLayout_10.addWidget(self.lineEdit_basic_dir_addr, 0, 1, 1, 2)

        self.btn_basic_batch_classification = QPushButton(self.layoutWidget)
        self.btn_basic_batch_classification.setObjectName(u"btn_basic_batch_classification")
        self.btn_basic_batch_classification.setEnabled(True)
        self.btn_basic_batch_classification.setMinimumSize(QSize(481, 41))
        self.btn_basic_batch_classification.setStyleSheet(u"background-color: #ecf1f1;")

        self.gridLayout_10.addWidget(self.btn_basic_batch_classification, 1, 0, 1, 3)

        self.btn_basic_choose_dir = QPushButton(self.layoutWidget)
        self.btn_basic_choose_dir.setObjectName(u"btn_basic_choose_dir")
        self.btn_basic_choose_dir.setMinimumSize(QSize(131, 41))
        self.btn_basic_choose_dir.setStyleSheet(u"background-color: #ecf1f1;")
        self.btn_basic_choose_dir.setIcon(icon3)

        self.gridLayout_10.addWidget(self.btn_basic_choose_dir, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_10, 0, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.checkBox_basic_default_model = QCheckBox(self.layoutWidget)
        self.checkBox_basic_default_model.setObjectName(u"checkBox_basic_default_model")
        self.checkBox_basic_default_model.setMinimumSize(QSize(152, 0))
        self.checkBox_basic_default_model.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.checkBox_basic_default_model, 0, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.comboBox_basic_net_choooser = QComboBox(self.layoutWidget)
        self.comboBox_basic_net_choooser.setObjectName(u"comboBox_basic_net_choooser")
        self.comboBox_basic_net_choooser.setEnabled(True)
        self.comboBox_basic_net_choooser.setMinimumSize(QSize(211, 0))
        self.comboBox_basic_net_choooser.setStyleSheet(u"background-color: #ecf1f1;")

        self.gridLayout_3.addWidget(self.comboBox_basic_net_choooser, 0, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_4, 1, 0, 1, 1)

        self.label_basic_log = QLabel(self.layoutWidget)
        self.label_basic_log.setObjectName(u"label_basic_log")
        self.label_basic_log.setMinimumSize(QSize(471, 17))

        self.gridLayout_2.addWidget(self.label_basic_log, 2, 0, 1, 1)

        self.textBrowser_basic_log = QTextBrowser(self.layoutWidget)
        self.textBrowser_basic_log.setObjectName(u"textBrowser_basic_log")
        self.textBrowser_basic_log.setMinimumSize(QSize(481, 150))
        self.textBrowser_basic_log.setFont(font)
        self.textBrowser_basic_log.setStyleSheet(u"color: #252825;\n"
"border: 0;")

        self.gridLayout_2.addWidget(self.textBrowser_basic_log, 3, 0, 1, 1)

        self.label_basic_tip_res = QLabel(self.layoutWidget)
        self.label_basic_tip_res.setObjectName(u"label_basic_tip_res")
        self.label_basic_tip_res.setMinimumSize(QSize(481, 35))

        self.gridLayout_2.addWidget(self.label_basic_tip_res, 4, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(238, 100))
        self.label_3.setMaximumSize(QSize(238, 100))

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_basic_classification_result_2 = QLabel(self.layoutWidget)
        self.label_basic_classification_result_2.setObjectName(u"label_basic_classification_result_2")
        self.label_basic_classification_result_2.setMinimumSize(QSize(237, 100))
        self.label_basic_classification_result_2.setMaximumSize(QSize(237, 100))
        self.label_basic_classification_result_2.setStyleSheet(u"color: #ff475f;\n"
"font: 18pt \"\u7b49\u8ddd\u66f4\u7eb1\u9ed1\u4f53 SC\";\n"
"background-image: url(:/images/images/images/label_bg.jpg); ")
        self.label_basic_classification_result_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_basic_classification_result_2, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 5, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_2, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.home_basic)
        self.page_feedback = QWidget()
        self.page_feedback.setObjectName(u"page_feedback")
        self.btn_page_feedback_submit = QPushButton(self.page_feedback)
        self.btn_page_feedback_submit.setObjectName(u"btn_page_feedback_submit")
        self.btn_page_feedback_submit.setEnabled(True)
        self.btn_page_feedback_submit.setGeometry(QRect(280, 300, 481, 41))
        self.btn_page_feedback_submit.setMinimumSize(QSize(131, 41))
        self.btn_page_feedback_submit.setStyleSheet(u"background-color: #ecf1f1;")
        self.btn_page_feedback_submit.setCheckable(False)
        self.comboBox_feedback = QComboBox(self.page_feedback)
        self.comboBox_feedback.setObjectName(u"comboBox_feedback")
        self.comboBox_feedback.setEnabled(True)
        self.comboBox_feedback.setGeometry(QRect(420, 240, 341, 36))
        self.comboBox_feedback.setMinimumSize(QSize(211, 0))
        self.comboBox_feedback.setStyleSheet(u"background-color: #ecf1f1;")
        self.label_3_feedback = QLabel(self.page_feedback)
        self.label_3_feedback.setObjectName(u"label_3_feedback")
        self.label_3_feedback.setGeometry(QRect(280, 240, 131, 36))
        self.stackedWidget.addWidget(self.page_feedback)
        self.page_pro = QWidget()
        self.page_pro.setObjectName(u"page_pro")
        self.label_please_choose_dataset = QLabel(self.page_pro)
        self.label_please_choose_dataset.setObjectName(u"label_please_choose_dataset")
        self.label_please_choose_dataset.setGeometry(QRect(80, 80, 121, 41))
        self.label_pro_epoch = QLabel(self.page_pro)
        self.label_pro_epoch.setObjectName(u"label_pro_epoch")
        self.label_pro_epoch.setGeometry(QRect(90, 210, 71, 40))
        self.label_pro_epoch.setMinimumSize(QSize(0, 40))
        self.lineEdit_pro_lr = QLineEdit(self.page_pro)
        self.lineEdit_pro_lr.setObjectName(u"lineEdit_pro_lr")
        self.lineEdit_pro_lr.setGeometry(QRect(190, 320, 120, 40))
        self.lineEdit_pro_lr.setMinimumSize(QSize(0, 40))
        self.lineEdit_pro_lr.setStyleSheet(u"background-color: #ecf1f1;")
        self.label_pro_lr = QLabel(self.page_pro)
        self.label_pro_lr.setObjectName(u"label_pro_lr")
        self.label_pro_lr.setGeometry(QRect(90, 318, 61, 40))
        self.label_pro_lr.setMinimumSize(QSize(0, 40))
        self.comboBox_pro_dataset_chooser_2 = QComboBox(self.page_pro)
        self.comboBox_pro_dataset_chooser_2.setObjectName(u"comboBox_pro_dataset_chooser_2")
        self.comboBox_pro_dataset_chooser_2.setEnabled(True)
        self.comboBox_pro_dataset_chooser_2.setGeometry(QRect(190, 70, 241, 51))
        self.comboBox_pro_dataset_chooser_2.setStyleSheet(u"background-color: #ecf1f1;")
        self.label_pro_tip_4_each = QLabel(self.page_pro)
        self.label_pro_tip_4_each.setObjectName(u"label_pro_tip_4_each")
        self.label_pro_tip_4_each.setGeometry(QRect(70, 380, 31, 40))
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_pro_tip_4_each.sizePolicy().hasHeightForWidth())
        self.label_pro_tip_4_each.setSizePolicy(sizePolicy2)
        self.label_pro_tip_4_each.setMinimumSize(QSize(0, 40))
        self.label_pro_pic = QLabel(self.page_pro)
        self.label_pro_pic.setObjectName(u"label_pro_pic")
        self.label_pro_pic.setGeometry(QRect(460, 140, 500, 400))
        self.label_pro_pic.setStyleSheet(u"background-color: #ecf1f1;")
        self.label_pro_pic.setMargin(0)
        self.label_pro_arguments_for_training = QLabel(self.page_pro)
        self.label_pro_arguments_for_training.setObjectName(u"label_pro_arguments_for_training")
        self.label_pro_arguments_for_training.setGeometry(QRect(88, 155, 200, 40))
        sizePolicy.setHeightForWidth(self.label_pro_arguments_for_training.sizePolicy().hasHeightForWidth())
        self.label_pro_arguments_for_training.setSizePolicy(sizePolicy)
        self.label_pro_arguments_for_training.setMinimumSize(QSize(0, 40))
        self.label_pro_arguments_for_training.setAcceptDrops(True)
        self.btn_pro_start_training = QPushButton(self.page_pro)
        self.btn_pro_start_training.setObjectName(u"btn_pro_start_training")
        self.btn_pro_start_training.setGeometry(QRect(80, 450, 181, 51))
        self.btn_pro_start_training.setStyleSheet(u"background-color: #ecf1f1;")
        self.lineEdit_pro_batch = QLineEdit(self.page_pro)
        self.lineEdit_pro_batch.setObjectName(u"lineEdit_pro_batch")
        self.lineEdit_pro_batch.setGeometry(QRect(190, 266, 121, 40))
        self.lineEdit_pro_batch.setMinimumSize(QSize(0, 40))
        self.lineEdit_pro_batch.setStyleSheet(u"background-color: #ecf1f1;")
        self.lineEdit_pro_saveevery_epoch = QLineEdit(self.page_pro)
        self.lineEdit_pro_saveevery_epoch.setObjectName(u"lineEdit_pro_saveevery_epoch")
        self.lineEdit_pro_saveevery_epoch.setGeometry(QRect(110, 380, 111, 40))
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit_pro_saveevery_epoch.sizePolicy().hasHeightForWidth())
        self.lineEdit_pro_saveevery_epoch.setSizePolicy(sizePolicy3)
        self.lineEdit_pro_saveevery_epoch.setMinimumSize(QSize(0, 40))
        self.lineEdit_pro_saveevery_epoch.setStyleSheet(u"background-color: #ecf1f1;")
        self.label_pro_batch_size = QLabel(self.page_pro)
        self.label_pro_batch_size.setObjectName(u"label_pro_batch_size")
        self.label_pro_batch_size.setGeometry(QRect(90, 268, 91, 40))
        self.label_pro_batch_size.setMinimumSize(QSize(0, 40))
        self.lineEdit_pro_epoch = QLineEdit(self.page_pro)
        self.lineEdit_pro_epoch.setObjectName(u"lineEdit_pro_epoch")
        self.lineEdit_pro_epoch.setGeometry(QRect(190, 212, 120, 40))
        self.lineEdit_pro_epoch.setMinimumSize(QSize(0, 40))
        self.lineEdit_pro_epoch.setStyleSheet(u"background-color: #ecf1f1;")
        self.label_pro_tip_epoch_to_save = QLabel(self.page_pro)
        self.label_pro_tip_epoch_to_save.setObjectName(u"label_pro_tip_epoch_to_save")
        self.label_pro_tip_epoch_to_save.setGeometry(QRect(230, 380, 191, 40))
        self.label_pro_tip_epoch_to_save.setMinimumSize(QSize(0, 40))
        self.comboBox_pro_premodel_chooser = QComboBox(self.page_pro)
        self.comboBox_pro_premodel_chooser.setObjectName(u"comboBox_pro_premodel_chooser")
        self.comboBox_pro_premodel_chooser.setEnabled(True)
        self.comboBox_pro_premodel_chooser.setGeometry(QRect(610, 70, 161, 51))
        self.comboBox_pro_premodel_chooser.setStyleSheet(u"background-color: #ecf1f1;")
        self.label_please_choose_dataset_2 = QLabel(self.page_pro)
        self.label_please_choose_dataset_2.setObjectName(u"label_please_choose_dataset_2")
        self.label_please_choose_dataset_2.setGeometry(QRect(460, 80, 121, 41))
        self.label = QLabel(self.page_pro)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 510, 281, 31))
        self.label.setStyleSheet(u"color: red;\n"
"font: 14pt \"\u7b49\u8ddd\u66f4\u7eb1\u9ed1\u4f53 SC\";")
        self.stackedWidget.addWidget(self.page_pro)
        self.page_batch_classification = QWidget()
        self.page_batch_classification.setObjectName(u"page_batch_classification")
        self.stackedWidget.addWidget(self.page_batch_classification)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setStyleSheet(u"background-color: #ecf1f1")
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font3 = QFont()
        font3.setFamilies([u"\u7b49\u8ddd\u66f4\u7eb1\u9ed1\u4f53 SC"])
        font3.setBold(False)
        font3.setItalic(False)
        self.creditsLabel.setFont(font3)
        self.creditsLabel.setStyleSheet(u"color: #4d5d5d;")
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setStyleSheet(u"color: #4d5d5d;")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.comboBox_setting_default_net_choooser.setCurrentIndex(-1)
        self.comboBox_basic_net_choooser.setCurrentIndex(-1)
        self.comboBox_feedback.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"14\u7ec4-\u5783\u573e\u5206\u7c7b\u7cfb\u7edf", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"\u667a\u4eab\u73af\u4fdd\u751f\u6d3b~", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"\u518d\u6b21\u70b9\u51fb\u6536\u8d77\u83dc\u5355", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Basic", None))
        self.btn_pro_switch.setText(QCoreApplication.translate("MainWindow", u"Pro", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u7b49\u8ddd\u66f4\u7eb1\u9ed1\u4f53 SC'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-"
                        "top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:1"
                        "2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.checkBox_GPU.setText(QCoreApplication.translate("MainWindow", u"\u9009\u4e2d\u4ee5\u542f\u7528GPU\u52a0\u901f", None))
        self.comboBox_setting_default_net_choooser.setCurrentText("")
        self.label_default_model.setText(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u6a21\u578b\uff1a", None))
        self.btn_basic_garbage_classification.setText(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b\u5783\u573e\u7c7b\u522b", None))
        self.btn_basic_choose_pic.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u56fe\u7247", None))
        self.lineEdit_basic_pic_addr.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u56fe\u7247\u6587\u4ef6", None))
        self.lineEdit_basic_pic_addr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.btn_basic_crop.setText(QCoreApplication.translate("MainWindow", u"\u526a\u88c1\u56fe\u7247", None))
        self.btn_basic_feedback.setText(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b\u7ed3\u679c\u53cd\u9988", None))
        self.basicpicturelabel.setText("")
        self.lineEdit_basic_dir_addr.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u6279\u91cf\u8bc6\u522b\u7684\u8def\u5f84", None))
        self.lineEdit_basic_dir_addr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.btn_basic_batch_classification.setText(QCoreApplication.translate("MainWindow", u"\u6279\u91cf\u8bc6\u522b\u5783\u573e\u7c7b\u522b", None))
        self.btn_basic_choose_dir.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6\u5939\u8def\u5f84", None))
        self.checkBox_basic_default_model.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u9ed8\u8ba4\u6a21\u578b", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u7f51\u7edc\u9009\u62e9\uff1a", None))
        self.comboBox_basic_net_choooser.setCurrentText("")
        self.label_basic_log.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7\uff1a", None))
        self.textBrowser_basic_log.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u7b49\u8ddd\u66f4\u7eb1\u9ed1\u4f53 SC'; font-size:12pt; font-weight:400; font-style:normal;\" bgcolor=\"#f9fcf5\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_basic_tip_res.setText(QCoreApplication.translate("MainWindow", u"\u5783\u573e\u56fe\u7247\u8bc6\u522b\u7ed3\u679c\uff1a", None))
        self.label_3.setText("")
        self.label_basic_classification_result_2.setText(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b\u7ed3\u679c", None))
        self.btn_page_feedback_submit.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4", None))
        self.comboBox_feedback.setCurrentText("")
        self.label_3_feedback.setText(QCoreApplication.translate("MainWindow", u"\u60a8\u671f\u671b\u7684\u6b63\u786e\u5206\u7c7b", None))
        self.label_please_choose_dataset.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u6570\u636e\u96c6", None))
        self.label_pro_epoch.setText(QCoreApplication.translate("MainWindow", u"Epoch", None))
        self.lineEdit_pro_lr.setText(QCoreApplication.translate("MainWindow", u"0.0001", None))
        self.label_pro_lr.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u4e60\u7387", None))
        self.label_pro_tip_4_each.setText(QCoreApplication.translate("MainWindow", u"  \u6bcf", None))
        self.label_pro_pic.setText("")
        self.label_pro_arguments_for_training.setText(QCoreApplication.translate("MainWindow", u"\u8bad\u7ec3\u53c2\u6570\u8bbe\u7f6e                                       ", None))
        self.btn_pro_start_training.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8bad\u7ec3", None))
        self.lineEdit_pro_batch.setText(QCoreApplication.translate("MainWindow", u"32", None))
        self.lineEdit_pro_saveevery_epoch.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_pro_batch_size.setText(QCoreApplication.translate("MainWindow", u"Batch Size", None))
        self.lineEdit_pro_epoch.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.label_pro_tip_epoch_to_save.setText(QCoreApplication.translate("MainWindow", u"\u4e2a Epoch \u4fdd\u5b58\u4e00\u6b21\u6a21\u578b", None))
        self.label_please_choose_dataset_2.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u4e8e\u9884\u8bad\u7ec3\u6a21\u578b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u6b63\u786e\u7684\u8bad\u7ec3\u53c2\u6570", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: \u7b2c 14 \u7ec4", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.1 \u5b9e\u8bad\u7279\u4f9b\u7248", None))
    # retranslateUi

