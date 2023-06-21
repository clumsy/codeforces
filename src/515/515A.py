a, b, s = (int(i) for i in input().split())
d = abs(a) + abs(b)
res = "YES" if s >= d and d & 1 == s & 1 else "NO"
print(res)
