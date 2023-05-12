from math import inf

t = int(input())
for _ in range(t):
    n = int(input())
    a = (int(i) for i in input().split())
    b = (int(i) for i in input().split())
    ma_a = ma_b = -inf
    res = None
    for i, j in zip(a, b):
        i, j = min(i, j), max(i, j)
        ma_a = max(ma_a, i)
        ma_b = max(ma_b, j)
        res = "YES" if ma_a == i and ma_b == j else "NO"
    print(res)
