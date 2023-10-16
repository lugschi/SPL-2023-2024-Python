import random


result = 0
result2 = 0

for i in range(6):

    randomNumber = random.randint(0, 7)
    randomNumber2 = random.randint(0, 7)
    result += randomNumber
    result2 += randomNumber2

if result < result2:
    print('Computer Wins!')
elif result == result2:
    print('Its a draw!')
else:
    print('Player1 Wins')
print(result)
print(result2)