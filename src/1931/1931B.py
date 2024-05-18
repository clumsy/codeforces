t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    x = sum(a) // n
    res, c = "YES", 0
    for i in a:
        i += c
        if i < x:
            res = "NO"
            break
        c = i - x
    res = "NO" if c != 0 else res
    print(res)
