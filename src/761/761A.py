a, b = (int(i) for i in input().split())
res = "YES" if not (a == b == 0) and abs(a - b) < 2 else "NO"
print(res)
