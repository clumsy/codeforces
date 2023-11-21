a, b, c = (int(i) for i in input().split())
# b = a + xc
d, r = divmod(b - a, c) if c else (-1, -1)
res = "YES" if a == b or (d >= 0 and r == 0) else "NO"
print(res)
