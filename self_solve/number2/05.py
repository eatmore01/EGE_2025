print("x y z w F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = int((((x <= y) or (y == w)) and ((x or z) == w)))
                if F == 1:
                    print(x, y, z, w, F)

# ((x → y) ∨ (y ≡ w)) ∧ ((x ∨ z) ≡ w)

# https://inf-ege.sdamgia.ru/problem?id=28677 - неверно