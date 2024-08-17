from itertools import repeat


t = int(input())
for _ in range(t):
    n, x, y = (int(i) for i in input().split())
    x, y = sorted([x, y])
    if x != 0 or y == 0 or (n - 1) % y != 0:
        res = [-1]
    else:
        res = [i for p in range(2, n + 1, y) for i in repeat(p, y)]
    print(*res)
