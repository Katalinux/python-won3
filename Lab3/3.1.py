num = int(input('Introdu un numar natural pozitiv: '))

if num < 0:
    print('Numarul trebuie sa fie mai mare ca 0')
else:
    factorial = 1
    for n in range(2, num + 1):
        factorial *= n

    print(str(num) + '! =', factorial)
