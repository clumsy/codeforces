from collections import deque

a, b = (int(i) for i in input().split())
q = deque([[a]])
while q:
    cur = q.pop()
    if cur[-1] == b:
        break
    if cur[-1] < b:
        cpy = cur.copy()
        q.appendleft(cpy + [2 * cpy[-1]])
        q.appendleft(cur + [10 * cur[-1] + 1])
res = cur
if res and res[-1] == b:
    print("YES")
    print(len(res))
    print(*res)
else:
    print("NO")
