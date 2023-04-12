n, m = (int(i) for i in input().split())
res = 0
while n > 0:
    res += 1
    n = n - 1 + (res % m == 0)
print(res)
