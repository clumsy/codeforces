n = int(input())
a = [int(i) for i in input().split()]
ma, res = 0, []
for i in reversed(range(n)):
    res.append(max(0, ma + 1 - a[i]))
    ma = max(ma, a[i])
res.reverse()
print(*res)
