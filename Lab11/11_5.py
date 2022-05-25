import os


def walk(root):
    global size
    temp = os.listdir(root)
    for item in temp:
        if os.path.isfile(os.path.join(root, item)):
            if '.py' in item[-3:].lower():
                print(item)
                size += os.path.getsize(os.path.join(root, item))
        else:
            walk(os.path.join(root, item))


size = 0
walk('../')
print(f'\nTotal file size: {size}')
