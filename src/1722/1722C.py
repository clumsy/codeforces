from collections import Counter

points = {1: 3, 2: 1, 3: 0}
t = int(input())
for _ in range(t):
    _, p = input(), [input().split() for i in range(3)]
    total = Counter()
    total.update(p[0]), total.update(p[1]), total.update(p[2])
    res = [0] * 3
    for w1, w2, w3 in zip(p[0], p[1], p[2]):
        res[0] += points[total[w1]]
        res[1] += points[total[w2]]
        res[2] += points[total[w3]]
    print(*res)
