from itertools import product

count = 0

for s in product ('0123456789abcde', repeat = 8 ):
    if s[0] != '0' and s.count('0') == 2:
        if s.count('a') + s.count('b') + s.count('c') + s.count('d') + s.count('e') < 5:
            count += 1

print(count)

# https://inf-ege.sdamgia.ru/problem?id=72566