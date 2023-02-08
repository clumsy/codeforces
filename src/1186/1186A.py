n, m, k = (int(i) for i in input().split())
res = "YES" if min(m, k) >= n else "NO"
print(res)
