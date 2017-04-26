def getGuessedWord(secretWord, lettersGuessed):
    ans = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            ans += letter
        else:
            ans += '_'
    return ans   
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
    
secretWord = 'woah' 
lettersGuessed = ['c','o','o','l','w','h','i','t','e']
print getGuessedWord('woah', ['w', 'i', 'h', 'z', 'h', 'o','a'])
print getGuessedWord('app', [])