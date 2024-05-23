t = int(input())
for _ in range(t):
    p = [int(i) for i in input().split()]
    if sum(i & 1 == 1 for i in p) & 1 == 1:
        res = -1
    else:
        d = p[2] - p[1]
        res = min(p[0], d)
        p[0] -= res
        p[2] -= res
        res += 2 * (p[0] // 2)
        res += p[1] - (p[0] // 2)
    print(res)
