# Re-Requesting a Vanity Plate
## Questions
1. Vanity plate should be in upper case?
2. Ask or not tu user fix punctuation issues
3. what is the format of the plate
4. Do we have limitation in plate string length

## Task
Implement a program that prompts the user for a vanity plate and then output Valid if meets
all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase.
Also, ask to user fix punctuation issues like AAA-222
Requarements:
    “All vanity plates must start with at least two letters.”
    “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable …
    vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    “No periods, spaces, or punctuation marks are allowed.”

## Pseudocode
Initialise user prompt
function checkPunctuation:
    Check if prompt contains any punctuation errorrs. Unaccaptable if prompt contains any punctiation symbols like . " ' , / @ other
    if yes reurn False
    else return True
function fixPunctuationError:
    remove from prompt punctuation symbols and return fixed string
function checkFirstTwoSymbols:
    run for loop only twice and check if first two symbols isAlpha.
        if yes return True
        else: False
function checkPromptLength:
    count symbols in prompt and return True if length is equal ro grater then 2 and euqal or less 6
function checkNumsInString:
    check if numbers starts with 0, if yes return false
    create variable as False like switch
    Run for loops where use switch and retur switch value True or False
    alse create variable as counter
    if counter is 0 means string does not contains numbers and return True
function MAIN:
    get prompt
    run prompt in checkPunctuation if result is True start while loop where we need to ask user fix or not
    if no eqplain that this is unnacaptable and ask again
    if yes run this prompt is fixing function and get result
    final result check in functions, if all returns True
        Display Valid
    in other case
        Display Invalid

## Tests
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

