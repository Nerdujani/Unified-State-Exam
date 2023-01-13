def f(a, b):
    if a > 9:
        p1 = a // 10
        p2 = a % 10
        k2 = f(p1 * p2, b)
        k1 = f(p1 + p2, b)
        return k1 + k2
    return a == b
kol = 0
for i in range(10, 100):
    if f(i, 8):
        kol += 1
print(kol)
