n, k = (int(i) for i in input().split())
res = (2 * n + k - 1) // k + (5 * n + k - 1) // k + (8 * n + k - 1) // k
print(res)
