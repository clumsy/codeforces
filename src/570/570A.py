n, m = (int(i) for i in input().split())
res = [0] * n
for _ in range(m):
    a = (int(i) for i in input().split())
    w = max((v, -i - 1) for i, v in enumerate(a))
    res[-w[1] - 1] += 1
res = -max((v, -i - 1) for i, v in enumerate(res))[1]
print(res)
