# Random Number Generator 2/4

# 0 Import module
# 1 User selects start and end numbers
# 2 Create random number
# 3 Display random number

import random

startNumber = int(input('Select your starting number: '))
endNumber = int(input('Select your end number: '))

number = random.randrange(startNumber,endNumber)

print('Your random number is: ' + str(number))