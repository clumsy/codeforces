n, k, l, c, d, p, nl, np = (int(i) for i in input().split())
res = min(k * l // nl, c * d, p // np) // n
print(res)
