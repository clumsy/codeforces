n, a, b = (int(i) for i in input().split())
res = (((a - 1) + b) % n) + 1
print(res)
