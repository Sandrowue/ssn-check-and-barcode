# Käännetystä Käyttöliittymätiedostosta pääikkunan luominen

import os
import sys

from PySide6 import QtWidgets
from MainWindow import Ui_MainWindow

# Määritellään luokka joka perii QMainWindow- ja Ui_MainWindow
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # luodaan käyttöliittymä konvertoidun tiedoston perusteella MainWindown ui-ominaisuudeksi.
        # Tämä suojaa lopun MainWindow olion ylikirjoitukselta
        self.ui = Ui_MainWindow()

        # Kutsutaa käyttöliittymän muodostusmetodia setupUI
        self.ui.setupUi(self)

        # Ohjelmoitut signaalit
        # Kun Tulosta painiketta on klikattu, kutsutaan updatePrintedLabel-metodia# Itseohjelmoidut
        self.ui.tulostaPushButton.clicked.connect(self.updatePrintedLabel)
        self.ui.varoitaPushButton.clicked.connect(self.openWarning)

    # OHJELMOIDUT SLOTIT
    # Muutetaan tulostettuLabel:n sisältö: teksti ja väri
    def updatePrintedLabel(self):
        self.ui.tulostusStatusLabel.setText("Tulostettu")
        self.ui.tulostusStatusLabel.setStyleSheet(u"color: green")

    # Avataan MessageBox
    def openWarning(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle('Hirveetä!')
        msgBox.setText('Jotain kamalaa tapahtui :(')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()
# Luodaan sovellus ja käynnistetään se
app = QtWidgets.QApplication(sys.argv)

# Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
window = MainWindow()
window.show()

# Käynnistetään sovellus ja tapahtumakäsittelijä
app.exec()