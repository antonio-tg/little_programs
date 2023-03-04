# This program is about the user guessing a number between 1 and 50
from random import randint

hidden_number = randint(1,50)
print("Let's play to guess the hidden number, the range is [1,50]")
n = 0
number_user = ''
while hidden_number != number_user:
    n += 1
    try:
        number_user = int(input('Enter your forecast: '))
    except:
        print('Your choice is not valid, try again')
    if number_user not in range(1,51):
        print('The entered number does not belong to the range [1,50]')
print(f'You have guessed the number in {n} tries')
