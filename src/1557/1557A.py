t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    mx = next(a)
    s = mx
    for i in a:
        mx = max(mx, i)
        s += i
    print((s - mx) / (n - 1) + mx)
