n, k = (int(i) for i in input().split())
y = (int(i) for i in input().split())
res = sum(i + k <= 5 for i in y) // 3
print(res)
