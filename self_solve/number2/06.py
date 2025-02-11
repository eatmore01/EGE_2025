print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = int((y <= z) and not ((y or w) <= (z and x))) 
                if F == 1: # 0/1
                    print(x, y, z, w)

# (y → z) ∧ ¬((y ∨ w) → (z ∧ x))

# https://inf-ege.sdamgia.ru/problem?id=35891 - неверно