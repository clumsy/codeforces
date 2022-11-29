a, b = (int(i) for i in input().split())
f, d, s = 0, 0, 0
for i in range(1, 7):
    d1, d2 = abs(i - a), abs(i - b)
    if d1 == d2:
        d += 1
    elif d1 < d2:
        f += 1
    else:
        s += 1
print(f, d, s)
