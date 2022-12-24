n, k = (int(i) for i in input().split())
res = "YES" if (n // k) & 1 == 1 else "NO"
print(res)
