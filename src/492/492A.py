n = int(input())
res, s, i = 0, 0, 1
while n > 0:
    s += i
    i += 1
    n -= s
    if n >= 0:
        res += 1
print(res)
