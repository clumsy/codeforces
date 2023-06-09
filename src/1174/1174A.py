n, a = int(input()), sorted(int(i) for i in input().split())
res = a if sum(a[:n]) != sum(a[n:]) else [-1]
print(*res)
