import random


result = 0;
randomNumber = 0;

while randomNumber != 15 and randomNumber != 25:
    randomNumber = random.randint(10, 30);
    print(randomNumber)
    result += randomNumber;
print('Total', result)