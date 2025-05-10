t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    if n & 1 == 0:
        k -= k & 1
        res = (n + k - 1) // k
    elif k & 1 == 0:
        res = (n + k - 1) // k
    else:
        k_ = k - (k & 1)
        res = 1 + (n - min(n, k) + k_ - 1) // k_
    print(res)
