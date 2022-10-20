a, b, c, d, e, f = (int(input()) for i in range(6))
res = max(
    e * min(a, d) + f * min(b, c, d - min(a, d)),
    f * min(b, c, d) + e * min(a, d - min(b, c, d)),
)
print(res)
