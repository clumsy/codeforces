t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    cur, res = 0, "YES"
    for i, e in enumerate(a):
        i += 1
        if e < cur:
            res = "NO"
        elif i - (i & -i) == 0:  # power of 2
            cur = 0
        else:
            cur = e
    print(res)
