from collections import deque

t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    # x = 1/3x + 2/3x = 1/9x + 2/9x + 4/9x
    # 2^a/3^b*x = m
    been = set()
    q = deque([m])
    while q:
        m = q.pop()
        if m > n or m in been:
            continue
        been.add(m)
        if m == n:
            break
        q.appendleft(3 * m)
        if m & 1 == 0:
            q.append(3 * (m // 2))
    res = "YES" if m == n else "NO"
    print(res)
