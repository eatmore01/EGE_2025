print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2): 
                F = (((w <= y) <= x) or not z)
                if F == 0:
                    print(x, y, z, w)


# zywx # какой то варинат пробника 2024-2025


