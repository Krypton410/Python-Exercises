
import random
import string

WORDLIST_FILENAME = "C:\Users\Maxwell\Desktop\Python Exercises\Week 3\Problem Set 3\words.txt"

def loadWords():
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    for word in secretWord:
        if word not in lettersGuessed:
            return False
    return True
    
print isWordGuessed('durian', ['h', 'a', 'c', 'd',\
                              'i', 'm', 'n', 'r', 't', 'u'])
def getGuessedWord(secretWord, lettersGuessed):
    ans = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            ans += letter
        else:
            ans += '_ '
    return ans
print getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's','a'])
'app_ e'

def getAvailableLetters(lettersGuessed):

    import string
    letterList = list(string.ascii_lowercase)
    outString = ''
    for letter in lettersGuessed:
        if letter in letterList:            
            letterList.remove(letter)
    for char in letterList:
        outString += char
    return outString    
print getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])

def hangman(secretWord):

    import string
    initialString = string.ascii_lowercase
    print 'Hangman'
    print 'Word is ' + str(len(secretWord)) + ' letters long.'
    getLetter = ''
    num = 8
    guessedLetters = ''

    while num > 0:
        print '-----------'
        if isWordGuessed(secretWord, getLetter):
            print 'word guessed'
            break
        print 'guesses left :' + str(num)
        print 'Available letters: ' + getAvailableLetters(getLetter)

        char = raw_input('Pick a letter: ')
        loChar = char.lower()
        getLetter += loChar
        outString = getGuessedWord(secretWord, getLetter)
        if loChar in secretWord:
            if loChar in guessedLetters:
                print 'letter already guessed ' + outString           
            else:
                print 'Cool : ' + outString   
        else:
            if loChar in guessedLetters:
                print 'letter already guessed: ' + outString
            else:
                print 'Letter : ' + outString
                num -= 1
              
        guessedLetters += loChar
    if num == 0:
        print '-----------'
        print 'out of guesses.  ' + secretWord + '.'

secretWord = chooseWord(wordlist).lower()
hangman(secretWord) 