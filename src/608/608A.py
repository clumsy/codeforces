n, s = (int(i) for i in input().split())
a = sorted([[int(i) for i in input().split()] for _ in range(n)], reverse=True)
res = 0
for f, t in a:
    res = max(res + s - f, t)
    s = f
res += f
print(res)
