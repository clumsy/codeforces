t = int(input())
for _ in range(t):
    n, m, k = (int(i) for i in input().split())
    winner = min(n // k, m)
    runner_up = (m - winner + k - 2) // (k - 1)
    res = winner - runner_up
    print(res)
