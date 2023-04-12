n, b, d = (int(i) for i in input().split())
a = (int(i) for i in input().split())
res = cur = 0
for i in a:
    if i > b:
        continue
    cur += i
    if cur > d:
        res += 1
        cur = 0
print(res)
