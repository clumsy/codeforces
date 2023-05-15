t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = "NO"
    for i, e in enumerate(a):
        if e <= i + 1:
            res = "YES"
            break
    print(res)
