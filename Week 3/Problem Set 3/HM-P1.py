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
    
    
 