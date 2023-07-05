x = int(input())
res = [x - (x & 1), 2] if x > 1 else [-1]
print(*res)
