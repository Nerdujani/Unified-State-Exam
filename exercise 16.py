def f(n):
    if n == 0:
        return 1
    if 0 < n <= 10:
        return f(n-1)
    if 10 < n < 100:
        return 2.2 * f(n-3)
    if n >= 100:
        return 1.7 * f(n-2)

print(f(22))
