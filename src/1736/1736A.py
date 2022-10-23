from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = (int(i) for i in input().split())
    b = (int(i) for i in input().split())
    c = Counter(i - j for i, j in zip(a, b))
    if c[0] == n:
        res = 0  # identical
    elif c[-1] == c[1]:
        res = 1  # shuffled
    else:
        res = abs(c[-1] - c[1]) + (c[-1] > 0 and c[1] > 0)
    print(res)
