n, k, t = (int(i) for i in input().split())
res = min(t, n) - max(0, t - k)
print(res)
