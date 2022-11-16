print ('x y z w')
from itertools import product
for x, y, z, w in product([0, 1], repeat = 4):
    f = not((x == y) or (x == w)) or z or not(y <= w)           #начальное условие задачи.
    if f == 0:          #значение F: 0 или 1
        print(x, y, z, w)