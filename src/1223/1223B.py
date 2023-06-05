q = int(input())
for _ in range(q):
    s, t = input(), input()
    res = "YES" if set(s) & set(t) else "NO"
    print(res)
