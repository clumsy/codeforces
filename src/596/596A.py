from operator import sub

n = int(input())
xs, ys = set(), set()
for _ in range(n):
    x, y = (int(i) for i in input().split())
    xs.add(x)
    ys.add(y)
if n < 2 or len(xs) + len(ys) < 4:
    res = -1
else:
    res = abs(sub(*xs)) * abs(sub(*ys))
print(res)
