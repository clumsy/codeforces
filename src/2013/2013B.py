t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = sum(e * (1 if i != n - 2 else -1) for i, e in enumerate(a))
    print(res)
