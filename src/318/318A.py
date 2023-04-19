n, k = (int(i) for i in input().split())
half = (n + 1) // 2
res = 2 * (k if k <= half else k - half) - (k <= half)
print(res)
