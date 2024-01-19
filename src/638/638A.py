n, a = (int(i) for i in input().split())
res = (a + 1) // 2 if a & 1 == 1 else ((n - a) // 2 + 1)
print(res)
