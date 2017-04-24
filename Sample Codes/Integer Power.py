x = float(raw_input('Enter a number: '))
p = int(raw_input('Enter Integer Power'))
result = 1
for turn in range(p):
    print('iteration: ' + str(turn) + \
    'current result ' + str(result))
    result = result * x
def iP(x,p):
    result = 1
    for turn in range(p):
            print('iteration: ' + str(turn) + \
    'current result ' + str(result))
    result = result * x
    return result
        