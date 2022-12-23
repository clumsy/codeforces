n, t = (int(i) for i in input().split())
a = (int(i) for i in input().split())
res = 0
while t > 0:
    t -= 86400 - next(a)
    res += 1
print(res)
