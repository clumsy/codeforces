t = int(input())
for _ in range(t):
    l, r = (int(i) for i in input().split())

    def luckiness(i):
        s = sorted(str(i))
        return ord(s[-1]) - ord(s[0])

    max_luck = res = 0
    for i in range(max(l, r - 100), r + 1):
        luck = luckiness(i)
        if luck >= max_luck:
            res, max_luck = i, luck
    print(res)
