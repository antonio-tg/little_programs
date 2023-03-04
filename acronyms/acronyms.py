import re
text = input('Enter the name of the organization for which you want to obtain the acronym: ')
acro = ''
for word in text.split(' '):
    if not re.search('[a-z]', word[0]):
        acro += word[0]
print(f'The acronym of the organization "{text}" is: {acro}')
