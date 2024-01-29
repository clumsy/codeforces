n, k, n1 = (int(i) for i in input().split())
x = (n + n1 - 1) // n1
res = "YES" if k >= x**2 else "NO"
print(res)
