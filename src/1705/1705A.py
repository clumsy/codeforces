t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    h = map(int, input().split())
    h = sorted(h)
    res = "YES"
    for i in range(n):
        if h[n + i] - h[i] < x:
            res = "NO"
            break
    print(res)
