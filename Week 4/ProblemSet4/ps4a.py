import random
import string
import sys

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "C:\Users\Maxwell\Desktop\Python Exercises\Week 4\ProblemSet4\words.txt"

def loadWords():
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList
wordList = loadWords()

def getFrequencyDict(sequence):


    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def getWordScore(word, n):

    sumLeSc = 0
    wordScore = 0
    for letter in word:
        if letter in SCRABBLE_LETTER_VALUES:
            sumLeSc += SCRABBLE_LETTER_VALUES[letter]

    wordScore = sumLeSc * len(word)
    if n!= len(word):
        return wordScore 

    else:
        return wordScore + 50

def displayHand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              
    print                               

def dealHand(n):

    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

def updateHand(hand, word):
    handCopy = hand.copy()
    for i in word:
        if i in handCopy:
            handCopy[i] -= 1
def isValidWord(word, hand, wordList):

    flag = True
    
    handCopy = hand.copy()
    if word in wordList:
        for letter in word:
            if letter in handCopy:
                handCopy[letter] -= 1
            else:
                return False
                
        for i in handCopy.values():
             if i < 0:
                flag = False
        return flag
    else:
        return False

def calculateHandlen(hand):
    handCopy = hand.copy()
    sumNum = 0
    for i in handCopy:
        sumNum += handCopy[i]
    return sumNum


def playHand(hand, wordList, n):
    total = 0
    handCopy = hand.copy()
    while sum(handCopy.values()) != 0:
        print 'Current Hand: ',displayHand(handCopy)
        userInput = raw_input('Enter word, or a "." to indicate that you are finished: ')
        if userInput == '.':
                break
        elif userInput != '.': 
            if isValidWord(userInput, handCopy, wordList) == False:
                print 'Invalid'
                print 
            else:
                total += getWordScore(userInput, n)
                print userInput , 'earned ', getWordScore(userInput, n), 'points. ', 'Total: ', total
                print
                handCopy = updateHand(handCopy, userInput)
                print 

    if userInput == '.' or sum(handCopy.values()) == 0:

        print 'Run out of letters. Total score: ', total,' points.'

def playGame(wordList):

    HAND_SIZE = 7
    n = HAND_SIZE

    flag = True
    handCopy = {}

    while flag:
        
        getInput = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        
        if getInput == 'n':
            hand = dealHand(n)
            playHand(hand, wordList, n)
            handCopy = hand.copy()
            print
            
        elif getInput == 'r':
            if handCopy == {}:
                print 'You have not played a hand yet. Please play a new hand first!'
                print
                
            else:
                playHand(handCopy, wordList, n)
                print

        elif getInput == 'e':
            return None

        else:
            print 'Invalid command.'
            print

if __name__ == '__main__':
    wordList = loadWords()
playGame(wordList)