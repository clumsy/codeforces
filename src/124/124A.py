n, a, b = (int(i) for i in input().split())
# -> b- Petr a+
#     [a; n]
# [0; b]
res = min(n - a, b + 1)
print(res)
