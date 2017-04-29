from ps4a import *
import time


def isValidWordInHand(word, hand):
    """
    Returns True if word is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    
    """
    flag = True
    
    handCopy = hand.copy()

    for letter in word:
        if letter in handCopy:
            handCopy[letter] -= 1
        else:
            return False
                
    for i in handCopy.values():
        if i < 0:
            flag = False
    return flag

def compChooseWord(hand, wordList, n):
    
    maxScore = 0
    score = 0
    bestWord = None
    for word in wordList:   
        if isValidWordInHand(word, hand) == True:
            score = getWordScore(word, n)
            if score > maxScore:
                maxScore = score
                bestWord = word

    return bestWord


def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.
    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    
    total = 0
    handCopy = hand.copy()
    bestWord = compChooseWord(handCopy, wordList, n)
    
    while bestWord != None:    
    # As long as there are still choice for computer:

        # Display the hand
        print 'Current Hand: ',
        displayHand(handCopy)

        # let computer to choose the best word        
        total += getWordScore(bestWord, n)
        print '\"', bestWord, '\"', 'earned', getWordScore(bestWord, n), 'points. Total: ',total, 'points'
        print 
        handCopy = updateHand(handCopy, bestWord)
        bestWord = compChooseWord(handCopy, wordList, n)

    if bestWord == None:
        if sum(handCopy.values()) != 0:
            print 'Current Hand: ',
            displayHand(handCopy)
            print 'Total score: ',total,' points.'
            print

        else:
            print 'Total score: ',total,' points.'
            print        
        
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.
    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.
    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.
    4) After the computer or user has played the hand, repeat from step 1
    wordList: list (string)
    """


    hand = {}
    
    while True:
      getInput = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
      print
      if getInput == 'e':
          return None
        
      elif getInput not in ('n','r'):
          print 'Invalid command.'
          
      elif hand == {} and getInput == 'r':
          print 'You have not played a hand yet. Please play a new hand first!'
          
      elif getInput == 'n' or getInput == 'r':    
        if (getInput == 'n'):
            hand = dealHand(HAND_SIZE)        
            handCopy = hand.copy()
        else:
            hand = handCopy.copy()
        
        while True:          
          getInputCom = raw_input('Enter u to have yourself play, c to have the computer play: ')
          print

          if getInputCom == 'u':
            playHand(hand, wordList, HAND_SIZE)
            print
            break

          elif getInputCom == 'c':
            compPlayHand(hand, wordList, HAND_SIZE)
            print
            break
        
          else:
              print 'Invalid command.'
              print              


    hand = {}
    
    while True:
      getInput = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
      print
      if getInput == 'e':
          return None
          
      elif hand == {} and getInput == 'r':
          print 'You have not played a hand yet. Please play a new hand first!'
       
      elif getInput == 'n' or getInput == 'r':        
      
        while True:          
          getInputCom = raw_input('Enter u to have yourself play, c to have the computer play: ')
          print

          if getInputCom == 'u':                            
              if getInput == 'n':
                  hand = dealHand(HAND_SIZE)
              playHand(hand, wordList, HAND_SIZE)
              print
              break

          elif getInputCom == 'c':
              if getInput == 'n':
                  hand = dealHand(HAND_SIZE)              
              compPlayHand(hand, wordList, HAND_SIZE)
              print
              break
        
          else:
              print 'Invalid command.'
              print
      else:
          print 'Invalid command.'


    isFirst = True
    n = HAND_SIZE
    while 1:
        choice = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if (choice == 'e'):
            break       
        elif (choice != 'r' and choice != 'n'):
            print "Invalid command.\n"            
        elif (isFirst and choice is 'r'):                    
            print "You have not played a hand yet. Please play a new hand first!\n"
        else:
            isFirst = False
            while 1:
                choice2 = raw_input("Enter u to have yourself play, c to have the computer play: ")
                if (choice2 == 'c'):
                    if (choice == 'n'):
                        hand = dealHand(n)
                    compPlayHand(hand, wordList, n)
                    break
                elif (choice2 == 'u'):
                    if (choice == 'n'):
                        hand = dealHand(n)
                    playHand(hand, wordList, n)
                    break
                else:
                    print "Invalid command.\n"          
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
