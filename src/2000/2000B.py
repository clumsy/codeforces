t = int(input())
for _ in range(t):
    n = int(input())
    a = (int(i) for i in input().split())
    res, s = "YES", set()
    for i in a:
        if s and i - 1 not in s and i + 1 not in s:
            res = "NO"
            break
        s.add(i)
    print(res)
