def main():
    # ask user the plate number and modify the string
    plate = input("Plate: ").strip().upper()
    # get function values true or false
    checkpunct = checkPunctuation(plate)
    twoChar = checkFirstTwoLetters(plate)
    strLen = plateLength(plate)
    charsInsaid = checkNumInString(plate)

    if checkpunct == False and twoChar and strLen and charsInsaid:
        print("Valid")
    elif checkpunct:
        while True:
            ask = input("You have added extra punctuation marks, do you want ignor them? Y/N ").lower()
            if ask == "y":
                fixed = fixPunctuation(plate)
                break
            else:
                print("We can not allow punctuation marks in the plate")
        if checkFirstTwoLetters(fixed) and plateLength(fixed) and checkNumInString(fixed):
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")


# fix punctuation
def fixPunctuation(txt):
    txt = txt.translate({ord(i): None for i in '.,/-_!#@ -+=$"()\''})
    return txt


# No periods, spaces, or punctuation marks are allowed.
def checkPunctuation(txt):
    chars = '.,/-_!#@ -+=$"()\''
    for i in txt:
        if i in chars:
            return True
        else:
            continue
    return False


# “All vanity plates must start with at least two letters.”
def checkFirstTwoLetters(txt):
    # listOfText = list(txt)
    counter = 0
    for i in range(2):
        try:
            eval(txt[i] * 1)
        except NameError:
            counter += 1
        if counter >= 2:
            return True
    return False


# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def plateLength(txt):
    if len(txt) <= 6 and len(txt) >= 2:
        return True
    else:
        return False


# “Numbers cannot be used in the middle of a plate; they must come at the end. For example,
# AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
# The first number used cannot be a ‘0’.”
def checkNumInString(txt):
    check = False
    counter = 0
    for i in range(len(txt)):
        try:
            x = eval(txt[i] * 1)
            if x == 0 and txt[i - 1].isalpha():
                return False
        except:
            continue
    for i in range(len(txt)):
        if not txt[i].isalpha():
            check = True
            counter += 1
        else:
            check = False
    if counter == 0:
        return True
    else:
        return check

if __name__ == "__main__":
    main()
