from collections import deque

s = input()
d, n = deque(s), len(s)
res = []
while n:
    c = d.pop() if n & 1 == 0 else d.popleft()
    res.append(c)
    n -= 1
res = "".join(reversed(res))
print(res)
