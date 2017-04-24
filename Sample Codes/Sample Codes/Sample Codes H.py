x = int(raw_input('1 : '))
p = int(raw_input('2 : '))
result = 1
for turn in range(p):
    print('iteration '+ str(turn) + 'current result ' + str(result))
    result = result * x
def max(x, y):
    if x > y:
        return x
    else:
        return y