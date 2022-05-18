a = 123.6
b = -14
c = ['23', True]
d = ['abcdefg', 1]
s = 'ABCDEFG'
lista = ["qwe", False, 234.0, 'GHJK', float('-inf'), -1]

# 1
print(b >= a and d < c)  # b >= a este False, d < c nu mai ajunge sa se evalueze
print(b != a or 'abc' > s and len(s) == 4)  # True or False este True

# 2
print(not (b >= a and d < c))  # False and False este False, negat este True
print(not b >= a and d < c)  # True and False este False

# 3
# 8 / 2 * 'abc' -> 8/2 este float si nu se poate inmulti cu str
# 8 // 3 * [3, 'def'] -> ok
# d >= s -> operatorul nu e suportat intre list si str
# [s] <= c -> ['ABCDEFG'] <= ['abcdefg', 1'] este False
# s <= c -> operatorul nu e suportat intre list si str
# s <= c[0] -> 'ABCDEFG' <= '23' False
# s <= c[2/2] -> index este float, trebuie int
# s <= c[6] -> index out of range

# 4
# "GHJK" not in lista -> False (este in lista)
# 234 in lista -> False
# (a < b) in lista -> True (False este in lista)
# lista[len(lista) - 1] * lista[2] > 0 -> 1170.0 > 0 este True

# 5
n = int(input("nr:"))
print('result: ', n ** 2)
