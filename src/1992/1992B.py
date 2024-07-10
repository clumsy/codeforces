t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    res = ma = 0
    for i in a:
        ma = max(ma, i)
        res += 2 * i - 1 if i > 1 else 1
    res -= 2 * ma - 1 if ma > 1 else 1
    print(res)
