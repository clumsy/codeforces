k, l, m, n, d = (int(input()) for _ in range(5))
res = sum(1 for i in range(1, d + 1) if any(i % j == 0 for j in [k, l, m, n]))
print(res)
