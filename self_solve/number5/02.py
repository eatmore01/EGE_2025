# https://inf-ege.sdamgia.ru/problem?id=75242
def new_binary_number():
    for i in (2, 40):
        bin_n = bin(i)[2:]

        left = bin_n[1]
        new_bin = bin_n[:-1] + f"{left}{left}"

        finnal = int(new_bin, 2)

        if finnal > 76: 
            return finnal, i
            

result = new_binary_number()
print(result)