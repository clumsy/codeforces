from collections import deque

n, a = int(input()), deque(int(i) for i in input().split())
res = [0, 0]
for i in range(n):
    res[i & 1] += a.pop() if a[-1] > a[0] else a.popleft()
print(*res)
