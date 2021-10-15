# Random Number Generator 3/4

# 0 Import module
# 1 User selects start and end numbers
# 2 Validate user input
# 3 Create random number
# 4 Display random number

import random

while True:
    startNumber = int(input('Select your starting number: '))
    endNumber = int(input('Select your end number: '))
    if startNumber < 0:
        print('Start Number cannot be less than zero. Try again.')
    elif startNumber == endNumber:
        print('Start and End numbers cannot be the same. Try again.')
    elif startNumber >= endNumber:
        print('Start Number cannot be higher than End Number. Try again.')
    elif startNumber <= endNumber:
        break

number = random.randrange(startNumber,endNumber)
print('Your random number is: ' + str(number))