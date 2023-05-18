t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    res = "YES" if n > 3 and len(set(s[: n // 2])) > 1 else "NO"
    print(res)
