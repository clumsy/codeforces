b, g = (int(i) for i in input().split())
res = []
while b > 0 and g > 0:
    res.append((b, g))
    if b > g:
        b -= 1
    else:
        g -= 1
print(len(res))
for b, g in res:
    print(b, g)
