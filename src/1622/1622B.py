from heapq import heappop, heappush


t = int(input())
for _ in range(t):
    n = int(input())
    p = [int(i) for i in input().split()]
    s = input()
    li, dl = [], []
    for i, r in enumerate(p):
        heappush(li if s[i] == "1" else dl, (-r, i))
    res = [None] * n
    while li:
        res[heappop(li)[1]] = n
        n -= 1
    while dl:
        res[heappop(dl)[1]] = n
        n -= 1
    print(*res)
