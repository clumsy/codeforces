from collections import Counter

t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    cnt, half = Counter(a), n // 2
    diff = cnt[-1] - (half - (half & 1))
    res = diff if diff >= 0 else cnt[-1] & 1
    print(res)
