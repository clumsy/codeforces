t = int(input())
for _ in range(t):
    n, r = int(input()), (int(i) for i in input().split())
    m, b = int(input()), (int(i) for i in input().split())
    s1 = s = 0
    for i in r:
        s += i
        s1 = max(s1, s)
    s2 = s = 0
    for i in b:
        s += i
        s2 = max(s2, s)
    res = s1 + s2
    print(res)
