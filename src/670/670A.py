n = int(input())
d, r = divmod(n, 7)
res = 2 * d + (r == 6), 2 * d + min(2, r)
print(*res)
