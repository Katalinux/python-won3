import os

files, dirs = 0, 0
path = '../'

for x in os.walk(path):
    dirs += len(x[1])
    files += len(x[2])

os.chdir(path)
print(f'Path: {os.getcwd()}\nNr. Folders: {dirs}\nNr. Files: {files}')
