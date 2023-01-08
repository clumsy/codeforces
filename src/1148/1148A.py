a, b, c = (int(i) for i in input().split())
res = 2 * c + 2 * min(a, b) + (max(a, b) - min(a, b) > 0)
print(res)
