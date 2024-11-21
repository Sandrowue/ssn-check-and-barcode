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

        self.ui.printPushButton.setEnabled(False)

        # Kun poistutaan ssnLineEdit-elementistä suoritetaan barcodeLabel-elementin päivitys
        self.ui.ssnLineEdit.editingFinished.connect(self.updateBarcodeLabel)
        """self.ui.firstNameLineEdit_2.editingFinished.connect(self.beautyfyFirstName)
        self.ui.LastNameLineEdit_2.editingFinished.connect(self.beautyfyLastName)"""
        self.ui.firstNameLineEdit_2.editingFinished.connect(lambda: self.beautyfyElement(self.ui.firstNameLineEdit_2))
        self.ui.LastNameLineEdit_2.editingFinished.connect(lambda: self.beautyfyElement(self.ui.LastNameLineEdit_2))
        self.ui.printAmountspinBox.valueChanged.connect(self.enablePrintButton)
        
    # OHJELMOIDUT SLOTIT
    # Viivakoodin muodostus ja barcodeLabel:n päivitys
    def updateBarcodeLabel(self):
        # Tarkistetaan, että henkilötunnus on oikein muodostettu
        uiSsn = self.ui.ssnLineEdit.text().upper() # Luetaan käyttöliittymästä henkilötunnus
        ssnToCheck = identityCheck2.NationalSSN(uiSsn) # Luodaan henkilötunnusobjekti
        self.ui.ssnLineEdit.setText(uiSsn)
        # Jos se on oikein, luodaan viivakoodi
        if ssnToCheck.isValidSsn():
            barcode128 = barcode.Code128B(uiSsn) # Luodaan viivakoodi-olio
            barCodeToPrint = barcode128.buildBarcode() # Lisätään alku- ja loppumerkki sekä varmistussumma
            self.ui.barcodeLabel.setText(barCodeToPrint) # Päivitetään käyttöliittymän barcodeLabel
            age = ssnToCheck.calculateAge() # Lasketaan ikä
            ssnToCheck.getGender() # kutsutaan sukupuolen selvitys metodia
            gender = ssnToCheck.gender # Luetaan ikä-ominaisuuden arvo oliosta
            textToShow = f'Asiakas on {age} vuotias {gender}'
            timeToShow = 10000
            self.updateStatusbar(textToShow, timeToShow)

        # Jos se on muodostettu väärin näytetään virheilmoitus MessageBox-ikkunassa
        else:
            self.errorTitle = 'Henkilötunnus virheellinen!'
            self.errorText = ssnToCheck.errorMessage
            self.openErrorMsgBox(self.errorTitle, self.errorText)
            

    """ def beautyfyFirstName(self):
        firstName = self.ui.firstNameLineEdit_2.text()
        firstName = firstName.strip() # Poistetaan ylimääräiset välit
        firstName = firstName.title()
        self.ui.firstNameLineEdit_2.setText(firstName) 

    def beautyfyLastName(self):
        lastName = self.ui.LastNameLineEdit_2.text()
        lastName = lastName.strip().title()
        self.ui.LastNameLineEdit_2.setText(lastName) """
    
    def beautyfyElement(self, element):
        elementText = element.text()
        elementText = elementText.strip().title()
        element.setText(elementText)

    # Aktivoidaan tulostuspainike
    def enablePrintButton(self):
        if self.ui.ssnLineEdit.text != "":     
            self.ui.printPushButton.setEnabled(True)

    # Avataan ErrorMessageBox
    def openErrorMsgBox(self, errorTitle, errorText):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle(errorTitle)
        msgBox.setText(errorText)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()

    def updateStatusbar(self, textToShow, timeToShow=-1):
        self.ui.statusbar.showMessage(textToShow, timeToShow)

if __name__ == "__main__":
    # Luodaan sovellus ja käynnistetään se
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')

    # Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
    window = MainWindow()
    window.show()

    # Käynnistetään sovellus ja tapahtumakäsittelijä
    app.exec()