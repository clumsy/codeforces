n = int(input())
res = [-1] if n & 1 == 1 else [i for i in range(n, 0, -1)]
print(*res)
