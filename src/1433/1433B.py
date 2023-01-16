t = int(input())
for _ in range(t):
    n, a = int(input()), "".join(i for i in input().split())
    s, e = a.index("1"), a.rindex("1")
    res = a[s:e].count("0")
    print(res)
