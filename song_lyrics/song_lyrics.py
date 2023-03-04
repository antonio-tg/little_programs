# We ask a user to choose a song from a list of 10 songs. When the user does so, it prints the lyrics of the song they selected.

import json

with open('songs.json', 'r') as f:
    lyrics = json.load(f)

print('Select one of the following songs: ')
for key in lyrics.keys():
    print(key)
song = input(f'Enter your choice: ')
if song in lyrics.keys():
    print(f'You have selected the song "{song}", then we show you the lyrics below:\n')
    print(f'{"-"*10}{song}{"-"*10}\n')
    print(lyrics[song])
else:
    print('That song is not on the list')
