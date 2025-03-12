from itertools import product

count = 0

for s in product ('ABCX', repeat = 5 ):
    if s.count('X') == 1 and (s[0] == 'X' or s[-1] == 'X'):
        count += 1

print(count)


# https://inf-ege.sdamgia.ru/problem?id=13486
