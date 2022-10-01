t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = [int(i) for i in input().split()]
    res = 0
    for i in range(k):
        res += max(a[j] for j in range(i, n, k))
    print(res)
