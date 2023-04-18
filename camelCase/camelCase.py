# The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

#Examples
#"the-stealth-warrior" gets converted to "theStealthWarrior"
#"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
#"The_Stealth-Warrior" gets converted to "TheStealthWarrior"

def to_camel_case(text):
    if '-' in text: text = text.split('-')
    if '_' in text: text = text.split('_')
    for i in range(1,len(text)):
        text[i] = text[i].capitalize()
    text = ''.join(text)
    print(text)
    return text

to_camel_case('the-stealth-warrior')
