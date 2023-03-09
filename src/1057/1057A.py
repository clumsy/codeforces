n, p = int(input()), [int(i) for i in input().split()]
res = [n]
while n > 1:
    res.append(n := p[n - 2])
res.reverse()
print(*res)
