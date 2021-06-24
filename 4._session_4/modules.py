# OS module allows us to run OS commands from code
import os

os_command = input('Name of new file: ')
os.mkdir(os_command)
os.chdir(os_command)

with open('A_new_file.py', 'w') as f:
    f.write('Some text')


#Sys module allows us to make arguements and retrieve these in the terminal
import sys

if len(sys.argv) > 1:
    print(f'Your flags: {sys.argv[1:]}')


#Subprocess module allows for a sort of multi-threading, but I dont know how it really works

#Zipfile module allows for the usage of .zip files
from zipfile import ZipFile

os.chdir('..')

files = os.listdir('.')

with ZipFile('project_zipped.zip', 'w') as zf:
    for file in files:
        zf.write(file)

#How to use your own custom module
import mymodule

print(mymodule.greeting('Andreas'))