t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    res = False
    for i in reversed(range(n)):
        if a[i] == 1:
            res = not res
        else:
            res = True
    res = "First" if res else "Second"
    print(res)
