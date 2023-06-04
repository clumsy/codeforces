from collections import deque

n, k = (int(i) for i in input().split())
id = (int(i) for i in input().split())
res, dis = deque(), set()
for i in id:
    if i in dis:
        continue
    dis.add(i)
    res.append(i)
    if len(res) > k:
        dis.remove(res.popleft())
res.reverse()
print(len(res))
print(*res)
