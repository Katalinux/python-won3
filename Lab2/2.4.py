a = list(input('Sequence: ').lower())
b = []

for x in range(-1, -len(a) - 1, -1):
    b.append(a[x])

print('Palindrome' if a == b else 'Not a Palindrome')
