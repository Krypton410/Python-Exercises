animals = {'a': [5, 6, 10, 4, 7, 2], \
'c': [18], 'b': [10, 20, 30, 2, 121, 44, 84, 33, 2, 7],\
'd': [43, 145, 8]}
def biggest(aDict):
    biggestNum = 0
    result = None
    for key in aDict.keys():
        if len(aDict[key]) >= biggestNum:
            result = key
    biggestNum = len(aDict[key])
    return result
print biggest(animals)