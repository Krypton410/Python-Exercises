epsilon = 0.01
y = int(raw_input('Enter Number'))
guess = y/2.0
while abs(guess*guess - y) >= epsilon:
    guess = guess - (((guess**2) - y)/(2*guess))
    print(guess)
print('Square root of' + str(y) + ' is about ' + str(guess))