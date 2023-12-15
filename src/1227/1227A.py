t = int(input())
for _ in range(t):
    n = int(input())
    l, r = [0] * n, [0] * n
    for i in range(n):
        l[i], r[i] = (int(i) for i in input().split())
    res = max(0, max(l) - min(r))
    print(res)
