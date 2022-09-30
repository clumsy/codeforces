from collections import Counter

t = int(input())
for _ in range(t):
    n, c = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    res = sum(min(v, c) for _, v in Counter(a).items())
    print(res)
