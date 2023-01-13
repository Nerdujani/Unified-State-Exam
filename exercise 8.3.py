from itertools import permutations
kol = 0
for s in permutations('АМФИБРАХИЙ'):
    s = ''.join(s)
    if all(s[i] in 'МФБРХ' for i in range(1, len(s), 2)): # строка отвечающая за размещение согласых на чётных поз.
        kol += 1
print(kol // 2 // 2) # деление в ответе из-за особености permutations, имеются повторяющиеся буквы


