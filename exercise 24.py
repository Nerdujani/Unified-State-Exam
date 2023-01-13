f = open('23-203.txt')
st = f.readline()
kol = 0
for i in range(len(st)-2):
    for j in range(i+2, len(st)):
        s = st[i:j+1]

        if not('A' in s and 'B' in s and 'C' in s):
            kol += 1
            print(s)
        else:
            break

print(kol)
