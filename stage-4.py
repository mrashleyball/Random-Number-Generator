# Random Number Generator 4/4

# 0 Import module
# 1 User selects start and end numbers
# 2 Validate user input
# 3 Handle error messages i.e user inputs strings
# 4 Create random number
# 5 Display random number

import random

while True:
    try:
        startNumber = int(input('Select your starting number: '))
    except ValueError or NameError:
        print('Error! Numbers only.')
    try:
        endNumber = int(input('Select your end number: '))
    except ValueError or NameError:
        print('Error! Numbers only.')
    
    try:
        if startNumber < 0:
            print('Start Number cannot be less than zero. Try again.')
        elif startNumber == endNumber:
            print('Start and End numbers cannot be the same. Try again.')
        elif startNumber >= endNumber:
            print('Start Number cannot be higher than End Number. Try again.')
        elif startNumber <= endNumber:
            break
    except NameError:
        print('Error, try again.')

number = random.randrange(startNumber,endNumber)
print('Your random number between ' + str(startNumber) + ' and ' + str(endNumber) + ' is: ' + str(number))