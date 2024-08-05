t = int(input())
for _ in range(t):
    n = int(input())
    a = (int(i) for i in input().split())
    res = sum(e * (1 if i & 1 == 0 else -1) for i, e in enumerate(a))
    print(res)
