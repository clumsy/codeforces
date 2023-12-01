n, k = (int(i) for i in input().split())
res = [i for i in range(1, n + 1)]
res = res[: n - k - 1] + res[n - k - 1 :][::-1]
print(*res)
