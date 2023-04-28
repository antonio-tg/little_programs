# In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superseded by voice and digital data communication channels, it still has its use in some applications around the world.
import re

d1 = { 'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-','L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-','R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.','0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-',' ':'¬','$':'...-..-','&':'.-...',':':'---...','SOS':'...---...','!':'-.-.--'}

d2 = dict((v,k) for k,v in d1.items())

def decode_morse(morse_code):
    word = ''
    morse_code = morse_code.strip()
    morse_code = re.sub('   ',' ¬ ',morse_code)
    for letter in morse_code.split(' '):
        word += d2[letter]
    return word
   
word1 = decode_morse('   .... . -.--   .--- ..- -.. .    ')
print(word1)
