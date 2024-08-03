from itertools import islice

t = int(input())
for _ in range(t):
    n = int(input())
    a = (int(x) for x in input().split())
    res = max(islice(a, 0, None, 2))
    print(res)
