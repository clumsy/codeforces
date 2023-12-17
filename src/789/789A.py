n, k = (int(i) for i in input().split())
p = sum((int(i) + k - 1) // k for i in input().split())
res = (p + 1) // 2
print(res)
