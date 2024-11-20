import barcode

Character = "H"
testStringI = '131298-2137'

def test_barcodeValue():
    assert barcode.barCodeValue(Character) == 40

def test_calculateCode128BCheksum(): 
    assert barcode.calculateCode128BCheksum(testStringI) == 43

def test_createCode128B():
    assert barcode.createCode128B(testStringI) == 'Ì131298-2137KÎ'

# Luokan Code 128B testit

text1 = '128B'
barcode1 = barcode.Code128B(text1, 'Common')

def test_common128B():
    assert barcode1.code == '128B'
    assert barcode1.variant == 'Common'

def test_common128B_valid():
    assert barcode1.checkValidity() == True