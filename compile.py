# Compile all the data into one text file.

import os

in_dir = 'data'
out_file = 'all_lyrics.txt'

os.chdir(in_dir)

# Get all directories in the data directory.
dirs = [d for d in os.listdir('.') if os.path.isdir(d)]
print('albums:')
print(dirs)

# Get all file names in the data directory.
files = []
for dir in dirs:
    _files = os.listdir(dir)
    files += map(lambda x: os.path.join(dir, x), _files)

out_text = ''
for file in files:
    # Read the file.
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    # Add the file name to the text.
    [album, song] = file.split('\\')
    song = song.replace('.txt', '')
    out_text += 'Album: ' + album + '\n'
    out_text += 'Song: ' + song + '\n'
    out_text += text

with open(out_file, 'w', encoding='utf-8') as f:
    f.write(out_text)