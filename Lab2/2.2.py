a = float(input('Latura 1: '))
b = float(input('Latura 2: '))
c = float(input('Latura 3: '))

if a == b == c:
    print('Echilateral.')

elif round(a ** 2) == round(b ** 2) + round(c ** 2) or round(b ** 2 == round(c ** 2) + round(a ** 2) or
                                                             round(c ** 2) == round(b ** 2) + round(a ** 2)):
    if a == b or b == c or a == c:
        print('Dreptunghic isoscel')
    else:
        print('Dreptunghic.')

elif a == b != c or b == c != a or a == c != b:
    print('Isoscel.')
