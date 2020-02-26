# ESTE É UM JOGO DE ADIVINHAR O NÚMERO

import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# PEÇA AO JOGADOR ADVINHAR 6 VEZES.
for guessTaken in range (1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Youe guess is too high.')
    else:
        break #ESSA CONDIÇÃO CORRESPONDE AO PALPITE CORRETO!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was' + str(secretNumber))