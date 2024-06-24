t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    d = -1
    for i in range(n):
        s = input()
        lo = s.find("#")
        if lo >= 0:
            hi = s.rfind("#")
            if hi - lo > d:
                d = hi - lo
                r, c = i, lo + (hi - lo + 1) // 2
    res = r + 1, c + 1
    print(*res)
