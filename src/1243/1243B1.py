t = int(input())
for _ in range(t):
    n, s, t = int(input()), input(), input()
    si = ti = None
    for i in range(n):
        if s[i] != t[i]:
            si = i
            break
    for i in reversed(range(n)):
        if t[i] != s[i]:
            ti = i
            break
    if si is None or ti is None:
        res = "NO"
    else:
        s_, t_ = s[si], t[ti]
        s = s[:si] + t_ + s[si + 1 :]
        t = t[:ti] + s_ + t[ti + 1 :]
        res = "YES" if s == t else "NO"
    print(res)
