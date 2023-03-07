import random

list = ['rock', 'paper', 'scissors']
user_choice = input("Let's play rock paper scissors, enter your choice: ").lower()
my_choice= ''
while user_choice != my_choice:
    while user_choice not in list:
        user_choice = input('This is not a valid choice, please type one of the following options: rock, paper, scissors: ')

    print(f'You chose {user_choice}')
    my_choice = random.choice(list)
    print(f'I choose {my_choice}')
    if user_choice == my_choice:
        print("We draw, let's play again")
        user_choice = input("Let's play rock paper scissors, enter your choice: ")
    else:
        if user_choice == 'rock':
            if my_choice == 'paper':
                print('You lose')
            else:
                print('You win')
        if user_choice == 'paper':
            if my_choice == 'rock':
                print('You win')
            else:
                print('You win')
        if user_choice == 'scissors':
            if my_choice == 'paper':
                print('You win')
            else:
                print('You lose')
        break
