t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    res = list(range(1, n + 1))
    res = res[: n - k][::-1] + res[n - k :]
    print(*res)
