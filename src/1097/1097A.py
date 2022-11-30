t, h = input(), input().split()
res = "YES" if any(t[0] == c[0] or t[1] == c[1] for c in h) else "NO"
print(res)
