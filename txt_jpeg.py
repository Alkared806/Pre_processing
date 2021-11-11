from sys import argv
import os

script_path = os.getcwd()
files_path, file_name = argv[1:] 
os.chdir(files_path)

file = open(script_path + '\ ' + file_name + ".txt", 'w')
for name in os.listdir('.'):
    if name.endswith('.jpg'):
        file.write(name + '\n')