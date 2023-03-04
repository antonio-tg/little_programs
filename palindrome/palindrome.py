# This program asks the user for a word and tells if it is a palindrome.
from colors import colors

words = input('Write five words separated by a comma: ').replace(' ','').split(',')
while len(words) != 5:
    words = input('The wordlist does not have the requested length, please try again: ').replace(' ','').split(',')
for word in words:
    p1 = word.lower()
    p2 = p1[::-1]
    if p1 == p2:
        print(f'The word {colors.bold(colors.green(word))} is a palindrome')
    else:
        print(f'The word {colors.bold(colors.red(word))} is not a palindrome')
