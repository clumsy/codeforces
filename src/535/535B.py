from collections import deque

n = input()
q = deque([""])
res = 0
while True:
    cur = q.pop()
    if cur == n:
        break
    q.appendleft(cur + "4")
    q.appendleft(cur + "7")
    res += 1
print(res)
