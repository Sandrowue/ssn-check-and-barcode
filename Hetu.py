# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hetu.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1109, 960)
        MainWindow.setToolTipDuration(5000)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ssnLineEdit = QLineEdit(self.centralwidget)
        self.ssnLineEdit.setObjectName(u"ssnLineEdit")
        self.ssnLineEdit.setGeometry(QRect(60, 60, 180, 35))
        font = QFont()
        font.setPointSize(18)
        self.ssnLineEdit.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 30, 160, 30))
        self.label.setFont(font)
        self.firstNameLineEdit_2 = QLineEdit(self.centralwidget)
        self.firstNameLineEdit_2.setObjectName(u"firstNameLineEdit_2")
        self.firstNameLineEdit_2.setGeometry(QRect(60, 130, 180, 35))
        self.firstNameLineEdit_2.setFont(font)
        self.LastNameLineEdit_2 = QLineEdit(self.centralwidget)
        self.LastNameLineEdit_2.setObjectName(u"LastNameLineEdit_2")
        self.LastNameLineEdit_2.setGeometry(QRect(280, 130, 180, 35))
        self.LastNameLineEdit_2.setFont(font)
        self.firstNameLabel = QLabel(self.centralwidget)
        self.firstNameLabel.setObjectName(u"firstNameLabel")
        self.firstNameLabel.setGeometry(QRect(60, 100, 160, 30))
        self.firstNameLabel.setFont(font)
        self.lastNameLabel = QLabel(self.centralwidget)
        self.lastNameLabel.setObjectName(u"lastNameLabel")
        self.lastNameLabel.setGeometry(QRect(280, 100, 160, 30))
        self.lastNameLabel.setFont(font)
        self.barcodeLabel = QLabel(self.centralwidget)
        self.barcodeLabel.setObjectName(u"barcodeLabel")
        self.barcodeLabel.setGeometry(QRect(60, 200, 300, 60))
        font1 = QFont()
        font1.setFamilies([u"Libre Barcode 128 Text"])
        font1.setPointSize(30)
        self.barcodeLabel.setFont(font1)
        self.printPushButton = QPushButton(self.centralwidget)
        self.printPushButton.setObjectName(u"printPushButton")
        self.printPushButton.setGeometry(QRect(280, 210, 100, 40))
        self.printPushButton.setFont(font)
        self.printPushButton.setStyleSheet(u"background-color: rgb(170, 170, 255);\n"
"color: rgb(0, 0, 127);\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.printAmountspinBox = QSpinBox(self.centralwidget)
        self.printAmountspinBox.setObjectName(u"printAmountspinBox")
        self.printAmountspinBox.setGeometry(QRect(390, 210, 65, 40))
        self.printAmountspinBox.setFont(font)
        self.printAmountspinBox.setMaximum(999)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1109, 21))
        MainWindow.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.ssnLineEdit, self.firstNameLineEdit_2)
        QWidget.setTabOrder(self.firstNameLineEdit_2, self.LastNameLineEdit_2)
        QWidget.setTabOrder(self.LastNameLineEdit_2, self.printAmountspinBox)
        QWidget.setTabOrder(self.printAmountspinBox, self.printPushButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip(QCoreApplication.translate("MainWindow", u"Suomalainen Henkil\u00f6tunnus", None))
#endif // QT_CONFIG(tooltip)
        self.ssnLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ppkkvv-111A", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Henkil\u00f6tunnus:", None))
        self.firstNameLabel.setText(QCoreApplication.translate("MainWindow", u"Etunimi:", None))
        self.lastNameLabel.setText(QCoreApplication.translate("MainWindow", u"Sukunimi:", None))
        self.barcodeLabel.setText(QCoreApplication.translate("MainWindow", u"Barcode 128", None))
        self.printPushButton.setText(QCoreApplication.translate("MainWindow", u"Tulosta", None))
    # retranslateUi

