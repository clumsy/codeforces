n, q = (int(i) for i in input().split())
p = sorted(int(i) for i in input().split())
for i in range(1, n):
    p[i] += p[i - 1]
for _ in range(q):
    x, y = (int(i) for i in input().split())
    res = p[n - x - 1 + y] - (p[n - x - 1] if n - x - 1 >= 0 else 0)
    print(res)
