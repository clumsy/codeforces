t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    e = o = 0
    for i in a:
        if i & 1 == 0:
            e += 1
        else:
            o += 1
    res = o + 1 if e > 0 else o - 1
    print(res)
