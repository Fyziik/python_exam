# Creating a new file 
f = open('lyrics.txt', 'w') # 'w' = write mode
f.write('Welcome to the internet \nHave a look around')
f.close()

# Opening and Reading from a file
f_read = open('lyrics.txt', 'r') # 'r' = read mode
f_readline = open('lyrics.txt', 'r')
f_readlines = open('lyrics.txt', 'r')

# The reason I make 3 different variables, is because once you read through the lines, you have to reset the variable since you cant go "back"

# Prints the contents of the file as string
print(f'Read: {f_read.read()} \n')

# Prints a single line of the file, can be used in a loop
print(f'Readline: {f_readline.readline()} \n')

# Returns a list of the contents of the file, each new line is a new element in the array
print(f'Readlines: {f_readlines.readlines()} \n')