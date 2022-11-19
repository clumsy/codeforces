x = sorted(int(i) for i in input().split())
res = (-(x[i] - x[-1]) for i in range(3))
print(*res)
