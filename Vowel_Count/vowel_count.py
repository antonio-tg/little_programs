# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    i = 0
    for letter in sentence:
        if letter in ['a','e','i','o','u']:
            i +=1
    return i

sentence = input('Ingres a sentence to count his vowels: ')
n = get_count(sentence)
print(f'The sentence {sentence} has {n} vowels')
