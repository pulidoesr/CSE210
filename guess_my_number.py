# Developer : Team 10
# Program   : guess_my_number
# Purpose   : Understanding Loops
import random

magic_number = 0
guess_number = 0
guess_count = 0
answer = 'y'
magic_number = int(input('What is the magic number? '))
guess_number = int(input('What is your guess number? '))
while guess_number != magic_number:
    if guess_number < magic_number:
        print('Higer')
    elif guess_number > magic_number:
        print('Lower')
    guess_number = int(input('What is your guess number? '))
print('You guessed it!')

while answer.lower() == 'y':
    number_range = int(input('Input the number range '))
    magic_number = random.randint(1, number_range)
    guess_number = int(input('What is your guess number? '))
    while guess_number != magic_number:
        guess_count = guess_count + 1
        if guess_number < magic_number:
            print('Higer')
        elif guess_number > magic_number:
            print('Lower')
        guess_number = int(input('What is your guess number? '))
    print(f'You tried {guess_count} times')
    print('You guessed it!')
    answer = input('Would you like to continue playing (Y/N)? ')