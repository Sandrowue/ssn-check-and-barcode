# Käännetystä Käyttöliittymätiedostosta pääikkunan luominen 
# HETU Barcode sovellus

import os
import sys

from PySide6 import QtWidgets
from Hetu import Ui_MainWindow

import identityCheck2 # Henkilötunnuksen tarkistukseen liittyvät työkalut
import barcode # Viivakoodin muodostukseen tarvittavat funktiot
from avtools import sound # Äänitoiminnot

# Määritellään luokka joka perii QMainWindow- ja Ui_MainWindow
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # luodaan käyttöliittymä konvertoidun tiedoston perusteella MainWindown ui-ominaisuudeksi.
        # Tämä suojaa lopun MainWindow olion ylikirjoitukselta
        self.ui = Ui_MainWindow()

        # Kutsutaa käyttöliittymän muodostusmetodia setupUI
        self.ui.setupUi(self)

        # Kun poistutaan ssnLineEdit-elementistä suoritetaan barcodeLabel-elementin päivitys
        self.ui.ssnLineEdit.editingFinished.connect(self.updateBarcodeLabel)

    # OHJELMOIDUT SLOTIT
    # Viivakoodin muodostus ja barcodeLabel:n päivitys
    def updateBarcodeLabel(self):
        # Tarkistetaan, että henkilötunnus on oikein muodostettu
        uiSsn = self.ui.ssnLineEdit.text().upper() # Luetaan käyttöliittymästä henkilötunnus
        ssnToCheck = identityCheck2.NationalSSN(uiSsn) # Luodaan henkilötunnusobjekti
        # Jos se on oikein, luodaan viivakoodi
        if ssnToCheck.isValidSsn():
            barcode128 = barcode.Code128B(uiSsn) # Luodaan viivakoodi-olio
            barCodeToPrint = barcode128.buildBarcode() # Lisätään alku- ja loppumerkki sekä varmistussumma
            self.ui.barcodeLabel.setText(barCodeToPrint) # Päivitetään käyttöliittymän barcodeLabel

        # Jos se on muodostettu väärin näytetään virheilmoitus MessageBox-ikkunassa
        else:
            self.errorTitle = 'Henkilötunnus virheellinen!'
            self.errorText = ssnToCheck.errorMessage
            self.openErrorMsgBox(self.errorTitle, self.errorText)
        
    # Avataan ErrorMessageBox
    def openErrorMsgBox(self, errorTitle, errorText):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle(errorTitle)
        msgBox.setText(errorText)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()

if __name__ == "__main__":
    # Luodaan sovellus ja käynnistetään se
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')

    # Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
    window = MainWindow()
    window.show()

    # Käynnistetään sovellus ja tapahtumakäsittelijä
    app.exec()