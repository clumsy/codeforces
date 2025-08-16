from heapq import heappop, heappush


t = int(input())
for _ in range(t):
    x = int(input())
    q = [0, 0, 0]
    res = 0
    while True:
        cur = heappop(q)
        nxt = heappop(q)
        if cur == x:
            break
        cur = min(x, 2 * nxt + 1)
        heappush(q, cur)
        heappush(q, nxt)
        res += 1
    print(res)
