n, a = int(input()), sorted(int(i) for i in input().split())
res = "YES" if a[n - 1] < a[n] else "NO"
print(res)
