d1, d2, d3 = (int(i) for i in input().split())
res = min(d1 + d3 + d2, 2 * d1 + 2 * d2, d1 + 2 * d3 + d1, d2 + 2 * d3 + d2)
print(res)
