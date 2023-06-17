n, m = (int(i) for i in input().split())
a = (int(i) for i in input().split())
res, left = 0, 0
for i in a:
    if i > left:
        res += 1
        left = m
    left -= i
print(res)
