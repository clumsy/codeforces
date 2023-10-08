from collections import deque

t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = deque()
    for i in a:
        if res and i < res[0]:
            res.appendleft(i)
        else:
            res.append(i)
    print(*res)
