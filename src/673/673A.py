n, t = int(input()), (int(i) for i in input().split())
res = 0
for i in t:
    if i - res > 15:
        break
    res = i
res = min(90, res + 15)
print(res)
