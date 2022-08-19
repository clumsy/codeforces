import itertools

t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    p = (int(i) for i in input().split())
    res = sum(1 for i in itertools.islice(p, k) if i > k)
    print(res)
