print("x y z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            F = int((x == y) or ((y or z) <= x))
            if F == 0:
                print(x, y, z)

# (x ≡ y ) ∨ ((y ∨ z) → x)

# https://inf-ege.sdamgia.ru/problem?id=15124 - xzy
