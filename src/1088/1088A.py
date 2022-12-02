x = int(input())
res = [x if x & 1 == 0 else x - 1, 2] if x > 1 else [-1]
print(*res)
