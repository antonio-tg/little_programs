# The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

#Examples
#"the-stealth-warrior" gets converted to "theStealthWarrior"
#"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
#"The_Stealth-Warrior" gets converted to "TheStealthWarrior"

import re
def to_camel_case(text):
    text = re.split('[-_]',text)
    for i in range(1,len(text)):
        text[i] = text[i].capitalize()
    text = ''.join(text)
    return text

sentence = input('Ingress a sentence to convert a camelCase: ')
camel = to_camel_case(sentence)
print(f'The sentence {sentence} is {camel} in camelCase')
