# TESTATAAN MODUULIN identityCheck2.py LUOKKIEN TOIMINTAA

import identityCheck2
import pytest

# Testeissä käytettävät henkilötunnukset
# --------------------------------------

testSsnOK = identityCheck2.NationalSSN('130728-478N')
testSsnShort = identityCheck2.NationalSSN('130728-78N')
testSsnLong = identityCheck2.NationalSSN('1300728-478N')
testSsnWrongDay = identityCheck2.NationalSSN('120728-478N')
testSsnWrongMonth = identityCheck2.NationalSSN('130628-478N')
testSsnWrongYear = identityCheck2.NationalSSN('130722-478N')
testSsnWrongCentury = identityCheck2.NationalSSN('130728x478N')
testSsnWrongNumber = identityCheck2.NationalSSN('130728-477N')
testSsnWrongCheckSum = identityCheck2.NationalSSN('130728-478A')
testSsnWrongCenturySymbol = identityCheck2.NationalSSN('130728x478N')

# Testitapaukset palautusarvojen ja ominaisuuksien päivittymisen testaamiseen
# ---------------------------------------------------------------------------

# Testitapaus 1: Hetun pituus on oikein -> True
def test_checkSsnLengthOK():
    assert testSsnOK.checkSsnLengthOk() == True

# Testitapaus 2: Henkilötunnuksen varmistussumma on oikein
def test_isValidSSN():
    assert testSsnOK.isValidSsn() == True
    

# Testitapaus 3: Henkilötunnuksen syntymäaika väärin -> False
def test_birthdayWrong():
    assert testSsnWrongDay.isValidSsn() == False
    assert testSsnWrongMonth.isValidSsn() == False
    assert testSsnWrongYear.isValidSsn() == False
    
# Testitapaus 4: Vuosisatamerkki väärin -> True (vuosisataa ei tarkisteta modulo 31)
def test_centuryWrong():
    assert testSsnWrongCentury.isValidSsn() == True

# Testitapaus 5: Iän laskenta, huom korjattava vuosittain testin tulos
def test_age():
    assert testSsnOK.calculateAge() == 96

# Testitapaus 6: Sukupuolen selvittämien 
def test_gender():
    testSsnOK.getGender()
    assert testSsnOK.gender == 'Nainen'

# Virhetilannetestit
# ------------------

# Testitapaus 7: liian lyhyen HeTu:n virheilmoitus, huom assert ei saa olla with:n sisällä
def test_tooShortError():
    with pytest.raises(ValueError) as exeptionMessage:
        testSsnShort.checkSsnLengthOk()
    assert str(exeptionMessage.value) == 'Henkilötunnuksesta puuttuu merkkejä'
 
# Testitapaus 8: liian pitkän HeTu:n virheilmoitus
def test_tooLongError():
    with pytest.raises(ValueError) as exeptionMessage:
        testSsnLong.checkSsnLengthOk()
    assert str(exeptionMessage.value) == 'Henkilötunnuksessa ylimääräisiä merkkejä'

# Testitapaus 9: Väärän vuosisatamerkin virheilmoitus, muutoin oikea HeTu
def test_wrongCenturySymbolError():
    with pytest.raises(ValueError) as exeptionMessage:
        testSsnWrongCenturySymbol.getDateOfBirth()
    assert str(exeptionMessage.value) == 'Vuosisatamerkki virheellinen'
