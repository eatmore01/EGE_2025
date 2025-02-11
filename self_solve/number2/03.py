print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = int(((not x or z) == (y and not w)) <= (z and y))
                if F == 0:
                    print(x, y, z, w)


# https://inf-ege.sdamgia.ru/problem?id=36857 - zyxw