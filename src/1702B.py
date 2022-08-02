t = int(input())
for _ in range(t):
    s = input()
    res = 1
    v = set()
    for c in s:
        if c not in v and len(v) == 3:
            v.clear()
            res += 1
        v.add(c)
    print(res)
