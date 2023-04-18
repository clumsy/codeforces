t, s, x = (int(i) for i in input().split())
res = "YES" if x == t or (x >= s + t and 0 <= (x - t) % s <= 1) else "NO"
print(res)
