a, b, c, d = (int(i) for i in input().split())
a, b, c = sorted((a, b, c))
# b's position is fixed
res = max(0, d - (b - a)) + max(0, d - (c - b))
print(res)
