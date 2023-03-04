# This program asks the user for a number and tells him if it is even or odd and if he wants to enter another number

class even_odd():
    # attributes
    number=None
    # methods
    def isnum(self):
        while self.number.isdigit() == False:
            self.number = input('That is not a number, try again please: ')

    def even_or_odd(self):
        if float(self.number)//2 == float(self.number)/2:
            print("It's an even number!")
        else:
            print("It's an odd number!")

final = 'yes'
while final == 'yes':
    num = even_odd()
    num.number = input('\nEnter a number: ')
    num.isnum()
    num.even_or_odd()
    f = ''
    while f not in {'yes','no'}:
        f = input('If you want to enter another number type "yes", otherwise type "no": ').lower()
    final = f
