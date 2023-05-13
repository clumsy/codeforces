from collections import Counter

t = int(input())
for _ in range(t):
    n, a = int(input()), Counter(abs(int(i)) for i in input().split())
    res = list(range(1, len(a) + 1)) + list(
        range(len(a) - 1, len(a) - 1 - (n - len(a)), -1)
    )
    print(*res)
    res = [1, 0] * (n - len(a)) + list(range(1, sum(v == 1 for _, v in a.items()) + 1))
    print(*res)
