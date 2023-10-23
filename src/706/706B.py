from bisect import bisect_right

n, x = int(input()), sorted(int(i) for i in input().split())
q = int(input())
for _ in range(q):
    m = int(input())
    res = bisect_right(x, m)
    print(res)
