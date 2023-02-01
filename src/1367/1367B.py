t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res, odd = 0, 0
    for i, e in enumerate(a):
        odd += e & 1
        res += e & 1 != i & 1
    res = -1 if odd != n // 2 else res // 2
    print(res)
