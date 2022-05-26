import os

size = 0
path = '../'

for x in os.walk(path):
    for file in x[2]:
        if '.py' in file[-3:].lower():
            size += os.path.getsize(os.path.join(x[0], file))

print(f'\nStart dir: {os.path.abspath(path)}\nTotal file size: {size}')

