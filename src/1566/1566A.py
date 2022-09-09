t = int(input())
for _ in range(t):
    n, s = (int(i) for i in input().split())
    n -= (n - 1) // 2  # first (n - 1) // 2 are all 0s
    res = s // n  # next we evenly distribute s across remaining positions
    print(res)
