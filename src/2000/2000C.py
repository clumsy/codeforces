def matches(s, a):
    if len(s) != len(a):
        return False
    mc, md = {}, {}
    for c, d in zip(s, a):
        if md.get(d, c) != c or mc.get(c, d) != d:
            return False
        mc[c] = d
        md[d] = c
    return True


t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    m = int(input())
    for _ in range(m):
        s = input()
        res = "YES" if matches(s, a) else "NO"
        print(res)
