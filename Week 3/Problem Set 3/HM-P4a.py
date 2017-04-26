def getGuessedWord(secretWord, lettersGuessed):   
    newList = []   
    for word in secretWord:
        flag = False # refresh every time when finish inner loop
                     # use flag to control when to output '_'
        for letter in lettersGuessed:
            if word == letter:
                flag = True
                newList.append(word)
                break # finish this inner loop
                      # avoid to compare the rest letters
        if(flag == False):
            newList.append('_')   
    return newList
    
    

def getAvailableLetters(lettersGuessed):
    import string
    letterList = list(string.ascii_lowercase)
    outString = ''
    for letter in lettersGuessed:
        letterList.remove(letter)
    for char in letterList:
        outString += char
    return outString


def isWordGuessed(secretWord, lettersGuessed):
    if lettersGuessed == []:
        return False
    for word in secretWord:
        resultLetterList = []
        for letter in lettersGuessed:
            result = word ==letter 
            resultLetterList.append(result)
        if True in resultLetterList:
            continue
        else:
            return False
    return True



def hangman(secretWord):
   
    import string
    initialString = string.ascii_lowercase
    print 'Bruh Hangman.'
    print 'The word length is:' + str(len(secretWord))
    print ''
    getLetter = ''
    num = 8
    print 'You have 8 guesses left.'
    print 'Available letters: ' + str(initialString)
    getLetterList = ''
    while num <= 8 and num >= 0:
        outString = getGuessedWord(secretWord, getLetter)
        print 'number left :' + str(num) 
        if num == 8:
            print 'Available letters: ' + str(initialString)
        else:
            print 'Available letters: ' + getAvailableLetters(outString)
        

        char = raw_input('Guess the lettr: ')
        loChar = char.lower()
        getLetter += loChar

        print 'getLetter is ' + getLetter
        print 'getLetterList is ' + getLetterList


        outString = getGuessedWord(secretWord, getLetter)

        leftLetters = getAvailableLetters(getLetter)
        
        result = isWordGuessed(char, secretWord)

        if result == True:
            if char in getLetterList:
                print 'already guessed: ' + outString
            
            else:
                print 'NiCE ' + outString
                getLetterList += getLetter
                
            print '-------------'
            if outString == secretWord:
                print 'woa!'
                break
                
            print 'number of guesses left :' + str(num) 
            print 'Available letters: ' + getAvailableLetters(outString)
            
            
        else:
            if char in getLetterList:
                print 'already guessed ' + outString
                print '-------------'
                print 'number of guesses left' + str(num)
                print 'Available letters: ' + leftLetters
            else:
                print 'does not t exist' + outString
                getLetterList += getLetter
                print '-------------'
            
                if num != 1:
                    num -= 1
                    print 'guesses left :' + str(num) 
                    print 'Available letters: ' + leftLetters
                else:
                    print 'word was ' + secretWord + '.'
                    break