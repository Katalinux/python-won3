import os

files = 0
path = '../'

for x in os.walk(path):
    for file in x[2]:
        if '.py' in file[-3:].lower():
            print(file)
            files += 1

print(f'Nr. Python Files: {files}')
