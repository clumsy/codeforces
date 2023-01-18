t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    ma, mb, res = min(a), min(b), 0
    for ai, bi in zip(a, b):
        res += max(ai - ma, bi - mb)
    print(res)
