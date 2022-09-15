t = int(input())
for _ in range(t):
    a, b, c = (int(i) for i in input().split())
    b, a = max(a, b), min(a, b)
    r = b - a
    d = c - r if c > r else c + r
    res = d if a <= r and min(c, d) <= r and d not in {a, b, c} else -1
    print(res)
