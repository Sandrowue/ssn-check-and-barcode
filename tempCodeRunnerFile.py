    # Luodaan sovellus ja käynnistetään se
    app = QtWidgets.QApplication(sys.argv)

    # Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
    window = MainWindow()
    window.show()

    # Käynnistetään sovellus ja tapahtumakäsittelijä
    app.exec()