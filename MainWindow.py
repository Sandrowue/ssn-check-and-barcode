# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tulostaPushButton = QPushButton(self.centralwidget)
        self.tulostaPushButton.setObjectName(u"tulostaPushButton")
        self.tulostaPushButton.setGeometry(QRect(250, 140, 75, 23))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 140, 113, 20))
        self.showTextLabel = QLabel(self.centralwidget)
        self.showTextLabel.setObjectName(u"showTextLabel")
        self.showTextLabel.setGeometry(QRect(90, 190, 47, 13))
        self.languageGroupBox = QGroupBox(self.centralwidget)
        self.languageGroupBox.setObjectName(u"languageGroupBox")
        self.languageGroupBox.setGeometry(QRect(70, 270, 120, 131))
        self.suomiRadioButton = QRadioButton(self.languageGroupBox)
        self.suomiRadioButton.setObjectName(u"suomiRadioButton")
        self.suomiRadioButton.setGeometry(QRect(20, 30, 82, 17))
        self.englishRadioButton = QRadioButton(self.languageGroupBox)
        self.englishRadioButton.setObjectName(u"englishRadioButton")
        self.englishRadioButton.setGeometry(QRect(20, 60, 82, 17))
        self.tulostusStatusLabel = QLabel(self.centralwidget)
        self.tulostusStatusLabel.setObjectName(u"tulostusStatusLabel")
        self.tulostusStatusLabel.setGeometry(QRect(390, 140, 150, 30))
        font = QFont()
        font.setPointSize(16)
        self.tulostusStatusLabel.setFont(font)
        self.tulostusStatusLabel.setStyleSheet(u"\n"
"color: rgb(255, 0, 0);")
        self.varoitaPushButton = QPushButton(self.centralwidget)
        self.varoitaPushButton.setObjectName(u"varoitaPushButton")
        self.varoitaPushButton.setGeometry(QRect(250, 90, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.lineEdit.textEdited.connect(self.showTextLabel.setText)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tulostaPushButton.setText(QCoreApplication.translate("MainWindow", u"Tulosta", None))
        self.showTextLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.languageGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Kielivalinta", None))
        self.suomiRadioButton.setText(QCoreApplication.translate("MainWindow", u"Suomi", None))
        self.englishRadioButton.setText(QCoreApplication.translate("MainWindow", u"Englanti", None))
        self.tulostusStatusLabel.setText(QCoreApplication.translate("MainWindow", u"Ei tulostettu", None))
        self.varoitaPushButton.setText(QCoreApplication.translate("MainWindow", u"Varoitus", None))
    # retranslateUi

