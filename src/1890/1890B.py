t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    s, t = (input() for _ in range(2))
    _00, _11 = "00" in s, "11" in s
    res = "YES"
    if _00 and _11:
        res = "NO"
    elif (_00 or _11) and len(t) & 1 == 0:
        res = "NO"
    elif _00 and t != ("10" * ((len(t) + 1) // 2))[:-1]:
        res = "NO"
    elif _11 and t != ("01" * ((len(t) + 1) // 2))[:-1]:
        res = "NO"
    print(res)
