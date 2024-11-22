n, p = int(input()), 0
for _ in range(n):
    t, c = input().split()
    c = int(c)
    if t == "P":
        p += c
    else:
        res = "YES" if c - p > 0 else "NO"
        print(res)
        p = max(0, p - c)
