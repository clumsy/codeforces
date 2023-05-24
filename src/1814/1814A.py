t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    res = "YES" if n & 1 == 0 or (n >= k and k & 1 == 1) else "NO"
    print(res)
