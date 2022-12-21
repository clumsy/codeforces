k, n, s, p = (int(i) for i in input().split())
res = (k * ((n + s - 1) // s) + p - 1) // p
print(res)
