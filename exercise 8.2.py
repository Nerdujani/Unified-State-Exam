from itertools import product
i = 0
for s in product(sorted('пятьдней'), repeat=4):
    s = ''.join(s)
    i += 1
    if 'я' not in s and s.count('е') == 0 and len(set(list(s))) == 4:
        print(i, s)
