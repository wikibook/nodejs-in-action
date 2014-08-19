# A really simple number-guessing game
while True:
    input = raw_input('Enter a number: ')
    try:
        val = int(input)
    except ValueError:
        print 'I said, a *number*...'
    if val == 7:
        print 'You guessed it!'
        break
    else:
        print 'Try again'
