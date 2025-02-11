print("a b c d")
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                F = int(((not a) and ( not b )) or ( b == c ) or d)
                if  F == 0:
                    print(a, b, c, d)



# https://inf-ege.sdamgia.ru/problem?id=37137

# c d b a