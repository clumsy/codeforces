n, a = int(input()), [int(i) for i in input().split()]
res = "NO" if n & 1 == 0 or a[0] & 1 == 0 or a[-1] & 1 == 0 else "YES"
print(res)
