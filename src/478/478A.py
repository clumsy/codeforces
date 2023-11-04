c = (int(i) for i in input().split())
n = s = 0
for i in c:
    n += 1
    s += i
d, r = divmod(s, n)
res = d if d and not r else -1
print(res)
