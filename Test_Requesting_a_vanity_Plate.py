from Requesting_a_Vanity_Plate import fixPunctuation, plateLength, checkNumInString, checkFirstTwoLetters, checkPunctuation

def main():
    test_fixPunctuation()
    test_checkPunctuation()
    test_plateLength()
    test_checkFirstTwoLetters()
    test_checkNumInString()

def test_fixPunctuation():
    assert fixPunctuation("AAA-222") == "AAA222"
    assert fixPunctuation("A@AA-222") == "AAA222"
    assert fixPunctuation("  A@AA-22  2 ") == "AAA222"

def test_checkPunctuation():
    assert checkPunctuation("AAA-222") == True
    assert checkPunctuation("A@AA-222") == True
    assert checkPunctuation("  A@AA-22  2 ") == True

def test_plateLength():
    assert plateLength("A") == False
    assert plateLength("AA") == True
    assert plateLength("AAA") == True
    assert plateLength("AAAA") == True
    assert plateLength("AAAAA") == True
    assert plateLength("AAAAAA") == True
    assert plateLength("AAAAAAA") == False

def test_checkFirstTwoLetters():
    assert checkFirstTwoLetters("AA123") == True
    assert checkFirstTwoLetters("AA") == True
    assert checkFirstTwoLetters("AAA") == True
    assert checkFirstTwoLetters("A1") == False
    assert checkFirstTwoLetters("1ABC") == False

def test_checkNumInString():
    assert checkNumInString("AAA222") == True
    assert checkNumInString("AA22A") == False
    assert checkNumInString("AA032") == False

if __name__ == "__main__":
    main()
