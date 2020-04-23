import random
import string


dif = input('difficulty level: easy, mid, hard; ')
x = 'easy'
y = 'mid'
z = 'hard'

if dif == 'easy':
    x = 'easy'
x = int(input('guess a number from 1 to 10'))
answer = random.randint(1,10)
numTries = 5
while (x != answer):
    print('you got it wrong')
    print('number of tries left is:' + str(numTries))
    x = int(input('guess a number from 1-10: '))
    numTries -= 1

    if numTries == 0:
        print('Game Over')
        break

   
    elif x == answer:
        print('You got it right')
        break


if dif == 'mid':
    y = 'mid'


y = int(input('guess a number from 1-20:'))
answery = random.randint(1,20)
numTries = 3

while (y != answery):
    print('you got it wrong')
    print('number of tries left is:' + str(numTries))
    y = int(input('guess a number from 1-20:'))
    numTries -= 1

    if numTries == 0:
        print('Game Over')
        break

   
    elif y == answery:
        print('You got it right')
        break
if dif == 'hard':
    z = 'hard'

z = int(input('guess a number from 1-50:'))
answerz = random.randint(1,50)
numTries = 2
        
while (z != answerz):
    print('you got it wrong')
    print('number of tries left is:' + str(numTries))
    z = int(input('guess a number from 1-50:'))
    numTries -= 1

    if numTries == 0:
        print('Game Over')
        break

   
    elif z == answerz:
        print('You got it right')
        break

