# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

# Please note that using encode is considered cheating.
import string

all_letters = string.ascii_lowercase
def index(n):
    if n > 25:
        n -= 26
    return(n)

def rot13(word1):
    word2 = ''
    for letter in word1:
        if letter in all_letters:
            letter = all_letters[index(all_letters.index(letter) + 13)]
        elif letter.lower() in all_letters:
            letter = all_letters[index(all_letters.index(letter.lower()) + 13)].upper()
        word2 += letter
    return word2

word1 = input('Ingress a wort to shifted it: ')
word2 = rot13(word1)
print(f'The original word is {word1} and become to {word2}')
