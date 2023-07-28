from collections import defaultdict
from bisect import bisect_left, bisect_right, insort

n = int(input())
xs, ys = defaultdict(list), defaultdict(list)
for _ in range(n):
    x, y = (int(i) for i in input().split())
    insort(xs[x], y)
    insort(ys[y], x)
res = 0
for x, y_list in xs.items():
    for y in y_list:
        res += (
            bisect_right(y_list, y - 1) > 0
            and bisect_left(y_list, y + 1) < len(y_list)
            and bisect_right(ys[y], x - 1) > 0
            and bisect_left(ys[y], x + 1) < len(ys[y])
        )
print(res)
