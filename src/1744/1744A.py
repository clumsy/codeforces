t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    s = input()
    m, res = {}, "YES"
    for i, e in enumerate(a):
        if m.get(e, s[i]) != s[i]:
            res = "NO"
            break
        m[e] = s[i]
    print(res)
