t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    mi = (2 * 1 + 2 * (k - 1)) * k // 2
    res = "YES" if n >= mi and n & 1 == k & 1 else "NO"
    print(res)
