print 'Please think of a number between 0 and 100!'

high = 100
low = 0
a = False

while a == False:
    middle = (high + low) / 2
    print('Is your secret number ' + str(middle)+ '?')
    x = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if x == 'l':
        high = middle
    elif x == 'h':
        low = middle
    elif x == 'c':
        a = True
    else:
        print 'Sorry, I did not understand your input.'

print('Game over. Your secret number was: ' + str(middle))