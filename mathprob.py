import random

def mathProb():
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    print('What is ' + str(number1) + ' + ' + str(number2) + '?')
    answer = input()
    if int(answer) == number1 + number2:
        print('Correct!')
    else:
        print('Nope! The answer is ' + str(number1 + number2) + ", dumbass!")

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    mathProb()

    print('Do you want to solve another?')
    playAgain = input()
