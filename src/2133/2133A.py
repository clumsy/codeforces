t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res, s = "NO", set()
    for i in a:
        if i in s:
            res = "YES"
        s.add(i)
    print(res)
