def f(x, a):
    return ((72 % x == 0) <= (120 % x != 0)) or (a - x > 100)


for a in range(1, 100000):
    if all(f(x, a) for x in range(1, 10000)):
        print(a)
        break
