t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    e, o = set(), set()
    res = "YES"
    for i, c in enumerate(s):
        if i & 1 == 0:
            if c in o:
                res = "NO"
                break
            e.add(c)
        else:
            if c in e:
                res = "NO"
                break
            o.add(c)
    print(res)
