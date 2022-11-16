m = 0
for n in range(1, 256):
    b1 = bin(n)[2:]
    b2 = '0' * (8 - len(b1)) + b1
    b2 = b2.replace('0', '9')
    b2 = b2.replace('1', '0')
    b2 = b2.replace('9', '1')
    r = int(b2, 2) - n
    if r == -21:
        print(n)
