import random

list = ['rock', 'paper', 'scissors']
class rps():
    user_choice = ''
    my_choice = '' 

    def my_choiceachine(self):
        self.my_choice = random.choice(list)
        return self.my_choice

    def game(self):
        if self.user_choice == self.my_choice:
            return "We draw, let's play again"
        else:
            if self.user_choice == 'rock':
                if self.my_choice == 'paper':
                    return 'You lose'
                else:
                    return 'You win'
            if self.user_choice == 'paper':
                if self.my_choice == 'rock':
                    return 'You win'
                else:
                    return 'You lose'
            if self.user_choice == 'scissors':
                if self.my_choice == 'papel':
                    return 'You win'
                else:
                    return 'You lose'

result = "We draw, let's play again"
print("Let's play rock paper scissors")
while result == "We draw, let's play again":
    rps_game = rps()
    rps_game.user_choice = input('Enter your choice: ').lower()
    while rps_game.user_choice not in list:
        rps_game.user_choice = input('This is not a valid choice, please type one of the following options: rock, paper, scissors: ').lower()
    my_choice = rps_game.my_choiceachine()
    print(f'I choose {my_choice}')
    result = rps_game.game()
    print(result)
