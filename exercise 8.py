from itertools import product, repeat
from math import prod
k = 0
for s in product(['1', '2', '3', '4'], repeat = 3):         #первое: доступные цифры, второе: последовательность символов (кол-во).
    s = ''.join(s)
    if s.count('2') == 1:           #цифра которая есть хотя бы один раз, если условий больше одного можно довабить условие через and.
        k += 1
print (k)