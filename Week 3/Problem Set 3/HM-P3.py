def getAvailableLetters(lettersGuessed):

    import string
    letterList = list(string.ascii_lowercase)
    outString = ''
    for letter in lettersGuessed:
        letterList.remove(letter)
    for char in letterList:
        outString += char
    return outString


print getAvailableLetters(['a', 'b', 'c', 'd', 'e', 'f']) 