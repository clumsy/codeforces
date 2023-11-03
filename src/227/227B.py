n, a = int(input()), (int(i) for i in input().split())
m, b = int(input()), (int(i) for i in input().split())
mp = {v: i for i, v in enumerate(a)}
res = [0, 0]
for i in b:
    k = mp[i]
    res[0] += k + 1
    res[1] += n - k
print(*res)
