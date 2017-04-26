animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dingo')
animals['d'].append('dog')
def howManyValue(aDict):
    result = 0
    for value in aDict.values():
        result += len(value)

    return result
print howManyValue(animals)
def howManyKey(aDict):
    result = 0
    for key in aDict:
        result += len(aDict[key])
    return result
    
print howManyKey(animals)