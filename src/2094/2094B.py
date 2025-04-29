t = int(input())
for _ in range(t):
    n, m, l, r = (int(i) for i in input().split())
    r = min(r, m)
    res = r - m, r
    print(*res)
