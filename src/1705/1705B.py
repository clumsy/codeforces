t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = 0
    for i, e in enumerate(a):
        if i < n - 1:
            res += e if e > 0 else res > 0
    print(res)
