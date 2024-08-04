t = int(input())
for _ in range(t):
    n, m, k = (int(x) for x in input().split())
    res = min(n, k) * min(m, k)
    print(res)
