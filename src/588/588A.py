n = int(input())
res, prc = 0, 100
for _ in range(n):
    a, p = (int(i) for i in input().split())
    prc = min(prc, p)
    res += a * prc
print(res)
