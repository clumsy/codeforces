n, a = int(input()), (int(i) for i in input().split())
p, z = 0, 0
for i in a:
    if i == 0:
        z += 1
    elif i > 0:
        p += 1
res = 1 if p >= (n + 1) // 2 else -1 if (n - p - z) >= (n + 1) // 2 else 0
print(res)
