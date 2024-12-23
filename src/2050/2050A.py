t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    s = [input() for _ in range(n)]
    res = 0
    while res < n and m > 0:
        m -= len(s[res])
        if m >= 0:
            res += 1
    print(res)
