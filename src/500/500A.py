n, t = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
i = 0
while i < t - 1:
    i += a[i]
res = "YES" if i == t - 1 else "NO"
print(res)
