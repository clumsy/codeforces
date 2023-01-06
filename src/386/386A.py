n, p = int(input()), sorted((int(p), i + 1) for i, p in enumerate(input().split()))
res = p[-1][1], p[-2][0]
print(*res)
