n, a = int(input()), (int(i) for i in input().split())
res, b = 0, 0
for i in a:
    if i < 0 and b == 0:
        res += 1
    b = max(0, b + i)
print(res)
