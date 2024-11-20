# MALLIPOHJA QT-SOVELLUKSEN RAKENTAMISEEN

# PYSIDE 6 MALLINEN SOVELLUKSEN PÄÄIKKUNA

# KIRJASTOJEN JA MODUULIEN LATAUKSET

# Järjestelmäkomentojen kirjasto
import sys # Tarvitaan sovelluksen argumenttien käsittelyyn
import os # Tarvitaan mm. hakemistopolkujen käsittelyyn

# Pyside kirjastot

from PySide6 import QtCore, QtGui, QtWidgets # Tärkeimmät Qt:n moduulit
from PySide6.QtUiTools import QUiLoader # Tarvitaan käyttöliitymätiedoston lataamiseen

#   luodaan käyttöliittymätiedoston lataajaobjekti QUiLoader-luokasta
loader = QUiLoader()

# Määritellään sovellusobjekti
app = QtWidgets.QApplication(sys.argv)

# Luodaan pääikkunan objekti ui-tiedoston perusteella, pääikkunalla ei ole isäntäobjekti
window = loader.load("hetu.ui", None)

# Asetetaan päåäikkunan nimi
window.setWindowTitle("TÄMÄ ON PÄÄIKKUNA")

# Luodaan osoite(pointer), joka viitta käyttöliittymän elementtiin label
label = window.findChild(QtWidgets.QLabel, "label")

# Muutetaan label elementin sisällön
# label.setText('Muutettu tekstiä')

# Luodaan osoitin sovelluksen tilariville
statusBar = window.findChild(QtWidgets.QStatusBar, "statusbar")

# Kirjoitetaan teksti tilariville ja pidetään se näkyvissä koko ajan(-1)
statusBar.showMessage('Kaikki hyvin', -1)

# Määritllään ikkuna näkyväksi, oletuksena kaikki ikkunat ovat piilotettuja
window.show()

# Ajetaan sovellus, tämä luo tapahtumankäsittelijän (event loop)
# Python 2 sovelluksissa komento on app.exex_(), tuettu edelleen.
app.exec()