open('lyrics.txt', 'w')

songs = open('songs.docx', 'w')

songs.write('Something 1 \nSomething more \nAnd yet another thing')
songs.close()

f_read = open('songs.docx', 'r')
f_readline = open('songs.docx', 'r')
f_readlines = open('songs.docx', 'r')

print(f'Read: {f_read.read()} \n')
print(f'Readline: {f_readline.readline()} \n')
print(f'Readlines: {f_readlines.readlines()}')