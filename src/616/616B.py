n, m = (int(i) for i in input().split())
res = 0
for _ in range(n):
    res = max(res, min(int(i) for i in input().split()))
print(res)
