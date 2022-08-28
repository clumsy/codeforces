from heapq import heappush, heappop

t = int(input())
for _ in range(t):
    n, a = input(), (int(i) for i in input().split())
    h = []
    for i in a:
        heappush(h, i)
        if len(h) > 2:
            heappop(h)
    res = (len(h) == 1 and h[0] == 1) or (len(h) == 2 and h[1] - h[0] < 2)
    print("YES" if res else "NO")
