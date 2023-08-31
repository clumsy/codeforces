t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    res = 2  # always 1s at both ends
    lo, hi = 0, n - 1
    while hi - lo > k:
        res += 2
        lo += k
        hi -= k
    res -= lo >= hi
    print(res)
